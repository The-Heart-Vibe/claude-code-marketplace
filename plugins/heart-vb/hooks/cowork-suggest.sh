#!/usr/bin/env bash
# UserPromptSubmit hook: detects multi-entity tasks (research X companies,
# build N scenarios, draft sections per persona) and suggests spawning
# parallel cowork agents instead of doing it sequentially in main session.
#
# Recommendation: workers on model:sonnet, main stays on opus as orchestrator.
#
# Opt-out per-prompt: "BEZ COWORK:" / "NO COWORK:" / "SINGLE SESSION:"

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
[ "${#PROMPT}" -lt 40 ] && exit 0

if printf '%s' "$PROMPT" | grep -qiE '^(bez\s*cowork|no\s*cowork|skip\s*cowork|single\s*session)[: ]'; then
  exit 0
fi
if printf '%s' "$PROMPT" | grep -qE '^\s*/[a-z]'; then exit 0; fi

# ── Extract explicit numbers (top 5, 3 firmy, etc.) ──────────────────────────

NUMBERS=$(printf '%s' "$PROMPT" | { grep -oE '\b[0-9]+\b' || true; } | head -10)
MAX_N=0
for n in $NUMBERS; do
  if [ "$n" -gt "$MAX_N" ] && [ "$n" -lt 100 ]; then
    MAX_N=$n
  fi
done

# ── Multi-entity patterns ────────────────────────────────────────────────────

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

# Numeric multi-entity (3+ entities of known type)
NUMERIC_MULTI=(
  '\b([3-9]|[1-9][0-9])\s*(konkurent|competitor|companies|compan|firm|firmy|sektor|sector|scenari|venture|persona|interview|wywiad|product|vendor|kraj|country|miast|cit|opcj|option)\w*\b'
  '\bdla\s+[3-9]\s+'
  '\b(top|first|pierwsz)\s+([3-9]|[1-9][0-9])\b'
)

# Iteration-friendly markers
ITERATION_PAT=(
  '\b(dla każd[eai]|for each|per (company|company|persona|item|country|kraj))\b'
  '\b(po jednym (na|dla)|one per|jeden (na|dla))\b'
  '\b(each (of|with)|każd[ay] z (tych|nich|powyższych))\b'
)

# Multi-scenario keywords
SCENARIO_PAT=(
  '\b(base|baseline|bull|bear|optimistic|pessimistic|conservative|aggressive)\s*(case|scenario|scenariusz)\b'
  '\b(what[- ]?if|sensitivity|stress[- ]?test|monte[- ]?carlo)\b'
  '\b(3 scenari|trzy scenari|three scenari|N scenari)\w*\b'
)

# Comparative landscape work
COMPARATIVE_PAT=(
  '\b(porównaj|porównanie|compare|comparison)\b.{0,40}\b(vs|przeciw|między|across|wobec)\b'
  '\b(landscape|teardown|matrix|map)\b.{0,30}\b(competitive|konkurenc|sektorow|sector)\b'
  '\b(scan|przeskanuj|przeglad).*\b(rynk|market|landscape|sektor)\b'
)

# Multi-section deliverables (IC memo with multiple sections, deck slides)
MULTISECTION_PAT=(
  '\b([3-9]|[1-9][0-9])\s*(sekcj|section|slide|chapter|rozdział|part)\w*\b'
  '\b(executive summary|thesis|risks|financials|team|moat|ask).*(executive summary|thesis|risks|financials|team|moat|ask)\b'  # multiple memo sections mentioned
)

# Parallel hint explicit
EXPLICIT_PARALLEL=(
  '\b(parallel|równolegl|in parallel|jednocześnie|w tym samym czasie)\b'
  '\b(spawn|wyspawnuj)\b'
)

NUMERIC_HITS=$(match_any "$PROMPT" "${NUMERIC_MULTI[@]}")
ITER_HITS=$(match_any "$PROMPT" "${ITERATION_PAT[@]}")
SCENARIO_HITS=$(match_any "$PROMPT" "${SCENARIO_PAT[@]}")
COMP_HITS=$(match_any "$PROMPT" "${COMPARATIVE_PAT[@]}")
SECTION_HITS=$(match_any "$PROMPT" "${MULTISECTION_PAT[@]}")
EXPLICIT_HITS=$(match_any "$PROMPT" "${EXPLICIT_PARALLEL[@]}")

TOTAL=$((NUMERIC_HITS + ITER_HITS + SCENARIO_HITS + COMP_HITS + SECTION_HITS + EXPLICIT_HITS))

# Threshold: 1+ signal OR explicit N >= 3 OR explicit parallel keyword
if [ "$TOTAL" -lt 1 ] && [ "$MAX_N" -lt 3 ]; then
  exit 0
fi

# Determine N (suggested agent count)
N=3
if [ "$MAX_N" -ge 3 ] && [ "$MAX_N" -le 10 ]; then
  N=$MAX_N
elif [ "$MAX_N" -gt 10 ]; then
  N=5  # cap suggestion at 5 — more = diminishing returns
fi

# Determine workflow type
WORKFLOW="parallel research"
if [ "$SCENARIO_HITS" -ge 1 ]; then WORKFLOW="parallel scenarios (base/bull/bear-style)"; fi
if [ "$SECTION_HITS" -ge 1 ]; then WORKFLOW="parallel section drafts"; fi
if [ "$COMP_HITS" -ge 1 ]; then WORKFLOW="parallel competitive teardown"; fi

cat <<EOF
{
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "🤖 [Cowork Spawn Router] Multi-entity task detected (signals: numeric=$NUMERIC_HITS iteration=$ITER_HITS scenario=$SCENARIO_HITS comparative=$COMP_HITS sections=$SECTION_HITS explicit=$EXPLICIT_HITS, N hint: $MAX_N). Sugeruję heart-orchestrate w stylu '${WORKFLOW}' z ${N} workers parallel. ZAWSZE najpierw spytaj user PLAIN LANGUAGE — np. 'Mogę zapytać ${N} ekspertów żeby przebadać te tematy równolegle? (a) tak, (b) Ty sam, (c) sam wiem'. NIE używaj 'Pattern E/F' jargon w pytaniu — user nie rozumie. Jeśli yes → spawn Agent(model:'sonnet') × ${N}, synthesize w main (Opus). NIE używaj orchestrate dla: pojedyncza decyzja, sequential reasoning, single lookup, final synthesis. Opt-out per-prompt: 'BEZ COWORK:' lub 'SINGLE SESSION:'. Pełne patterns: skills/heart-custom/heart-orchestrate/SKILL.md (KROK -1 confirmation pattern)."
  }
}
EOF
