#!/usr/bin/env bash
# PreCompact hook — fire przed automatyczną kompresją kontekstu (~70-80% limitu).
# Pyta usera czy zachować key learnings przez /si:remember zanim context zniknie.
# Restored v0.8.12 po fixie kolizji nazw (0.8.10).
#
# Auto-loaded przez hooks/hooks.json. Działa w CLI i Cowork.

set -euo pipefail

cat <<'EOF'
{
  "hookSpecificOutput": {
    "hookEventName": "PreCompact",
    "additionalContext": "🧠 [heart-vb] Sesja zbliża się do kompresji kontekstu. PRZED kompresją spytaj usera plain language: 'Sesja zbliża się do automatycznej kompresji. Chcesz żebym zachował key learnings (nowy pattern, decyzję strategiczną, insight z rozmowy z klientem)? Mogę użyć /si:remember. (a) tak, podpowiedz co warto (b) nie (c) sam dam 1 zdanie what we learned'. One-shot — nie pytaj ponownie w tej sesji. Uwaga Cowork: si: memory jest per-session sandbox; dla cross-session learnings użyj CLI lub przeklej do trwałych docs."
  }
}
EOF
