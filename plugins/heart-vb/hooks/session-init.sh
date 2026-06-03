#!/usr/bin/env bash
# SessionStart hook — one-shot context injection przy starcie sesji Claude Code/Cowork.
# Zastępuje 4 UserPromptSubmit hooks (vb-suggest, devtools-suggest, cowork-suggest, model-route)
# z wersji 0.6.10-0.8.4 — Cowork UI odrzuca pluginy z UserPromptSubmit jako security policy
# (prompt injection vector).
#
# Trade-off: zamiast per-prompt auto-suggest, dajemy Claude'owi one-shot świadomość:
# - jakie skille/agents są dostępne w heart-vb
# - DD by Heart framework (12 milestones, 4 fazy)
# - Pattern E/F dla decyzji
# - Plain language consent gate (KROK -1) przed odpalaniem workflow
#
# Auto-loaded od v0.8.5 przez hooks/hooks.json. Działa w Claude Code CLI + Claude Desktop Cowork.

set -euo pipefail

cat <<'EOF'
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "🧰 [heart-vb plugin loaded] Venture Builder toolkit aktywny. Framework: DD by Heart (12 non-negotiable milestones w 4 fazach: Discovery M1-M5 / Creation M6-M8 / Validation M9-M10 / Fundraising M11-M12). === ROUTING (auto-detect z user prompta) === decision/'co wybrać'/'vs' → heart-orchestrate Pattern E (3 personas debate) lub spawn 3 dedicated agents (vc-partner+pricing-analyst+founder-skeptic); research/facts/regulacja → Pattern F (3 LLMs verification) lub regulatory-officer-pl agent (Pattern F built-in); modeling/CAC/LTV/DCF → financial-analyst skill lub cfo agent + pricing-analyst; writing/IC memo/deck → board-prep/heart-pitch-deck skille lub pitch-coach agent; validation/JTBD/interview → product-discovery/experiment-designer skille lub customer-research-lead agent; screening/fit/founder → deal-desk + heart-dd-checklist lub vc-partner agent. === SECTOR CONTEXT (załącz przy detection) === HealthTech/MedTech → heart-healthtech-compliance + regulatory-officer-pl agent; academic spinout → heart-academic-spinouts; energy/OZE/BESS → heart-energy; FinTech → heart-fintech-compliance. === MILESTONE-SPECIFIC === TAM/SAM/SOM → M1 market-research; konkurenci → M2 competitive-teardown + comps-analyst agent; napkin math → M5 vb-process/napkin-math + cfo agent; exit/acquirers → M6 vb-process/exit-strategy + comps-analyst; LOI/pilot → M9 pricing-strategist + customer-research-lead. === KROK -1 CONSENT GATE === BEFORE invoking ANY skill or spawning ANY agent ask user PLAIN LANGUAGE (NIE 'Pattern E/F' jargon, NIE 'M5' kodu — używaj nazwy 'napkin math'): 'To wygląda na [intent w plain] — proponuję [skill X / dialog / 3 ekspertów]. (a) tak (b) odpowiedz inline bez skill (c) sam wiem co chcę.' Wait for explicit yes. Skip consent ONLY na: trivial lookups (haiku tier), single Read/Bash, slash commands. Opt-out per prompt: prefix 'BEZ PYTANIA:' (skip consent), 'BEZ COUNCIL:' (skip skill suggestion), 'BEZ COWORK:' (skip agent spawn). === BRIEFING-STYLE SYNTHESIS === Wszystkie outputs max ~150-300 słów (briefing, NIE research dump). Każdy claim ma source. Pełen framework: skills/heart-custom/heart-vb-process/SKILL.md."
  }
}
EOF
