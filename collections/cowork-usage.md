# Jak używać heart-vb w Claude Cowork (Desktop)

**TL;DR: nie musisz nic dodawać do każdego prompta.** Pisz normalnie — model sam widzi wszystkie skille i agentów heart-vb i dobiera właściwy. Ta instrukcja pokazuje 3 wzorce użycia od najprostszego do najbardziej "sterowanego".

---

## Najpierw — 3 środowiska Claude (gdzie co działa)

Łatwo się pogubić bo "Claude Code", "CLI" i "Cowork" brzmią podobnie. W rzeczywistości są **dwa silniki**:

| Środowisko | Co to | Silnik | Plugin heart-vb |
|---|---|---|---|
| **Claude Code — CLI** | `claude` w Terminalu | Claude Code | ✅ Pełny (hooki, agenci, skille, council CLI) |
| **Claude Code — IDE** | rozszerzenie w VSCode / Cursor | Claude Code (ten sam silnik co CLI) | ✅ Pełny (identycznie jak CLI) |
| **Claude Desktop — Cowork** | zakładka Cowork w aplikacji Claude Desktop | Claude Code, ale **w sandboxie** | ⚠️ Skille + agenci ✅, **bez auto-hooków** |
| ~~claude.ai (web)~~ | przeglądarka | — | ❌ Brak wsparcia pluginów w ogóle |

**Kluczowy wniosek:**
- **"Claude Code" = CLI + IDE** — ten sam silnik, te same możliwości, **pełne hooki**. To jest środowisko z największą funkcjonalnością (auto-suggest, cross-session memory, council CLI z terminala).
- **"Cowork" = osobna zakładka w Desktop** — używa silnika Claude Code, ale działa w sandboxie per-sesja. Z bezpieczeństwa **nie pozwala na plugin-shipped shell hooki**, więc heart-vb działa tam bez auto-suggest (ale skille i agenci w pełni).

### Co wybrać do czego

| Praca | Rekomendowane środowisko | Dlaczego |
|---|---|---|
| Długoterminowy projekt VB (tygodnie) | **Claude Code CLI/IDE** | Cross-session memory (si:*), pełne auto-hooki, council CLI |
| Szybkie zadanie / pojedyncza analiza | **Cowork** | Wygodny UI, mniej frykcji, dependencies dziedziczone z CLI |
| Pojedyncza decyzja (Pattern E/F) | Dowolne | Działa wszędzie gdzie plugin zainstalowany |
| Portfolio / cross-venture analiza | **Claude Code CLI** | Cross-session learnings, bi-weekly cadence |

> **Dependencies (gemini-cli, codex, council) instalujesz raz w Terminalu** — są system-level, więc Cowork je dziedziczy. Sam plugin (skille+agenci) instalujesz przez `/plugin install` w obu środowiskach niezależnie.

---

> **Kontekst techniczny (dlaczego Cowork bez hooków):** Cowork to autonomous-agent sandbox. Plugin **może shippować hooki i jest normalnie widoczny** (heart-vb shippuje SessionStart + PreCompact i instaluje się bez problemu) — ale Cowork **po prostu ich nie wykonuje** (cicho pomija plugin-shipped shell hooki, bo `.sh` odpalany autonomicznie to injection vector). CLI/IDE pozwala (user kontroluje terminal). Hooki w CLI robiły proaktywny "💡 użyj skilla X" przy każdym prompcie. W Cowork tego nudge'a nie ma — ale skille i agenci działają w pełni, bo model widzi ich opisy i sam je wywołuje. Różnica: musisz być odrobinę bardziej konkretny, jeśli model nie trafi za pierwszym razem.
>
> ⚠️ **Uwaga historyczna:** wcześniej myśleliśmy, że to hooki ukrywają plugin w Coworku. **Nieprawda** — przyczyną była kolizja nazw skilla (`status` zduplikowany), naprawiona w 0.8.10. Hooki nigdy nie ukrywały pluginu; po prostu się nie odpalają.

---

## Wzorzec 1 — Pisz naturalnie (domyślny, 90% przypadków)

Po prostu opisz zadanie. Model dopasuje skill/agenta z opisu.

