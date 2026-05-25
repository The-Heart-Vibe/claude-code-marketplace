#!/usr/bin/env bash
# UserPromptSubmit hook: detects research prompts with URLs + complexity
# signals and routes Claude toward chrome-devtools-mcp instead of WebFetch
# when appropriate (token-saving).
#
# Activates only when:
#   - Prompt contains URL(s) AND
#   - 2+ URLs (multi-page = DevTools territory), OR
#   - 1 URL + at least one signal (JS-heavy domain, interactive flow,
#     dynamic content, targeted extraction)
#
# Output: appends additionalContext instructing Claude to use DevTools.
#
# Disable globally: remove from ~/.claude/settings.json hooks.UserPromptSubmit
# Override per-prompt: prefix with "BEZ DEVTOOLS:" / "NO DEVTOOLS:" / "USE WEBFETCH:"

set -euo pipefail

INPUT="$(cat)"

PROMPT="$(printf '%s' "$INPUT" | python3 -c '
import json, sys
try:
    data = json.load(sys.stdin)
    print(data.get("prompt", data.get("user_prompt", "")))
except Exception:
    print("")
' 2>/dev/null || printf '')"

# Bail conditions
[ -z "$PROMPT" ] && exit 0
[ "${#PROMPT}" -lt 30 ] && exit 0

if printf '%s' "$PROMPT" | grep -qiE '^(bez\s*devtools|no\s*devtools|use\s*webfetch|skip\s*devtools)[: ]'; then
  exit 0
fi
if printf '%s' "$PROMPT" | grep -qE '^\s*/[a-z]'; then exit 0; fi  # slash command

# ── URL detection ────────────────────────────────────────────────────────────

# grep returns 1 when no match → wrap in subshell with `|| true` to satisfy pipefail
URL_COUNT=$(printf '%s' "$PROMPT" | { grep -oE 'https?://[^[:space:]<>")]+' || true; } | wc -l | tr -d ' ')
[ "$URL_COUNT" -lt 1 ] && exit 0

# ── Pattern matching ─────────────────────────────────────────────────────────

match_any() {
  local prompt="$1"; shift
  local count=0
  for pat in "$@"; do
    if printf '%s' "$prompt" | grep -qiE "$pat"; then
      count=$((count + 1))
    fi
  done
  printf '%s' "$count"
}

# JS-heavy domains where WebFetch fails or sees only shell HTML
JS_HEAVY_DOMAINS=(
  'g2\.com'
  'capterra\.com'
  'producthunt\.com'
  'crunchbase\.com'
  'pitchbook\.com'
  'linkedin\.com'
  'twitter\.com'
  'x\.com[/]'
  'facebook\.com'
  'instagram\.com'
  'apps?\.shopify\.com'
  'app\.[a-z]+\.[a-z]{2,}'      # SaaS apps
  'dashboard\.[a-z]+\.[a-z]{2,}'
  'console\.[a-z]+\.[a-z]{2,}'
  'admin\.[a-z]+\.[a-z]{2,}'
  'medium\.com[/]'              # JS rendering
  'substack\.com'
  'notion\.so'
  'figma\.com'
  'salesforce\.com'
  'allegro\.pl[/].*-[0-9]'     # Allegro listings (dynamic)
  'otodom\.pl'
  'morizon\.pl'
  'rocketreach\.co'
  'apollo\.io'
  'sales\.navigator'
  'glassdoor\.com[/].*\.htm$'
)

# Interactive flow signals
INTERACTIVE_PAT=(
  '\b(klik|kliknij|click|scroll|przewi[jń])\b'
  '\b(wype[łl]ni|fill[- ]?out|fill[- ]?in|submit|sign[- ]?in|log[- ]?in|zaloguj)\b'
  '\b(navigate to|przejd[źz] do|po klikn|after clicking)\b'
  '\b(behind login|after auth|session|cookies)\b'
)

# Dynamic content signals
DYNAMIC_PAT=(
  '\b(infinite scroll|lazy[- ]?load|dynamic|JavaScript|JS[- ]?heavy)\b'
  '\b(SPA|single[- ]?page[- ]?app)\b'
  '\b(zobacz wszystk|see all|load more|wczytaj wi[ęe]cej|pokaż wszystkie)\b'
  '\b(react|vue|angular|next\.?js|svelte)\b'
)

# Targeted extraction signals (user wants specific data, not whole page)
TARGETED_PAT=(
  '\b(wyci[ąa]gnij|pobierz|extract|scrape|grab)\b.{0,40}\b(list|tabela|table|tier|pricing|nazwy|cen|cena)\b'
  '\b(top [0-9]+|first [0-9]+|pierwsze [0-9]+)\b'
  '\b(z każd[eai]|each|wszystkie|all the)\b.{0,30}\b(stron|page|firm|company)\b'
  '\b(selektor|selector|CSS|querySelector|class[ -]?\.|h[1-6] tag)\b'
)

