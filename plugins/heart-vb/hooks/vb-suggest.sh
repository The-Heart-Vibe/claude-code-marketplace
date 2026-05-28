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

# BRAINSTORM intent — generic exploratory tasks bez clear VB context
# (organizacja eventu, struktura spotkania, ad-hoc decyzja, draft komunikacji,
#  refleksja strategiczna). Fall-through gdy żaden inny intent nie pasuje.
BRAINSTORM_PAT=(
  '\b(pomyśl|pomysl) ze mną\b'
  '\b(pomóż|pomoz) mi (z|ułożyć|ulozyc|zaplanować|zaplanowac|przemyśleć|przemysl|wymyślić|wymyslic|ogarn)\b'
  '\b(jak (ułożyć|ulozyc|zorganiz|zaplanować|zaplanowac|podejść|podejsc|ugryźć|ugryzc|ogarn|napisać|napisac))\b'
  '\b(co (napisać|napisac|odpowiedzieć|odpowiedziec)) (.*do|.*na)\b'
  '\b(nie wiem (jak|od czego))\b'
  '\b(mam (pomysł|pomysl|ideę|idee).*(pomóż|pomoz|ułóż|uloz))\b'
  '\b(agenda spotkania|struktura warsztatu|format eventu|plan retreat)\b'
  '\b(brainstorm|burza mózgów|burza mozgow|przemyśl|przemysl)\b'
  '\b(zorganiz(uj|ować|owac) (mi|spotkanie|warsztaty|event|retreat))\b'
)

# SECTOR hints — adds context, doesn't trigger alone
# Heart portfolio focus: HealthTech, Academic spinouts, Energy storage, FinTech (legacy)
SECTOR_PAT=(
  '\b(FinTech|HealthTech|CleanTech|EnergyTech|energ(ia|etyk|ii)|magazyn(y)? energii|BESS|V2G|fotowoltaik|PV|wiatr|offshore wind|nuclear|SMR|OZE|elektrolizer|wodór|H2|electrolyzer|hydrogen|heat pump|pompa ciepła|biogaz|biogas|ciepłownict|district heating)\b'
  '\b(academic spinout|spin[- ]?out|tech transfer|uczelni|profesor|PAN|NCBR|NCN|patent|IP commercializ)\b'
  '\b(KNF|RODO|AMLD|MDR|NFZ|MIFID|PSD2|EU Battery|CSRD|EU Taxonomy|RED III|EU ETS|EPBD|Fit-for-55|CBAM)\b'
  '\b(bank|przychodni|klinika|szpital|PSE|TSO|DSO|PGE|Tauron|Enea|Energa|URE|TGE|Orlen|KGHM|CPO|EMSP|ładowarka|charger|charging)\b'
)

DEC_HITS=$(match_count "$PROMPT" "${DECISION_PAT[@]}")
RES_HITS=$(match_count "$PROMPT" "${RESEARCH_PAT[@]}")
MOD_HITS=$(match_count "$PROMPT" "${MODELING_PAT[@]}")
WRT_HITS=$(match_count "$PROMPT" "${WRITING_PAT[@]}")
VAL_HITS=$(match_count "$PROMPT" "${VALIDATION_PAT[@]}")
SCR_HITS=$(match_count "$PROMPT" "${SCREENING_PAT[@]}")
PRI_HITS=$(match_count "$PROMPT" "${PRICING_PAT[@]}")
SEC_HITS=$(match_count "$PROMPT" "${SECTOR_PAT[@]}")
BRN_HITS=$(match_count "$PROMPT" "${BRAINSTORM_PAT[@]}")

TOTAL=$((DEC_HITS + RES_HITS + MOD_HITS + WRT_HITS + VAL_HITS + SCR_HITS + PRI_HITS))

