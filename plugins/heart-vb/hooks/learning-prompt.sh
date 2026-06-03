#!/usr/bin/env bash
# PreCompact hook — fire'uje przed automatic context compaction (~70-80% context limit).
# Cel: zapytać usera czy chce zachować key learnings z sesji przez /si:remember
# ZANIM context zostanie skompresowany (i potencjalnie zgubione insighty).
#
# Auto-loaded od v0.7.3 przez hooks/hooks.json w pluginie.
# Disable globally: /plugin uninstall heart-vb lub edit hooks/hooks.json w plugin dir.
# Override per-prompt (NIE per session — to PreCompact hook): NA — hook jest passive prompt,
# Claude decyduje czy zadać pytanie user'owi.

set -euo pipefail

# Input: PreCompact hook dostaje JSON z polami session_id, transcript_path (jeśli dostępne).
# Nie potrzebujemy parsować — output jest static instruction dla Claude.

cat <<EOF
{
  "hookSpecificOutput": {
    "hookEventName": "PreCompact",
    "additionalContext": "🧠 [Learning Prompt — heart-vb] Sesja zbliża się do compaction (Claude Code/Cowork wkrótce skompresuje wcześniejsze wiadomości). To dobry moment żeby zachować kluczowe learnings ZANIM zostaną stracone. PRZED kompresją: spytaj user'a w PLAIN LANGUAGE (1-2 zdania): 'Sesja zbliża się do automatycznej kompresji kontekstu. Czy chcesz żebym zachował w pamięci jakieś key learnings z tej sesji (np. nowy pattern który znalazłeś, decyzję strategiczną, ważny insight z rozmowy z klientem)? Mogę użyć /si:remember żeby je zapisać do MEMORY.md zanim context zostanie skompresowany. (a) tak, podpowiedz mi co warto zapisać (b) nie, idziemy dalej (c) sam zdecyduję — daj mi 1 zdanie what we learned w tej sesji'. WAŻNE: w Cowork (Claude Desktop tab) memory jest per-session sandbox — si:remember zapisze do bieżącego session sandboxa, NIE cross-session global. Dla cross-session learning user musi używać Claude Code CLI lub manualnie kopiować do persistent location. To one-shot prompt — NIE pytaj o consent ponownie w tej sesji."
  }
}
EOF
