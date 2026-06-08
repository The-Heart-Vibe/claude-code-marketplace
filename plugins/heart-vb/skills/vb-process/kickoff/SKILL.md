---
name: kickoff
description: "Krok 2 procesu VB — po assessment generuje harmonogram dla projektu. Risk ranking brakujących milestones, podział na sprinty 2-3 tygodniowe, capacity planning, OKR per milestone (Objective + Key Results). Output: timeline z przypisanymi sprintami i jasnym celem per sprint, max 2-3 streamy in progress jednocześnie. Use po assessment lub gdy projekt startuje od zera. Triggeruj na: \"kickoff\", \"harmonogram projektu\", \"sprint planning\", \"od czego zacząć\", \"rozpisz milestones na sprinty\"."
---

> 🔒 **heart-vb CORE — zawsze, niezależnie od załadowanego skilla:**
> (1) output = prosty polski, zero żargonu (pass/Voices/Pattern-F-internal) · (2) fakty do VC (TAM/multiple/exit/CAC-LTV/regulacje) → zaproponuj cross-check Pattern F zanim trafią do decka · (3) nowy milestone → **załaduj jego skill** (`/heart-vb:X`), nie improwizuj · (4) KROK -1 consent przed kosztownym spawnem · (5) taguj [Guessing] na niepewnych liczbach, nie udawaj cross-checku na jednym modelu.

# Krok 2 — Kickoff

Po assessment (lub przy projekcie od zera) — generuje **harmonogram operacyjny**: które milestones w jakim sprincie, kto co robi, jakie OKR.

## Kiedy fire