# Trigger threshold
# Brainstorming jest fall-through: fire'uje gdy BRAINSTORM_PAT match a żaden VB intent nie złapał
if [ "$TOTAL" -lt 1 ] && [ "$BRN_HITS" -lt 1 ]; then exit 0; fi
if [ "$TOTAL" -eq 1 ] && [ "$SEC_HITS" -eq 0 ] && [ "$BRN_HITS" -eq 0 ]; then exit 0; fi  # single weak signal — skip

# ── Determine primary intent (highest hit count) ─────────────────────────────

# Fall-through to brainstorming gdy żaden VB intent nie złapał (TOTAL=0) ale BRAINSTORM_PAT match
if [ "$TOTAL" -eq 0 ] && [ "$BRN_HITS" -ge 1 ]; then
  PRIMARY="brainstorm"
  PRIMARY_HITS=$BRN_HITS
else
  PRIMARY="decision"
  PRIMARY_HITS=$DEC_HITS

  if [ "$RES_HITS" -gt "$PRIMARY_HITS" ]; then PRIMARY="research"; PRIMARY_HITS=$RES_HITS; fi
  if [ "$MOD_HITS" -gt "$PRIMARY_HITS" ]; then PRIMARY="modeling"; PRIMARY_HITS=$MOD_HITS; fi
  if [ "$WRT_HITS" -gt "$PRIMARY_HITS" ]; then PRIMARY="writing"; PRIMARY_HITS=$WRT_HITS; fi
  if [ "$VAL_HITS" -gt "$PRIMARY_HITS" ]; then PRIMARY="validation"; PRIMARY_HITS=$VAL_HITS; fi
  if [ "$SCR_HITS" -gt "$PRIMARY_HITS" ]; then PRIMARY="screening"; PRIMARY_HITS=$SCR_HITS; fi
fi

# ── Map intent to skill suggestions ──────────────────────────────────────────

case "$PRIMARY" in
  decision)
    SKILLS="**heart-orchestrate Pattern E** (3 cowork workers z różnymi personami pricing/growth/VP product, gemini-cli przez Bash) — judgment przez role-play divergence. Council CLI tylko z terminala (nie z CC session)."
    ;;
  research)
    SKILLS="**heart-orchestrate Pattern F** (3 workers, KAŻDY INNY LLM: Sonnet native + Gemini + Codex z `codex exec --skip-git-repo-check`) — fact verification przez cross-LLM divergence; wykrywa hallucinacje pojedynczego modelu. Lub samo **deep-research**/**market-research** dla single-source research, **exa-search** token-efficient, **chrome-devtools-mcp** dla multi-page browser."
    ;;
  modeling)
    SKILLS="**saas-metrics-coach** (CAC/LTV/payback/churn/unit econ) lub **financial-analyst** (P&L + 3-statement + DCF). Dla interpretacji wyników: heart-orchestrate Pattern E z personami (CFO/pricing analyst/VP product)."
    ;;
  writing)
    SKILLS="**board-prep** (IC memo), **heart-pitch-deck** (10-12 slide deck), **investor-materials** (one-pagery), **heart-stakeholder-update** (weekly/monthly update). Dla multi-section deliverables: heart-orchestrate Pattern E (1 persona per sekcja)."
    ;;
  validation)
    SKILLS="**product-discovery** (JTBD), **experiment-designer** (smoke test / fake door), **ux-researcher-designer** (interview plan + synthesis). Dla simulacji stakeholderów: heart-orchestrate Pattern E (różne user personas)."
    ;;
  screening)
    SKILLS="**deal-desk** (quick fit/no-fit), **heart-dd-checklist** (sector-aware DD), **heart-dd-prep** (one-page DD case dla IC). Dla founder fit assessment: heart-orchestrate Pattern E (VC partner + operator + skeptic personas)."
    ;;
  brainstorm)
    SKILLS="**brainstorming** — generic thinking partner dla non-VB tasków bez precyzyjnego kontekstu (organizacja eventu, struktura spotkania, ad-hoc decyzja personal/operacyjna, draft komunikacji). Flow: explore context → clarify questions one-at-a-time → propose 2-3 approaches → user approves → output. Po dialogu, jeśli scope się skrystalizował, transition do bardziej specyficznego skill (heart-orchestrate / board-prep / heart-pitch-deck etc.)."
    ;;
