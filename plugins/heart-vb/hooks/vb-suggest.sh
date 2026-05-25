#!/usr/bin/env bash
# UserPromptSubmit hook: detects venture-builder intent and suggests
# the most relevant skill(s) — not just /council.
#
# Activation: only fires on prompts matching VB signal patterns.
# Output: appends additionalContext instructing Claude to ASK the user
# whether to route through the suggested skill before answering directly.
#
# Disable globally: remove from ~/.claude/settings.json hooks.UserPromptSubmit
# Override per-prompt: prefix with "BEZ COUNCIL:" / "NO COUNCIL:" / "SKIP VB:"

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
if [ -z "$PROMPT" ]; then exit 0; fi
if [ "${#PROMPT}" -lt 40 ]; then exit 0; fi
if printf '%s' "$PROMPT" | grep -qiE '^(bez\s*council|no\s*council|skip\s*council|skip\s*vb)[: ]'; then exit 0; fi
if printf '%s' "$PROMPT" | grep -qE '^\s*/[a-z]'; then exit 0; fi  # any slash command

# ── Intent detection — match per category ────────────────────────────────────

match_count() {
  local prompt="$1"; shift
  local count=0
  for pat in "$@"; do
    if printf '%s' "$prompt" | grep -qiE "$pat"; then
      count=$((count + 1))
    fi
  done
  printf '%s' "$count"
}

# DECISION intent — multi-option choices, comparisons, build-vs-buy
DECISION_PAT=(
  '\b(versus|vs\.?)\b'
  '\b(co (wybrać|wybierzemy|wybieramy|lepiej|lepsze))\b'
  '\b(który (lepsz|wybrać))\b'
  '\b(czy (warto|powinniśmy))\b'
  '\b(build[- ]vs[- ]buy|build or buy)\b'
  '\b(pivot(ujem|ować)|go[/ ]no[- ]?go|fit[/ ]no[- ]?fit)\b'
  '\b(porównaj|porównanie|oceń|zdecyduj|decyzj)\b'
)

# RESEARCH intent — market, competitors, sizing, exploration
RESEARCH_PAT=(
  '\b(TAM|SAM|SOM|sizing rynku|rozmiar rynku|market size)\b'
  '\b(konkurent|competitor|landscape|teardown)\b'
  '\b(research|zbadaj|przeanalizuj|find out|deep[- ]dive)\b'
  '\b(jakie firmy|kto już|kto robi)\b'
)

# MODELING intent — financial models, unit econ, valuation
MODELING_PAT=(
  '\b(unit econom|CAC|LTV|payback|churn|MRR|ARR|ARPU)\b'
  '\b(DCF|WACC|comps|valuation|wycena|MOIC|IRR|breakeven)\b'
  '\b(P&L|cash[- ]?flow|3-statement|projekcj)\b'
  '\b(model finansowy|projekt budżetu)\b'
)

# WRITING intent — IC memo, pitch deck, investor materials
WRITING_PAT=(
  '\b(IC[-_ ]?memo|investment[- ]committee|term[- ]?sheet)\b'
  '\b(pitch[- ]deck|deck inwestorski|one[- ]pager|teaser|data[- ]?room)\b'
  '\b(napisz|zredaguj|wygeneruj|sporządź)\b.*\b(memo|deck|pitch|brief|spec|update|raport|prd|prezentacj)\b'
  '\b(stakeholder update|investor update)\b'
)

# VALIDATION intent — user research, experiments
VALIDATION_PAT=(
  '\b(JTBD|jobs[- ]to[- ]be[- ]done|persona|user research)\b'
  '\b(interview|wywiad z|talk to user)\b'
  '\b(experiment|smoke test|fake[- ]door|fake door|MVP)\b'
  '\b(zwaliduj|validate|hypothesis|hipotez)\b'
)

# SCREENING intent — incoming opportunity / founder / research fit
SCREENING_PAT=(
  '\b(founder fit|founder profile|założyciel)\b'
  '\b(profesor|naukowiec|patent|spin[- ]?out|commercializ|tech[- ]?transfer)\b'
  '\b(fit dla|dla nas|incoming|opportunity|inquiry)\b'
  '\b(DD checklist|due[- ]diligence|deal screen)\b'
)

# PRICING intent (special — usually triggers council + benchmarks)
PRICING_PAT=(
  '\b(pricing|cennik|tier|freemium|paid tier|enterprise tier)\b'
  '\b(price (point|elasticity)|monetiz)\b'
)

# SECTOR hints — adds context, doesn't trigger alone
SECTOR_PAT=(
  '\b(FinTech|HealthTech|MarTech|RealEstate|Real Estate)\b'
  '\b(KNF|RODO|AMLD|MDR|NFZ|MIFID|PSD2)\b'
  '\b(bank|przychodni|broker real estate|e[- ]commerce)\b'
)

DEC_HITS=$(match_count "$PROMPT" "${DECISION_PAT[@]}")
RES_HITS=$(match_count "$PROMPT" "${RESEARCH_PAT[@]}")
MOD_HITS=$(match_count "$PROMPT" "${MODELING_PAT[@]}")
WRT_HITS=$(match_count "$PROMPT" "${WRITING_PAT[@]}")
VAL_HITS=$(match_count "$PROMPT" "${VALIDATION_PAT[@]}")
SCR_HITS=$(match_count "$PROMPT" "${SCREENING_PAT[@]}")
PRI_HITS=$(match_count "$PROMPT" "${PRICING_PAT[@]}")
SEC_HITS=$(match_count "$PROMPT" "${SECTOR_PAT[@]}")

