#!/usr/bin/env bash
# UserPromptSubmit hook: classifies task complexity and suggests appropriate
# Claude model tier (Haiku / Sonnet / Opus) for cost/quality optimization.
#
# Logic:
#   - Trivial lookup / formatting → suggest Haiku (cheap)
#   - Strategic / complex reasoning → suggest Opus (deep)
#   - Default (routine) → silent (Sonnet is the default, no suggestion needed)
#
# Cowork integration: workers should be on sonnet, main on opus.
#
# Opt-out per-prompt: "BEZ ROUTE:" / "NO ROUTE:" / "SKIP MODEL ROUTE:"

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

[ -z "$PROMPT" ] && exit 0
[ "${#PROMPT}" -lt 30 ] && exit 0

if printf '%s' "$PROMPT" | grep -qiE '^(bez\s*route|no\s*route|skip\s*model\s*route)[: ]'; then
  exit 0
fi
if printf '%s' "$PROMPT" | grep -qE '^\s*/[a-z]'; then exit 0; fi

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

# TRIVIAL patterns → Haiku (cheap, fast)
TRIVIAL_PAT=(
  '\b(co znaczy|what (is|does)|definicj|define|explain[- ]simply|wyjaśnij prost)\b'
  '\b(format|sformatuj|przekonwertuj|convert (to|into)|encode|decode)\b'
  '\b(rename|zmień nazwę|zmień tytuł)\b'
  '\b(literówk|spell[- ]?check|typo|gramatyk|grammar check)\b'
  '\b(quick (lookup|check|definition|summary)|szybka definicj|szybkie sprawdzenie)\b'
  '\b(jak się pisze|how to spell|jak nazwać)\b'
  '\b(skróć|abbreviate|jednym zdaniem|in one sentence|one[- ]liner)\b'
)

# COMPLEX patterns → Opus (deep reasoning, strategic)
COMPLEX_PAT=(
  '\b(strategic|strategia|long[- ]term|10[- ]year|long horizon)\b'
  '\b(architektur|architecture|system design|design system)\b'
  '\b(ambiguous|niejasn|trade[- ]?off|tradeoff|opportunity cost)\b'
  '\b(IC[- ]?memo|investment[- ]committee|board[- ]?prep|board prep)\b'
  '\b(pivot|major decision|big bet|strategic decision|critical decision)\b'
  '\b(council|multi[- ]LLM|adversarial debate|red[- ]?team)\b'
  '\b(synthesize|synteza|integrate findings|łącz wnioski)\b'
  '\b(ethical|etyczn|moral implications|implikacje moralne)\b'
  '\b(novel|nowatorsk|pionierski|first[- ]of[- ]kind)\b'
  '\b(value[- ]creation|moat analysis|competitive positioning)\b'
)

# DEEP-RESEARCH patterns → Opus (heavy reasoning over data)
DEEP_RESEARCH_PAT=(
  '\b(deep[- ]research|deep dive|comprehensive analysis|kompleksowa analiza)\b'
  '\b(TAM.*SAM.*SOM|landscape teardown)\b'
  '\b(scenario planning|scenariusz|planowanie scenariuszy)\b'
)

TRIV_HITS=$(match_any "$PROMPT" "${TRIVIAL_PAT[@]}")
COMPLEX_HITS=$(match_any "$PROMPT" "${COMPLEX_PAT[@]}")
DEEP_HITS=$(match_any "$PROMPT" "${DEEP_RESEARCH_PAT[@]}")

# ── Decide tier ──────────────────────────────────────────────────────────────

TIER=""
REASON=""

if [ "$COMPLEX_HITS" -ge 2 ] || [ "$DEEP_HITS" -ge 1 ] && [ "$COMPLEX_HITS" -ge 1 ]; then
  TIER="opus"
  REASON="strategic/complex reasoning task (complex:$COMPLEX_HITS deep:$DEEP_HITS) — Opus daje najlepsze deep reasoning"
elif [ "$COMPLEX_HITS" -ge 1 ]; then
  TIER="opus"
  REASON="single strong complex signal (complex:$COMPLEX_HITS) — Opus warto dla wysokiej-stake decisions"
elif [ "$TRIV_HITS" -ge 2 ]; then
  TIER="haiku"
  REASON="trivial/lookup task ($TRIV_HITS signals) — Haiku jest 3× tańszy i wystarczający"
elif [ "$TRIV_HITS" -eq 1 ] && [ "${#PROMPT}" -lt 100 ]; then
  TIER="haiku"
  REASON="krótkie pytanie ($(echo $PROMPT | wc -w | tr -d ' ') słów) z trivial signal — Haiku wystarczy"
fi

# If no clear classification → silent (default Sonnet is fine)
[ -z "$TIER" ] && exit 0

# ── Build recommendation message ─────────────────────────────────────────────

case "$TIER" in
  haiku)
    GUIDANCE="Suggest /model claude-haiku for this. Lub jeśli spawnujesz agenta — model:'haiku'. Sonnet też zadziała ale Haiku jest 3× tańszy dla tego typu zadań."
    ;;
  opus)
    GUIDANCE="Suggest pozostać na /model claude-opus dla main session (deep reasoning). Jeśli spawnujesz cowork agents — workers na 'sonnet' (model:sonnet), orchestrator (main) na opus. Pattern: rozważ /think lub plan mode dla extra reasoning budget."
    ;;
esac

cat <<EOF
{
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "🎚️ [Model Router] Detected complexity tier: ${TIER}. Reason: ${REASON}. ${GUIDANCE} Cowork pattern reminder: orchestrator (main) na opus, workers (Agent tool calls) na sonnet, trivial helpers na haiku — explicit 'model:' parameter w Agent calls. Opt-out: prefix 'BEZ ROUTE:'."
  }
}
EOF
