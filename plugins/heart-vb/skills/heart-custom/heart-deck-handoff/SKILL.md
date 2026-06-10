---
name: heart-deck-handoff
description: "Pakuje GOTOWĄ treść decka (z heart-pitch-deck / board-prep / stakeholder-update / IC memo) w paste-ready brief dla Claude Design, który renderuje wizualny deck (React+Tailwind, 16:9) używając design systemu The Heart. Most content→visual — NIE generuje sam slajdów. Use gdy treść gotowa i user chce ją wizualnie złożyć. Triggeruj na: 'zróbmy z tego slajdy', 'handoff do Claude Design', 'wrzućmy outline w deck', 'gotowy outline co dalej', 'turn this into a deck', 'make these into slides'. NIE fire gdy treść dopiero powstaje albo user pyta CO napisać na slajdzie."
---

> 🔒 **heart-vb CORE — zawsze, niezależnie od załadowanego skilla:**
> (1) output = prosty polski, zero żargonu (pass/Voices/Pattern-F-internal) · (2) fakty do VC (TAM/multiple/exit/CAC-LTV/regulacje) → zaproponuj cross-check Pattern F zanim trafią do decka · (3) zmiana zadania lub milestone → **załaduj właściwy skill** (`/heart-vb:X`), nie improwizuj · (4) KROK -1 consent przed kosztownym spawnem · (5) taguj [Guessing] na niepewnych liczbach, nie udawaj cross-checku na jednym modelu.

# Heart Deck Handoff

Bierze **gotową treść** decka i przekształca ją w **brief paste-ready dla Claude Design**. Most między fazą THINKING (struktura/treść/dane/narracja — robi heart-pitch-deck / board-prep / stakeholder-update) a fazą VISUAL (polished slajdy renderowane przez Claude Design w trybie artifacts, na bazie design systemu The Heart).