TOTAL=$((DEC_HITS + RES_HITS + MOD_HITS + WRT_HITS + VAL_HITS + SCR_HITS + PRI_HITS))

# Trigger threshold
if [ "$TOTAL" -lt 1 ]; then exit 0; fi
if [ "$TOTAL" -eq 1 ] && [ "$SEC_HITS" -eq 0 ]; then exit 0; fi  # single weak signal — skip

# ── Determine primary intent (highest hit count) ─────────────────────────────

PRIMARY="decision"
PRIMARY_HITS=$DEC_HITS

if [ "$RES_HITS" -gt "$PRIMARY_HITS" ]; then PRIMARY="research"; PRIMARY_HITS=$RES_HITS; fi
if [ "$MOD_HITS" -gt "$PRIMARY_HITS" ]; then PRIMARY="modeling"; PRIMARY_HITS=$MOD_HITS; fi
if [ "$WRT_HITS" -gt "$PRIMARY_HITS" ]; then PRIMARY="writing"; PRIMARY_HITS=$WRT_HITS; fi
if [ "$VAL_HITS" -gt "$PRIMARY_HITS" ]; then PRIMARY="validation"; PRIMARY_HITS=$VAL_HITS; fi
if [ "$SCR_HITS" -gt "$PRIMARY_HITS" ]; then PRIMARY="screening"; PRIMARY_HITS=$SCR_HITS; fi

# ── Map intent to skill suggestions ──────────────────────────────────────────

case "$PRIMARY" in
  decision)
    SKILLS="**/council** (Tier L) — multi-LLM debate dla decyzji. Lub jeśli to porównanie cech: critic --mode review."
    ;;
  research)
    SKILLS="**deep-research**, **market-research** lub **competitive-teardown** — depending on scope. Browser tools (**chrome-devtools-mcp**) > WebFetch dla multi-page research, znacząco taniej."
    ;;
  modeling)
    SKILLS="**unit-economics** (CAC/LTV/payback) lub **3-statement-model** (P&L+cashflow). Dla valuation: **dcf-model** + **comps-analysis**. Council dopiero przy interpretacji wyników."
    ;;
  writing)
    SKILLS="**ic-memo** (dla IC The Heart), **pitch-deck** (dla inwestorów), **investor-materials** (one-pagery), lub **stakeholder-update** (regularne update'y)."
    ;;
  validation)
    SKILLS="**product-discovery** (JTBD framework), **experiment-designer** (smoke test/fake door design), **customer-research** lub **ux-researcher-designer** (interview plan + synthesis)."
    ;;
  screening)
    SKILLS="**screen-deal** (quick fit/no-fit), **dd-checklist** (early DD signals), lub **dd-prep** (pełny case przed IC). Dla founder fit: council z personą 'VC partner'."
    ;;
esac

# Pricing usually = decision + modeling
if [ "$PRI_HITS" -ge 1 ]; then
  SKILLS="$SKILLS Bonus: pricing-strategy + comps-analysis dla benchmarków + council."
fi

# Sector hint adds compliance reminder
SECTOR_NOTE=""
if [ "$SEC_HITS" -ge 1 ]; then
  if printf '%s' "$PROMPT" | grep -qiE 'FinTech|KNF|AMLD|MIFID|PSD2|bank'; then
    SECTOR_NOTE=" ⚠️ FinTech kontekst — uwzględnij compliance (KNF, AMLD6, MIFID2, PSD2, RODO)."
  elif printf '%s' "$PROMPT" | grep -qiE 'HealthTech|MDR|NFZ|RODO art.?9|medycyn|klinicz'; then
    SECTOR_NOTE=" ⚠️ HealthTech kontekst — uwzględnij MDR, RODO art. 9, IRB approval."
  elif printf '%s' "$PROMPT" | grep -qiE 'RealEstate|Real Estate|nieruchom|broker'; then
    SECTOR_NOTE=" ⚠️ Real Estate kontekst — lokalność rynku PL, OtoDom/Morizon partnerships."
  elif printf '%s' "$PROMPT" | grep -qiE 'MarTech|e[- ]commerce|loyalty|Shopify'; then
    SECTOR_NOTE=" ⚠️ MarTech kontekst — Shopify/WooCommerce ecosystem, agency distribution."
  fi
fi

# ── Emit hint ────────────────────────────────────────────────────────────────

cat <<EOF
{
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "💡 [Venture Builder hook] User's prompt matches **${PRIMARY}** intent (decision:${DEC_HITS} research:${RES_HITS} modeling:${MOD_HITS} writing:${WRT_HITS} validation:${VAL_HITS} screening:${SCR_HITS} pricing:${PRI_HITS} sector:${SEC_HITS}). Suggested skill(s): ${SKILLS}${SECTOR_NOTE} BEFORE answering directly, briefly ask the user (Polish): 'To wygląda na zadanie typu \"${PRIMARY}\" — proponuję użyć: <wskazany skill>. Wolisz tak, czy odpowiedzieć od razu?'. Wait for their reply. Skip prompt on simple lookups (user can also prefix BEZ COUNCIL: to opt-out). For collection map: collections/venture-builder.md in The-Heart-Vibe/claude-code-marketplace."
  }
}
EOF