esac

# Pricing usually = decision + modeling
if [ "$PRI_HITS" -ge 1 ]; then
  SKILLS="$SKILLS Bonus: **pricing-strategist** + **heart-comps-analysis** dla benchmarków valuation."
fi

# Sector hint adds compliance/context reminder for Heart portfolio sectors.
# Dla nowych sektorów (nie ujętych poniżej) — persona alone wystarczy, Pattern E w heart-orchestrate.
SECTOR_NOTE=""
if [ "$SEC_HITS" -ge 1 ]; then
  if printf '%s' "$PROMPT" | grep -qiE 'HealthTech|MDR|NFZ|RODO art.?9|medycyn|klinicz|szpital|przychodni|klinika'; then
    SECTOR_NOTE=" ⚠️ HealthTech kontekst — załącz **heart-healthtech-compliance** (MDR, RODO art. 9, IRB approval, NFZ procurement)."
  elif printf '%s' "$PROMPT" | grep -qiE 'academic spinout|spin[- ]?out|tech transfer|uczelni|profesor|PAN|NCBR|NCN|IP commercializ'; then
    SECTOR_NOTE=" ⚠️ Academic spinout kontekst — załącz **heart-academic-spinouts** (IP ownership, NCBR/NCN funding paths, cooperation models z profesorami)."
  elif printf '%s' "$PROMPT" | grep -qiE 'energ(ia|etyk|ii)|magazyn(y)? energii|BESS|V2G|PSE|TSO|DSO|URE|TGE|fotowoltaik|PV|wiatr|offshore wind|nuclear|SMR|OZE|elektrolizer|wodór|H2|hydrogen|heat pump|pompa ciepła|ciepłownict|district heating|ładowarka|charging|CPO|EMSP|EU Battery|RED III|EPBD|EU ETS'; then
    SECTOR_NOTE=" ⚠️ Energy kontekst — załącz **heart-energy** (generation/OZE/nuclear, T&D PSE/DSO, storage/BESS, e-mobility, H2, heat & buildings, energy services SaaS; regulator stack RED III/Battery Reg/ETS/EPBD/CSRD, funding NFOŚiGW/NCBR/EU Innovation Fund)."
  elif printf '%s' "$PROMPT" | grep -qiE 'FinTech|KNF|AMLD|MIFID|PSD2|bank'; then
    SECTOR_NOTE=" ⚠️ FinTech kontekst — załącz **heart-fintech-compliance** (KNF, AMLD6, MIFID2, PSD2, RODO, DORA)."
  fi
fi

# ── Emit hint ────────────────────────────────────────────────────────────────

cat <<EOF
{
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "💡 [Venture Builder hook] User's prompt matches **${PRIMARY}** intent (decision:${DEC_HITS} research:${RES_HITS} modeling:${MOD_HITS} writing:${WRT_HITS} validation:${VAL_HITS} screening:${SCR_HITS} pricing:${PRI_HITS} sector:${SEC_HITS}). Suggested skill(s): ${SKILLS}${SECTOR_NOTE} BEFORE answering: briefly ask user in PLAIN BUSINESS LANGUAGE (NIE 'Pattern E/F' jargon). For decisions use 'konsultacja z 3 ekspertami (~60s)'. For research use 'cross-check przez 3 niezależne AI (~90s)'. Always offer choice: (a) tak (b) tylko Ty (c) sam wiem. Wait for explicit yes. Skip on simple lookups. Opt-out: prefix 'BEZ COUNCIL:'. Pełen pattern w skills/heart-custom/heart-orchestrate/SKILL.md (KROK -1 confirmation)."
  }
}
EOF