| Co piszesz | Co się dzieje automatycznie |
|---|---|
| "Pomóż mi z napkin math dla HealthTech B2B SaaS sprzedawanego klinikom" | → skill `napkin-math` + sector context HealthTech |
| "Kto może kupić nasz BESS venture za 5-10 lat?" | → skill `exit-strategy` (M6) |
| "Porównaj 5 konkurentów na rynku AI-EHR" | → skill `competitive-teardown` lub agent `comps-analyst` |
| "Czy nasz pricing €99/€299 vs flat €2500 ma sens?" | → `pricing-analyst` + `cfo`, lub Pattern E (3 ekspertów) |
| "Sprawdź stan projektu / gdzie jesteśmy" | → `/heart-status` |

**Działa bez żadnego prefiksu.** Jak każdy normalny chat.

---

## Wzorzec 2 — Zacznij sesję od orkiestratora (NAJLEPSZE dla pracy nad projektem)

Jeśli pracujesz nad **konkretnym projektem VB przez dłuższą sesję**, zacznij od jednego zdania które ładuje cały framework DD by Heart. Potem przez resztę sesji model routuje wszystko poprawnie.

**Pierwszy prompt sesji (skopiuj):**
```
Pracuję nad projektem venture building [NAZWA] w [sektor: HealthTech / energetyka / academic spinout / FinTech].
Użyj heart-vb-process — przeprowadź mnie przez proces DD by Heart.
```

To uruchamia master orchestrator `heart-vb-process`, który:
- Ładuje świadomość 12 milestones (Discovery → Creation → Validation → Fundraising)
- Wie kiedy zaproponować assessment / kickoff / konkretny milestone
- Zachowuje briefing-style output (zwięzłe odpowiedzi, nie research dump)
- Pyta o zgodę zanim odpali kosztowny workflow (3 ekspertów / cross-check 3 AI)

Po tym jednym prompcie — reszta sesji "wie" o frameworku. Nie musisz powtarzać.

---

## Wzorzec 3 — Wywołaj konkretny skill/agenta wprost (gdy wiesz czego chcesz)

Slash command lub wprost po nazwie:

```
/heart-vb-process          → master orchestrator (cały framework)
/heart-status           → diagnostyka: co działa, jaki tier gotowości
```

Albo opisowo:
```
"Użyj skilla assessment — oceń nasz projekt przez 12 milestones"
"Spawn agenta cfo i pricing-analyst równolegle dla analizy pricingu"
"Uruchom exit-strategy dla naszego venture"
```

**Lista najważniejszych skilli do wywołania wprost:**

| Chcesz... | Skill / agent |
|---|---|
| Ocenić stan projektu (12 milestones) | `assessment` |
| Zaplanować sprinty + risk ranking | `kickoff` |
| Sprawdzić czy ekonomia się spina | `napkin-math` (M5) |
| Exit strategy + acquirers | `exit-strategy` (M6) |
| Cap table / equity split | `cap-table-helper` (M7) |
| Pitch deck narrative | `pitch-coach` agent / `heart-pitch-deck` skill |
| Model finansowy 3Y | `cfo` agent / `financial-analyst` skill |
| Stress-test VC | `vc-partner` agent |
| "Co może pójść źle" | `founder-skeptic` agent |
| Czy gotowi do fundraisingu | `fundraising-readiness` |

---

## Konsultacja zespołu ekspertów (Pattern E) w Cowork

Dla decyzji warto zebrać kilka perspektyw. W Cowork piszesz wprost:

```
"Mam decyzję: [opis]. Zbierz 3 perspektywy — pricing analyst, growth lead i founder-skeptic — i daj mi syntezę."
```

Model spawnuje 3 dedicated agents równolegle i syntetyzuje. To samo co stary auto-Pattern-E, tylko wywołane świadomie zamiast przez hook.

---

## Czego NIE ma w Cowork (vs CLI)

| Funkcja | CLI | Cowork |
|---|---|---|
| Skille (47) | ✅ | ✅ |
| Agenci (15) | ✅ | ✅ |
| Pattern E/F (multi-ekspert / multi-LLM) | ✅ | ✅ (wywołaj wprost) |
| DD by Heart framework | ✅ | ✅ (przez heart-vb-process) |
| Auto-suggest "💡 użyj skilla X" przy każdym prompcie | ✅ (hook) | ❌ — model routuje sam z opisów |
| Auto-consent gate przy każdej decyzji | ✅ (hook) | ⚠️ częściowo — wbudowane w skille gdy aktywne |
| PreCompact "zapisz learnings" | ✅ (hook) | ❌ — zapisuj ręcznie `/si:remember` |