**Ten skill NIE generuje slajdów ani .pptx.** Produkuje strukturalny brief, który człowiek wkleja do Claude Design. Podział pracy: heart-vb = myślenie (jego mocna strona z milestone'ów); Claude Design = wizualna egzekucja (jego mocna strona). Świadomie NIE rywalizujemy z Claude Design na wizualizacji.

## Kiedy fire'uje (detekcja)

Wyzwalaj **TYLKO** gdy oba warunki spełnione:
1. **Jest gotowa treść na deck** w rozmowie (pitch-deck outline, board narrative, stakeholder-update, IC memo, model/traction z M11).
2. **User sygnalizuje przejście do warstwy wizualnej** — nie samo słowo "prezentacja".

**Trigger-frazy** — PL: "treść decka gotowa", "zróbmy z tego slajdy", "trzeba to ładnie złożyć/zaprojektować", "handoff do Claude Design", "wrzućmy outline w deck", "kto to wyklika", "gotowy outline, co dalej". EN: "turn this into a deck", "ready to design the slides", "hand off to Claude Design", "make these into slides".

**NIE wyzwalaj gdy:** treść dopiero powstaje (outline niekompletny) · user pyta CO napisać na slajdzie (to robi heart-pitch-deck) · user już raz odmówił handoffu w tej rozmowie.

## KROK -1 — Consent prompt

Gdy detekcja zadziała, zapytaj jednym zdaniem, plain polski:

> *"Wygląda że masz już gotową treść na deck — chcesz żebym przygotował handoff do Claude Design (slajd-po-slajdzie + brand + który pattern użyć)? (a) tak, zrób handoff (b) nie, zostań przy treści."*

Po "tak" → wypełnij template danymi z rozmowy. Pól których nie znasz **nie wymyślaj** — zostaw `<…>` / `[TBD]`, taguj [Guessing] jeśli cokolwiek zgadujesz.

## Design system The Heart (Claude Design importuje to repo)

Handoff zakłada że Claude Design użyje brandowego design systemu — gotowe slide patterns + tokeny + widgety:

**Repo:** `https://github.com/The-Heart-Vibe/theheart-design-system` (w Claude Design: `setup → design-system → repo URL`)

**Gotowe slide patterns** (`src/patterns/`): `Cover`, `SectionDivider`, `Problem3Col`, `ValueProp`, `CompetitiveMatrix`, `Roadmap`, `SWOTGrid`, `OKRBoard`, `BigQuote`, `BeforeAfter`, `CustomerJourney`, `WeeklyStatus` — wszystkie owinięte w `SlideShell` (auto: czerwony footer, page number, eyebrow, lewy pasek — NIE duplikuj chrome).
**Widgety** (`src/components/`): `KPITile`, `BigStat`, `PersonCard`, `StatusPill`, `Badge`, `BulletList`, `Symbol`, `Logo`, `Icon`, `TimelineEvent`, `ComparisonRow`.

**Brand rules (twarde, łatwo złamać):**
- Czerwony **#E61B25** (`th-primary`) dominuje: headline'y, paski, kluczowe akcenty.
- Niebieski **#0056A4** RZADKO ("accent if needed") — **NIGDY na statusy**.
- Status palette fixed: done→zielony #13A538 · **in_progress→CZARNY #000000** (nie niebieski!) · at_risk→#E9787E · blocked→czerwony · planned→szary.
- Font **Raleway** (heading SemiBold / body / Light), Arial tylko fallback. Duże numerały dla danych.
- **NIGDY nie hardcode'uj hex** — używaj tokenów `--th-*` / Tailwind (`bg-th-primary`, `text-th-h1`, `font-heading`).

## Mapowanie treści VB → pattern

| Slajd | Pattern / widget |
|---|---|
| Cover | `Cover` |
| Problem (M4) | `Problem3Col` lub `BigQuote` (cytat z research) |
| Solution / value prop | `ValueProp` |
| Konkurencja (M2) | `CompetitiveMatrix` |
| Market / Traction (M1/M9) | content + `KPITile` / `BigStat` |
| Roadmap / milestones (M8) | `Roadmap` |
| Team (M7) | `PersonCard` grid |
| Exit / analiza (M6) | `SWOTGrid` |
| OKR / board | `OKRBoard` |
| Stakeholder / sprint status | `WeeklyStatus` + `StatusPill` |
| Transformacja / before-after | `BeforeAfter` · journey → `CustomerJourney` |
| Mocny cytat / testimonial | `BigQuote` |

## Handoff template (kanoniczny blok — output skilla)

Wypełnij każde `<…>`; usuń niewykorzystane slajdy. Analityk wkleja cały ten blok do Claude Design.

````text
# DECK BRIEF — Claude Design (The Heart)

## Setup
- W Claude Design: setup → design-system → repo:
  https://github.com/The-Heart-Vibe/theheart-design-system
- Użyj jego patterns (src/patterns/*), widgetów (src/components/*), SlideShell i tokenów --th-*. NIGDY nie hardcode'uj hex.

## Brand rules (twarde)
- #E61B25 (th-primary) dominuje; #0056A4 rzadko, NIGDY na statusy.
- Status: done→zielony · in_progress→CZARNY · at_risk→#E9787E · blocked→czerwony · planned→szary.
- Font Raleway (SemiBold/regular/Light). Duże numerały dla danych.

## Goal & Context
- Decyzja którą deck napędza: <np. approve €500k seed>
- Audience: <IC The Heart / VC / board / partner> — sophistication: <IC-grade>
- Jedno zdanie takeaway: <…>
- Format: 16:9 (1280×720), React+Tailwind, 1 komponent = 1 slajd, wrap w SlideShell.

## Per-slide spec
### Slide 1 — <Title>
- Pattern: <Cover | ValueProp | CompetitiveMatrix | Roadmap | SWOTGrid | OKRBoard | Problem3Col | BigQuote | BeforeAfter | CustomerJourney | WeeklyStatus | content+KPITile/BigStat>
- Headline: <≤8 słów — teza, nie temat>
- Body: <2-4 bullety, fragmenty>
- Key data: <dokładne liczby + jednostki + źródło>
- Widgets: <KPITile / BigStat / PersonCard / StatusPill / Badge / Symbol — jeśli pasują>
- Emphasis: <jedna liczba/słowo do wyróżnienia>

<powtórz per slide — celuj 8–14 slajdów>

## Constraints
- Bez text-walls (≤6 bulletów, ≤8 słów); jedna myśl/slajd; headline = wniosek.
- Bez wymyślania danych — tylko liczby wyżej; luki = [TBD].
- Charts: bez 3D/dual-axis, label directly, jeden insight/chart.
- Tokeny th-*, nie hex; spójny spacing/radius/shadow; kontrast czytelny na sali.

## Instrukcja (wklej razem z briefem)
"Zbuduj polished React+Tailwind 16:9 deck używając mojego design systemu (repo wyżej):
jeden komponent/slajd, mapuj slajdy na wskazane patterns, użyj moich danych verbatim,
zero wymyślania liczb — spytaj zanim cokolwiek dopiszesz. Wyrenderuj wszystkie slajdy."
````

## Instrukcja dla analityka (po wygenerowaniu briefu)

1. Skopiuj cały blok `DECK BRIEF`.
2. W **Claude Design** najpierw podłącz design system (`setup → design-system → repo URL`), potem wklej brief.
3. Dodaj brakujące assety (logo, zdjęcia zespołu) jeśli template ich nie miał.
4. Iteruj w Claude Design **tylko nad wizualem** — nie re-litiguj treści tutaj (treść ustalona upstream w heart-pitch-deck / board-prep).

## Anti-patterns (NIE rób tego)

| Anti-pattern | Zamiast |
|---|---|
| Generowanie slajdów / .pptx samodzielnie | Produkujesz BRIEF; egzekucję wizualną robi Claude Design |
| Handoff przy niekompletnej treści | Najpierw dokończ outline (heart-pitch-deck), potem handoff |
| Wymyślanie liczb/brandu żeby wypełnić template | Zostaw `[TBD]`, taguj [Guessing], spytaj usera |
| Re-litygacja treści w briefie | Brief pakuje to co JUŻ ustalone; zmiana treści = wróć do source skilla |
| Spamowanie sugestią | Jedna propozycja per gotowy artefakt; odmowa = cisza |
| Hardcode hex / niebieski na status | Tokeny th-*; status palette fixed (in_progress = czarny) |

## Alternatywa — branded .pptx

Jeśli user chce **sztywny branded .pptx** zamiast generative decka: osobna ścieżka przez plugin `pptx-generator` (python-pptx renderer, predefiniowane layouty). Świadomy wybór: **Claude Design = generative HTML/React deck (lepszy wizualnie)** · pptx-generator = sztywny .pptx gdy ktoś musi mieć plik PowerPoint.

## Connection — gdzie leży w pipeline

Wszystkie poniższe produkują **treść**. `heart-deck-handoff` jest **downstream** (po nich) i pakuje treść do formatu dla Claude Design. Brak overlapu — one robią CO napisać, on robi most do wizualizacji.

- **`heart-pitch-deck`** — gotowy outline → handoff pakuje go w brief wizualny.
- **`vb-comms/board-prep`** — gotowy deck/narrative pre-read → handoff dla wizualizacji.
- **`vb-comms/investor-materials`** — wizualny deck przez Claude Design (alternatywa dla `frontend-slides`).
- **`heart-stakeholder-update`** — gdy update ma trafić jako slajdy (board deck) → handoff.
- **`heart-vb-process` M11** — krok po heart-pitch-deck: content → handoff → wizualny deck.