- Po assessment (Krok 1 wynik wskazał >3 missing milestones)
- Projekt startuje od zera (np. naukowiec z IP, brak business case'a)
- Reset / replan istniejącego projektu (np. po pivot)
- Wejście nowego menadżera na projekt — chce zobaczyć cały plan

## NIE jest to

- Substytut weryfikacji jakości (to robi assessment)
- Sztywny waterfall plan — to są guardrails, kolejność może się zmieniać
- Mikromanagement (5-6 tasków/tydzień to **menadżer decyduje**, plugin tylko milestone-level)

## Inputs które potrzebuję

1. **Assessment result** (preferred) — z poprzedniej sesji lub w bieżącej. Jeśli brak → spytaj user'a żeby uruchomił `/heart-vb:assessment` pierwsze.
2. **Capacity** — ile osób w zespole, ile godzin/tydzień per osoba (founder fulltime / menadżer 50% / analityk wsparcia)
3. **Constraint timeline** — czy jest deadline (np. "musimy zamknąć rundę do końca Q3")
4. **Domena projektu** — wpłynie na M10 (regulacje) i ewentualne sub-skille sectorowe

## Flow

### Krok 0 — Consent

> *"Mogę wygenerować pełen harmonogram kickoffu wg DD by Heart framework: risk ranking, podział na sprinty 2-3 tyg., capacity planning, OKR per milestone. ~5-10 min dialogu. Output: tabela tydzień-po-tygodniu z przypisanymi milestone'ami. (a) tak, jedźmy (b) tylko risk ranking, bez sprintów (c) sam wiem co dalej."*

### Krok 1 — Pull assessment

Jeśli w kontekście jest assessment result → użyj. Jeśli nie → spytaj:

> *"Czy zrobiłeś już assessment (12-row matrix per milestone)? Jeśli tak — wklej output albo opowiedz w skrócie co jest done, co missing. Jeśli nie — uruchom /heart-vb:assessment najpierw, to da nam baseline."*

### Krok 2 — Risk ranking (zasada #4 z dokumentu)

Posortuj missing/needs-review milestones wg dwóch wymiarów:

#### A. Deal-breaker risk

Co jest największym deal-breakerem? Jeśli to się nie spina → cała reszta bez sensu.

| Milestone | Typical deal-breaker risk |
|---|---|
| M5 Napkin math | **NAJCZĘSTSZY** — jeśli ekonomia się nie spina, project martwy. Lepiej wiedzieć po 2 tygodniach niż po 6 miesiącach |
| M1 Analiza rynku | Jeśli rynek za mały lub nie rośnie — VC nie zainteresowani |
| M3 Walidacja z inwestorami | Reality check — jeśli 3 inwestorów z networku mówi "zapomnijcie" → reset całego pomysłu |
| M2 Konkurencja | Jeśli brak defensible advantage → fundraising trudny |
| M4 Walidacja problemu | Jeśli klienci nie potwierdzają bólu → zła hipoteza |
| M7 Zespół & cap table | Brak CEO → nie zbierzecie pieniędzy. Złe equity split → equity drama later |
| M6 Exit strategy | Bez exit narrative → pierwsza rozmowa z VC nieudana |

#### B. Trudność / czas

Jak długo zajmie? (estymaty z dokumentu firmy)

| Time bucket | Milestones | Implication |
|---|---|---|
| **3-5 dni** | M5 napkin math, M6 exit strategy | Quick wins — zrób od razu |
| **1-2 tygodnie** | M1 market, M2 competition, M3 investors, M7 cap table, M12 investor list | Standard sprint |
| **2-4 tygodnie** | M4 customer problem, M9 solution validation, M11 materials | Wymaga external touch (rozmowy, iteracje) |
| **4-12 tygodni** | M8 MVP | Zwykle longest pole — paralelizuj inne milestones |
| **Variable** | M10 IP/regulacje | Depends on sector — może być 1 tydzień (FinTech advisor) albo 3 lata (FDA) |

#### Output Risk Ranking

```
RISK-RANKED PRIORITY:

🔴 CRITICAL (zacznij teraz):
  - M<N>: <milestone> — <why critical>
  
🟠 HIGH (sprint 2-3):
  - M<N>: <milestone> — <why high>
  
🟡 MEDIUM (sprint 4+):
  - M<N>: <milestone>

🟢 PARALEL (side-activity od dnia 1):
  - M12 Lista inwestorów — buduje się sukcesywnie
  - M3 Early signal z inwestorami — zacznij tydzień 1-2
```

### Krok 3 — Sprint planning

Zasada z dokumentu:
- **Sprinty 2-3 tygodnie**
- **5-6 tasków/tydzień per osoba**
- **Żaden task >1 miesiąc**
- **Max 2-3 streamy in progress jednocześnie**

Generuj harmonogram bazowany na przykładzie z dokumentu firmy:

```
HARMONOGRAM (~20 tygodni dla projektu od zera, paralelizowany)

TYDZIEŃ | FOCUS 1                    | FOCUS 2                  | FOCUS 3                | SIDE ACTIVITY
1-2     | M1 Analiza rynku           | M2 Analiza konkurencji   | M5 Napkin math         | M3 Pierwsze rozmowy z inwestorami
3-4     | M4 Walidacja problemu      | M6 Exit strategy         | —                      | M12 Budowanie listy inwestorów
5-8     | M4 (cd.)                   | M7 Zespół & cap table    | M8 MVP / prototyp      | Bi-weekly summary #1
9-12    | M8 (cd.)                   | M9 Walidacja rozwiązania | —                      | Bi-weekly summary #2, #3
13-16   | M9 (cd.)                   | M10 IP/regulacje         | M11 Materiały fundr.   | Bi-weekly summary #4
17-20   | M11 (iteracja)             | M12 Outreach — GO!       | —                      | Spotkanie z zarządem → start
```

**Adjust** to:
- Capacity user'a (jeśli 1-osobowy zespół → mniej paralelizacji)
- Already-done milestones (jeśli M1+M2 ✓ → start od M3-M5)
- Domain specifics (M10 może być longer dla MedTech/BioTech)

### Krok 4 — OKR per milestone

Per każdy critical milestone z risk ranking — wygeneruj **Objective + Key Results**:

```
M5 — Napkin Math
Objective: Wiemy czy projekt się spina ekonomicznie, na poziomie 1-strony.
Key Results:
  KR1: Revenue model zidentyfikowany (1-N źródeł)
  KR2: Unit economics policzone: COGS, CAC, LTV szacunkowe
  KR3: Break-even policzony (months / # klientów do break-even)
  KR4: Go/no-go decision podjęta + udokumentowana
Deliverable: 1-stronicowy napkin doc
Estymacja: 3-5 dni
Owner: <manager>
```

Powtórz dla każdego z TOP 3 priorytetów.

### Krok 5 — Capacity check

> *"Capacity check: czy sam dasz radę te 3 milestones w 2-3 tygodniach (5-6 tasków/tydzień), czy potrzebujesz: (a) analityka do M1/M2 (b) designera do M8 (c) regulatory advisora do M10 (d) niczego — sam zrobię?"*

**Output** mention'a o capacity gap'ach:

```
Capacity:
  - M1+M2 (rynek+konkurencja) w paraleli → wymaga 2 osób tydz. 1-2 (lub jednej osoby 4 tyg.)
  - M8 MVP → wymaga dev/designera 4-12 tyg.
  - M10 (jeśli MedTech) → regulatory advisor zewnętrzny
  - Reszta → menadżer sam ogarnia
```

### Krok 6 — Final kickoff doc

Wygeneruj **1-page kickoff doc** z całym powyższym (risk ranking + harmonogram + OKR + capacity + next-steps). Spytaj user'a:

> *"Zapisać do `docs/projekty/<projekt>/kickoff-YYYY-MM-DD.md` żeby zachować baseline? (a) tak (b) inline w czacie (c) wyślij w Notion (jeśli connector aktywny)."*

## Output template

```
🚀 Kickoff Plan — <Projekt>

Faza startowa: <faza> · Domena: <D> · Capacity: <X osób, Y godz./tydz.>
Target horyzont fundraisingu: <X miesięcy>

═══════════════════════════════════════════════
RISK-RANKED PRIORITY (od czego zaczynamy)
═══════════════════════════════════════════════

🔴 Krytyczne:
  M<N>: <milestone> → <skill>
  Why: <konkret>
  Estymacja: <X tyg.>
  OKR: Obj=<X> · KR1=<X> · KR2=<X>

🟠 Wysokie: ...
🟡 Średnie: ...

═══════════════════════════════════════════════
SPRINT HARMONOGRAM (2-3 tyg. każdy)
═══════════════════════════════════════════════
[tabela z tygodniami, focus 1/2/3, side activity]

═══════════════════════════════════════════════
CAPACITY
═══════════════════════════════════════════════
- Menadżer (manager): X tasków/tydz., owner of M_, M_
- Analityk (jeśli potrzebny): owner of M_
- Designer/dev (jeśli potrzebny dla M8): X tygodni
- External (regulatory, M10): TBD

═══════════════════════════════════════════════
SIDE ACTIVITIES (od dnia 1, ciągłe)
═══════════════════════════════════════════════
- M12 lista inwestorów — buduj sukcesywnie
- Bi-weekly summary (Krok 3 z procesu) — co 2 tyg.

═══════════════════════════════════════════════
NEXT STEPS
═══════════════════════════════════════════════
1. Setup Notion (Warstwa 1 Project Card + Warstwa 2 Streams + Warstwa 3 Sprint Kanban)
2. Tydzień 1: kick-off rozmowa z founderem, ustal owner per milestone
3. Tydzień 1-2: zacznij od <CRITICAL milestone> → uruchom <skill>
4. Co 2 tyg.: bi-weekly summary do CC zarządu
```

## Anti-patterns

| Anti-pattern | Co zrobić zamiast |
|---|---|
| 100 mikro-tasków na kickoff | **Grube klocki, zasada #1** — milestone-level, nie task-level. Menadżer decyduje o granularności w Warstwie 3 Kanban |
| Wszystkie 12 milestones in progress naraz | **Max 2-3 streamy in progress** — focus, nie parallel chaos |
| Ignorowanie risk ranking, "zacznijmy od najłatwiejszych" | **Zasada #4 — zacznij od największego ryzyka**. Łatwe nie znaczy ważne |
| 20-tygodniowy plan bez milestone'ów paralelnych | Dokument firmy explicit shows paralelizację (M1+M2+M5 razem w tyg. 1-2). Zalecaj paralelizm gdzie capacity pozwala |
| Pomijanie M12 (lista inwestorów) na koniec | **Side activity od dnia 1** — lista buduje się ciągle, nie jest "ostatnim taskiem" |
| Sprint > 3 tygodnie | Hard cap. Jeśli milestone >3 tyg. (np. M8 MVP 4-12 tyg.) → rozbij na sub-sprinty |