# Research workflow signals (researching multiple competitors/sites)
WORKFLOW_PAT=(
  '\b(konkurenc|competitor|alternativ|porównaj firm)\b.{0,40}\b(pricing|features|tier)\b'
  '\b(scan|przeskanuj|przejrz[yj] [0-9]+ stron)\b'
  '\b(landscape|teardown).*\b(competitive|konkurenc)\b'
)

JS_HITS=$(match_any "$PROMPT" "${JS_HEAVY_DOMAINS[@]}")
INTERACTIVE_HITS=$(match_any "$PROMPT" "${INTERACTIVE_PAT[@]}")
DYNAMIC_HITS=$(match_any "$PROMPT" "${DYNAMIC_PAT[@]}")
TARGETED_HITS=$(match_any "$PROMPT" "${TARGETED_PAT[@]}")
WORKFLOW_HITS=$(match_any "$PROMPT" "${WORKFLOW_PAT[@]}")

MULTI_PAGE=0
[ "$URL_COUNT" -ge 2 ] && MULTI_PAGE=1

SIGNAL_SCORE=$((JS_HITS + INTERACTIVE_HITS + DYNAMIC_HITS + TARGETED_HITS + WORKFLOW_HITS + MULTI_PAGE))

# Threshold: single static URL with no signals → let Claude use WebFetch
if [ "$URL_COUNT" -eq 1 ] && [ "$SIGNAL_SCORE" -eq 0 ]; then
  exit 0
fi

# ── Determine primary reason ─────────────────────────────────────────────────

REASON=""
if [ "$MULTI_PAGE" -eq 1 ] && [ "$URL_COUNT" -ge 3 ]; then
  REASON="multi-page workflow ($URL_COUNT URLs — DevTools z jedną sesją oszczędza N× re-load tax vs. N×WebFetch)"
elif [ "$JS_HITS" -ge 1 ]; then
  REASON="JS-heavy domain ($JS_HITS dopasowań) — WebFetch widzi tylko shell HTML, DevTools renderuje JS"
elif [ "$INTERACTIVE_HITS" -ge 1 ]; then
  REASON="interactive flow signaled — WebFetch nie umie click/fill/navigate, potrzebny DevTools"
elif [ "$DYNAMIC_HITS" -ge 1 ]; then
  REASON="dynamic content (infinite scroll / lazy load / SPA) — WebFetch widzi tylko initial state"
elif [ "$TARGETED_HITS" -ge 1 ]; then
  REASON="targeted extraction — DevTools evaluate_script zwraca ~200 tok dokładnie tego co prosisz; WebFetch summary może zgubić niuanse"
elif [ "$WORKFLOW_HITS" -ge 1 ]; then
  REASON="competitive research workflow — DevTools sesja przez wiele stron znacznie taniej niż N×WebFetch"
elif [ "$MULTI_PAGE" -eq 1 ]; then
  REASON="multiple URLs ($URL_COUNT) — DevTools z evaluate_script per page oszczędza tokeny vs N×WebFetch"
else
  REASON="signals match (score $SIGNAL_SCORE)"
fi

# ── Emit hint ────────────────────────────────────────────────────────────────

cat <<EOF
{
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "🔧 [Research Tool Router] Detected $URL_COUNT URL(s) + signals (js:$JS_HITS interactive:$INTERACTIVE_HITS dynamic:$DYNAMIC_HITS targeted:$TARGETED_HITS workflow:$WORKFLOW_HITS multi-page:$MULTI_PAGE). Reason for DevTools: ${REASON}. STRONG RECOMMENDATION: użyj chrome-devtools-mcp zamiast WebFetch. Wzorzec: (1) navigate_page do URL, (2) evaluate_script z konkretnym CSS selectorem (NOT take_snapshot — zjada 2-8k tok). Dla multi-URL: jedna sesja browser, navigate między stronami → compounding savings (1 sesja x N evaluate_script ~200 tok każdy = ~$((URL_COUNT * 300)) tok vs ${URL_COUNT}×WebFetch ~$((URL_COUNT * 600))+ tok summary). PRZED użyciem WebFetch, zapytaj user 'WebFetch czy DevTools z evaluate_script?' (chyba że user jasno preferuje WebFetch). Opt-out per-prompt: prefix 'BEZ DEVTOOLS:' / 'USE WEBFETCH:'. Pełen wzorzec w collections/venture-builder.md sekcja Token-efficient practices."
  }
}
EOF