**Bottom line:** w Cowork masz **pełną funkcjonalność**, tracisz tylko proaktywne podpowiedzi. Wzorzec 2 (start od orkiestratora) odzyskuje większość tej proaktywności na całą sesję jednym zdaniem.

---

## Potwierdzone empirycznie (2026-06-08)

Przetestowaliśmy realnie w Coworku (świeże sesje + analiza logu `~/Library/Logs/Claude/main.log`). Wnioski **potwierdzone**, nie teoretyczne:

| Co sprawdzaliśmy | Wynik |
|---|---|
| Prompt konkretny ("napkin math dla HealthTech RPM") | ✅ skill `napkin-math` załadowany natywnie (`elicitation … via=PreToolUse`), output framework-aware: M5 + sektor + routing milestone'ów |
| Prompt ogólnikowy ("czym możesz pomóc przy startupie?") | ✅ pełna mapa DD by Heart (12 milestones, 4 fazy) **bez ładowania żadnego skilla** — model zsyntetyzował z opisów w manifeście |
| SessionStart hook (`session-init.sh`) | ❌ **zero śladu w logu** — hook **nie odpala się w Coworku** (loguje się wszystko inne, więc to nie kwestia braku logowania) |

**Skąd więc świadomość frameworka w Coworku?** Z dwóch natywnych warstw — obu działających **bez hooka**:

1. **Opisy (description) 47 skilli + 15 agentów w manifeście** — zawsze widoczne modelowi → framework overview nawet na ogólnikowy prompt, nawet bez ładowania skilla.
2. **Treść skilla via PreToolUse elicitation** — gdy konkretne zadanie triggeruje → głęboka metodyka + consent (Krok 0) + routing do innych milestone'ów.

**Wniosek operacyjny: pracownik NIE odpala niczego ręcznie.** Pisze zadanie zwykłym językiem — Cowork sam dobiera skill i wciąga framework. Żadnej komendy `/`, żadnej inicjalizacji. Hook jest **martwy w Coworku, ale zbędny** (te dwie warstwy pokrywają wszystko, co miał robić). W CLI/IDE hook nadal działa jako bonus — zostawiamy go.

---

## Jak zaktualizować heart-vb w Cowork

**Update DZIAŁA — potrzebuje tylko czasu.** Cowork nie pobiera zmian w czasie rzeczywistym: po push do repo serwer Anthropic musi re-zindeksować marketplace (server-side, per konto). To zajmuje **~12-16 sekund** na sync + **cooldown 42s** między sync'ami.

**Normalna aktualizacja (zalecana):**
```
1. Directory → Plugins → tab "the-heart-marketplace" → Update
2. POCZEKAJ ~15-30 sekund (server re-scan repo)
3. Jeśli pokazuje "Already up to date" mimo nowej wersji → cooldown aktywny,
   odczekaj ~minutę i kliknij Update ponownie
```

**Forcing (gdy się spieszysz / Update uparcie pokazuje stare):**
```
tab "the-heart-marketplace" → ··· → Remove → dodaj ponownie → reinstall
```
Remove+re-add wymusza świeży re-scan, ale też podlega cooldownowi.

> **Ważne — dlaczego czasem "Already up to date" mimo że jest nowa wersja:** Cowork triggeruje sync server-side który (a) trwa kilkanaście sekund, (b) ma cooldown 42s, (c) pomija re-poll gdy panel otwierasz przy `already_connected`. To NIE jest zepsute — po prostu daj sekundy/minutę. Świeży push do repo nie jest widoczny natychmiast.

> **Dla zespołu w praktyce:** instalujesz **raz**, działa. Aktualizacje pluginu są rzadkie — gdy wyjdzie nowa wersja, kliknij Update i poczekaj chwilę. W CLI: `/plugin marketplace update` + `/plugin update heart-vb` (też ma latencję, ale mniejszą).

---

## Najprostsza rekomendacja dla pracownika

1. **Szybkie zadanie** → pisz naturalnie (Wzorzec 1)
2. **Praca nad projektem** → zacznij od *"użyj heart-vb-process dla projektu [X]"* (Wzorzec 2), potem normalnie
3. **Nie wiesz czy plugin działa** → `/heart-status`

Żadnego magicznego prefiksu przy każdym prompcie. Maksymalnie jedno zdanie na starcie sesji.
