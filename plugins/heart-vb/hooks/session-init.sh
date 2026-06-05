#!/usr/bin/env bash
# SessionStart hook — one-shot context injection przy starcie sesji Claude Code/Cowork.
# Daje modelowi świadomość heart-vb frameworka bez per-prompt UserPromptSubmit hooków
# (które Cowork blokuje). Restored v0.8.12 po fixie kolizji nazw (0.8.10).
#
# Auto-loaded przez hooks/hooks.json. Działa w Claude Code CLI/IDE i Claude Desktop Cowork.

set -euo pipefail

cat <<'EOF'
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "🧰 [heart-vb plugin] Venture Builder toolkit aktywny. Framework: DD by Heart (12 milestones w 4 fazach: Discovery M1-M5 / Creation M6-M8 / Validation M9-M10 / Fundraising M11-M12). === ROUTING (auto-detect z user prompta) === decision/'co wybrać'/'vs' → heart-orchestrate Pattern E (3 personas) lub spawn agentów vc-partner+pricing-analyst+founder-skeptic; research/facts/regulacja → Pattern F (3 LLMs) lub regulatory-officer-pl agent; modeling/CAC/LTV/DCF → financial-analyst skill lub cfo+pricing-analyst agenci; writing/IC memo/deck → board-prep/heart-pitch-deck skille lub pitch-coach agent; validation/JTBD/interview → product-discovery/experiment-designer lub customer-research-lead agent; screening/founder fit → deal-desk + heart-dd-checklist lub vc-partner agent. === SECTOR (załącz przy detection) === HealthTech/MedTech → heart-healthtech-compliance + regulatory-officer-pl; academic spinout → heart-academic-spinouts; energy/OZE/BESS → heart-energy; FinTech → heart-fintech-compliance. === MILESTONE === TAM/SAM/SOM → M1 market-research; konkurenci → M2 competitive-teardown + comps-analyst; napkin math → M5 vb-process/napkin-math + cfo; exit/acquirers → M6 exit-strategy + comps-analyst; LOI/pilot → M9 pricing-strategist + customer-research-lead. === MASTER ENTRY === /heart-vb-process dla całego procesu, /heart-status dla diagnostyki. === KROK -1 CONSENT === przed odpaleniem skilla/agenta spytaj plain language: 'To wygląda na [intent] — proponuję [X]. (a) tak (b) inline (c) sam wiem.' Skip dla trivial lookups. Opt-out: 'BEZ PYTANIA:'. === BRIEFING STYLE === outputy max ~150-300 słów. Framework: skills/heart-custom/heart-vb-process/SKILL.md."
  }
}
EOF
