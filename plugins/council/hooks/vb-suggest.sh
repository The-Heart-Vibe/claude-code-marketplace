#!/usr/bin/env bash
# UserPromptSubmit hook: detects venture-builder / decision prompts and asks
# Claude to confirm with the user whether to route through /council.
#
# Activation: only fires when prompt matches venture-builder signal patterns
# (multi-option choices, sector keywords, financial modeling, IC/pitch tasks).
#
# Output: appends additionalContext that instructs Claude to ASK the user
# first ("Czy uruchomić to przez /council?") before answering directly.
#
# Disable: remove from ~/.claude/settings.json hooks.UserPromptSubmit
# Override per-prompt: prefix message with "BEZ COUNCIL:" or "NO COUNCIL:"

set -euo pipefail

# Read hook payload (JSON with user_prompt and other context)
INPUT="$(cat)"

# Extract prompt safely (handles empty / malformed JSON)
PROMPT="$(printf '%s' "$INPUT" | python3 -c '
import json, sys
try:
    data = json.load(sys.stdin)
    print(data.get("prompt", data.get("user_prompt", "")))
except Exception:
    print("")
' 2>/dev/null || printf '')"

# Bail early on opt-outs and trivially short messages
if [ -z "$PROMPT" ]; then exit 0; fi
if [ "${#PROMPT}" -lt 40 ]; then exit 0; fi
# Explicit opt-out prefix
if printf '%s' "$PROMPT" | grep -qiE '^(bez\s*council|no\s*council|skip\s*council)[: ]'; then
  exit 0
fi
# Explicit invocation — user już woła council, nie podpowiadaj ponownie
if printf '%s' "$PROMPT" | grep -qE '^\s*/council\b'; then exit 0; fi

# ── Pattern matching ─────────────────────────────────────────────────────────
# Każda kategoria liczy się jako 1 "signal". Wymagamy ≥ 2 signals albo 1 strong.

STRONG_PATTERNS=(
  # Multi-option decisions (najsilniejszy signal)
  '\b(versus|vs\.?)\b'
  '\b(co (wybrać|wybierzemy|wybieramy|lepiej|lepsze))\b'
  '\b(który (lepsz|wybrać))\b'
  '\b(czy (warto|powinniśmy|warto iść))\b'
  # IC / pitch deliverables
  '\b(IC[-_ ]?memo|investment[- ]committee|pitch[- ]deck)\b'
  # Strategic decisions
  '\b(build[- ]vs[- ]buy|build or buy)\b'
  '\b(pivot(ujem|ować)|go[/ ]no[- ]?go|fit[/ ]no[- ]?fit)\b'
)

WEAK_PATTERNS=(
  # Decision verbs
  '\b(porównaj|porównanie|oceń|ocena|zdecyduj|decyzj)\b'
  # Financial modeling
  '\b(unit econom|CAC|LTV|DCF|comps|valuation|wycena|MOIC|IRR)\b'
  # Pricing / GTM
  '\b(pricing|cennik|GTM|go[- ]to[- ]market|positioning)\b'
  # Sectors & regulators (Heart-specific)
  '\b(FinTech|HealthTech|MarTech|RealEstate|Real Estate|KNF|RODO|AMLD|MDR|NFZ|MIFID|PSD2)\b'
  # Venture / founder
  '\b(founder|co[- ]?founder|venture|spin[- ]?out|commercializ|opportunity|MVP|PoC)\b'
  # Market sizing
  '\b(TAM|SAM|SOM|sizing rynku|rozmiar rynku)\b'
  # Risk / assessment
  '\b(ryzyk|risk|trade[- ]off|opportunity cost)\b'
)

count_matches() {
  local prompt="$1"
  shift
  local count=0
  for pat in "$@"; do
    if printf '%s' "$prompt" | grep -qiE "$pat"; then
      count=$((count + 1))
    fi
  done
  printf '%s' "$count"
}

STRONG_HITS=$(count_matches "$PROMPT" "${STRONG_PATTERNS[@]}")
WEAK_HITS=$(count_matches "$PROMPT" "${WEAK_PATTERNS[@]}")

# Trigger: 1+ strong OR 2+ weak
if [ "$STRONG_HITS" -lt 1 ] && [ "$WEAK_HITS" -lt 2 ]; then
  exit 0
fi

# ── Determine suggested tier ─────────────────────────────────────────────────
# Heuristic: more weak patterns = bigger decision = higher tier

TIER="M"
if [ "$STRONG_HITS" -ge 1 ] && [ "$WEAK_HITS" -ge 2 ]; then TIER="L"; fi
if [ "$STRONG_HITS" -ge 2 ] || [ "$WEAK_HITS" -ge 4 ]; then TIER="L"; fi
if [ "$WEAK_HITS" -ge 6 ]; then TIER="XL"; fi

# Detect domain — non-tech if business/pricing/GTM/sector keywords dominate
DOMAIN="tech"
if printf '%s' "$PROMPT" | grep -qiE '\b(pricing|GTM|FinTech|HealthTech|MarTech|RealEstate|positioning|IC[- ]memo|pitch|unit econom|CAC|LTV|founder|venture|MVP brief|persona|customer)\b'; then
  DOMAIN="non-tech"
fi

# ── Emit hint to Claude ──────────────────────────────────────────────────────

cat <<EOF
{
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "💡 [Venture Builder hook] User's prompt matched ${STRONG_HITS} strong + ${WEAK_HITS} weak venture-builder signals (suggested tier: ${TIER}, domain: ${DOMAIN}). BEFORE answering, briefly ask the user in Polish: 'Wygląda mi to na decyzję wartą uruchomienia przez /council (tier ${TIER}, domain ${DOMAIN}). Wolisz to puścić przez radę, czy odpowiedzieć od razu?' — wait for their answer. If they decline OR it's actually a simple lookup, answer directly without council. To skip hook on a single message, user can prefix with 'BEZ COUNCIL:'."
  }
}
EOF
