---
name: fundraising-readiness
description: "Krok 4 procesu VB — regularny check \"czy już możemy iść z tym do inwestorów?\". To NIE jest assessment (Krok 1 — pełny 12-milestone checker), tylko go/no-go gate decision oparty o weighted scoring najważniejszych milestones. Z dokumentu firmy \"nie czekaj na 12/12 — czasami 8/12 wystarczy, a IP dopracujesz po term sheet\". Triggeruj na: \"fundraising readiness\", \"czy idziemy do inwestorów\", \"ready do VC\", \"minimum viable fundraising\", \"stempel The Heart\"."
---

> 🔒 **heart-vb CORE — zawsze, niezależnie od załadowanego skilla:**
> (1) output = prosty polski, zero żargonu (pass/Voices/Pattern-F-internal) · (2) fakty do VC (TAM/multiple/exit/CAC-LTV/regulacje) → zaproponuj cross-check Pattern F zanim trafią do decka · (3) zmiana zadania lub milestone → **załaduj właściwy skill** (`/heart-vb:X`), nie improwizuj · (4) KROK -1 consent przed kosztownym spawnem · (5) taguj [Guessing] na niepewnych liczbach, nie udawaj cross-checku na jednym modelu.

# Fundraising Readiness Check (Krok 4)

Cel: regularny **go/no-go gate** czy projekt jest gotowy żeby rozpocząć M12 outreach do inwestorów. NIE czekamy na perfekcyjne 12/12 — celujemy w **minimum viable fundraising state**, zwykle 8-10/12 z konkretnymi milestones jako absolute requirements.

## Filozofia (z dokumentu firmy)

> *"Regularnie sprawdzasz: 'czy już możemy z tym iść do inwestorów?' Nie czekaj na 12/12 — czasami 8/12 wystarczy, a IP dopracujesz po term sheet. Zawsze idziemy do inwestorów jak najszybciej — zbieramy feedback i iterujemy."*

Implikacje:
- Niektóre milestones są **must-have** (np. M5 napkin math, M7 cap table, M11 materiały)
- Inne są **nice-to-have / post-term-sheet** (np. M10 IP — depends on sector)
- "Going early" zbiera feedback od VC który dopracowuje narrative → faster final close

## Kiedy fire

- Cyklicznie w trakcie projektu (np. co miesiąc lub po każdym major milestone)
- Po assessment (Krok 1) — gdy ktoś pyta "czy już możemy iść"
- Gdy menadżer myśli że jesteśmy gotowi, ale chce drugiej opinii
- Przed strategicznym spotkaniem z zarządem (Maciek/Jędrzej — Krok 4 z dokumentu)
- Gdy konkurent zebrał rundę i pressure na timing rośnie

## NIE jest to

- **Full assessment** (Krok 1 — 12-row matrix) — to robi `vb-process/assessment`
- **Kickoff replan** — to robi `vb-process/kickoff`
- **Pitch coaching** — to deck content, nie readiness gate
- **Term sheet review** — to legal/financial po term sheet od VC

## Flow

### Krok 0 — Consent

> *"Mogę zrobić fundraising readiness check — weighted go/no-go ocena czy projekt jest gotowy iść do inwestorów. ~10 min dialogu. Output: verdict (GO / GO with caveats / NOT YET), z konkretnym powodem i action items na ostatnie tygodnie przed outreachem. (a) tak (b) tylko quick check 3 najważniejszych milestones (c) sam ocenię, daj checklistę."*

### Krok 1 — Pull stan milestones (input)

Spytaj user'a o status (lub use output z poprzedniego `/heart-vb:assessment`):

```
Quick status check:
M1 Analiza rynku            — ✓/◐/☐
M2 Analiza konkurencji      — ✓/◐/☐
M3 Walidacja inwestorska    — ✓/◐/☐
M4 Walidacja problemu       — ✓/◐/☐
M5 Napkin math              — ✓/◐/☐
M6 Exit strategy            — ✓/◐/☐
M7 Zespół & cap table       — ✓/◐/☐
M8 MVP / produkt            — ✓/◐/☐
M9 Walidacja rozwiązania    — ✓/◐/☐
M10 IP/regulacje            — ✓/◐/☐ / N/A
M11 Materiały fundr.        — ✓/◐/☐
M12 Lista inwestorów        — ✓/◐/☐

Faza projektu: <faza>
Stage rundy planowanej: <pre-seed/seed/Series A>
Branża: <D>
```

### Krok 2 — Weighted scoring (per milestone vs stage)

Nie wszystkie milestones są równe. **Weight zależy od:**
- **Stage rundy** (pre-seed wybacza brakujące M8 MVP, Series A nie)
- **Branża** (HealthTech/MedTech wymaga mocniejszego M10, SaaS B2B nie)

#### Pre-seed readiness (target ~€500k - €2M)

| Milestone | Weight | Reason |
|---|---|---|
| M1 Analiza rynku | 🟡 Medium | Need solid narrative, ale full bottom-up TAM nie jest blocker |
| M2 Analiza konkurencji | 🟡 Medium | "Kto" wystarczy, deep teardown nie konieczny |
| M3 Walidacja z inwestorami | 🟢 High | Pre-seed = relationship plays, M3 already validates direction |
| M4 Walidacja problemu | 🟢 High | Bez customer validation pre-seed VC zignoruje |
| **M5 Napkin math** | 🔴 **Must-have** | Bez basic unit econ VC nie inwestuje, nawet pre-seed |
| **M6 Exit strategy** | 🟢 High | "Pierwsze pytanie funduszy" — must have at least narrative |
| **M7 Cap table** | 🔴 **Must-have** | CEO + spółka MUST exist before pre-seed |
| M8 MVP | 🟡 Medium | Pre-seed często bez MVP — vision wystarczy |
| M9 Walidacja rozwiązania | 🟡 Medium | LOI nice-to-have ale not blocker dla pre-seed |
| M10 IP/regulacje | 🟠 Sector-specific | MedTech/Biotech: 🔴 Must. SaaS: 🟡 Medium |
| **M11 Materiały** | 🔴 **Must-have** | Dek + 1-pager musi być (iterowane, nie z 1 tygodnia) |
| **M12 Lista inwestorów** | 🔴 **Must-have** | Bez targets nie ma co startować |

#### Seed readiness (target ~€2M - €8M)

| Milestone | Weight | Reason |
|---|---|---|
| M1 Analiza rynku | 🔴 Must-have | Bottom-up TAM/SAM, multiple sources, deep |
| M2 Analiza konkurencji | 🔴 Must-have | 5-10 konkurentów + defensible advantage |
| M3 Walidacja z inwestorami | 🟢 High | Już za nami, używamy jako warm leads dla M12 |
| M4 Walidacja problemu | 🔴 Must-have | 10-20+ rozmów, segmenty defined |
| **M5 Napkin math** | 🔴 Must-have | Full unit econ, ratios solid |
| **M6 Exit strategy** | 🔴 Must-have | Comparable exits z liczbami |
| **M7 Cap table** | 🔴 Must-have | Wszystkie założenia + IP cleaned |
| **M8 MVP** | 🔴 Must-have | Working product / demo, NOT vision |
| **M9 Walidacja rozwiązania** | 🔴 Must-have | LOI / pilot agreements / first revenue |
| M10 IP/regulacje | 🟠 Sector | MedTech/Biotech: must. SaaS: medium |
| **M11 Materiały** | 🔴 Must-have | Full deck + financial model 3Y + data room |
| **M12 Lista inwestorów** | 🔴 Must-have | Tiered list, intro pipeline aktywny |

### Krok 3 — Verdict calculation

**GO conditions:**

1. **Wszystkie 🔴 Must-haves done lub ◐ in-progress z deadline'm <2 tygodnie**
2. **>70% wszystkich milestones** w statusie ✓ lub ◐
3. **Brak blocker red flags** (np. brak CEO, IP dispute, broken cap table)

**GO with caveats:**

1. Must-haves done ale niektóre 🟡 medium są ☐ (działamy w paraleli z fundraising)
2. M10 ☐ ale stage pre-seed (postponujemy IP audit do post-term-sheet)

**NOT YET:**

1. >1 Must-have w statusie ☐
2. Blocker red flag (CEO missing, ekonomia się nie spina po M5, IP dispute)
3. Materiały (M11) wymagają więcej niż 2 tygodni żeby były presentable

### Krok 4 — Output (decision document)

```
🚦 FUNDRAISING READINESS — <Projekt>
Data: <YYYY-MM-DD>
Stage planowany: <pre-seed / seed / Series A>
Branża: <D>

╔══ VERDICT ══╗

🟢 GO — gotowi do M12 outreach
🟡 GO WITH CAVEATS — gotowi ale z konkretnymi gap'ami do paralelnego dorobienia
🔴 NOT YET — wymaga konkretnych milestones dorobić przed startem

<2-3 zdania narracji>

╔══ MILESTONE SCORE ══╗

Must-haves done:    X / Y (must be 100%)
Total done/in-prog: X / 12 (must be >70%)
Red flag blockers:  X (must be 0)

╔══ READY MILESTONES (✓) ══╗
- M<N> <name>
- ...

╔══ IN-PROGRESS (◐) ══╗
- M<N> <name> — ETA: <X dni>
- ...

╔══ MISSING (☐) ══╗
- M<N> <name> — required for stage? Must / Nice
- ...

╔══ CRITICAL ISSUES ══╗

🚩 <red flag jeśli wykryty>

╔══ ACTION ITEMS (jeśli GO with caveats / NOT YET) ══╗

PRIORITY 1 (blockers — fix przed outreach):
- <konkret>

PRIORITY 2 (paralelnie z outreach):
- <konkret>

PRIORITY 3 (post-term-sheet):
- <konkret>

╔══ NEXT STEPS ══╗

Jeśli GO:
1. Strategiczne spotkanie z zarządem (Maciek + Jędrzej) — zaplanować outreach
2. Activate M12 outreach plan — typowo 2-3 mies. close cycle
3. Bi-weekly summary cadence (Krok 3) staje się weekly podczas active fundraising

Jeśli NOT YET:
1. <konkret milestone do dorobienia>
2. Re-check za <X tygodni> — kolejny readiness check
```

Spytaj: *"Zapisać do `docs/projekty/<projekt>/readiness-check-YYYY-MM-DD.md`? Wysłać do zarządu z TLDR (Krok 4 z dokumentu — strategiczne spotkanie)?"*

### Krok 5 (jeśli GO) — Outreach planning handoff

Po GO verdict, propozycja:

> *"Verdict: GO. Najnaturalniejszy next step to spotkanie strategiczne z zarządem (Maciek + Jędrzej z dokumentu firmy) — zaplanować outreach. Mogę pomóc przygotować materiały na to spotkanie: (a) TLDR readiness raport (1 page dla zarządu), (b) shortlist 20-30 target inwestorów (M12 build), (c) draft outreach timeline. Co preferowane?"*

## Anti-patterns

| Anti-pattern | Co zrobić zamiast |
|---|---|
| "Czekamy na 12/12 zanim ruszymy" | **Filozofia firmy: idziemy wcześnie, iterujemy**. 8-10/12 z must-haves wystarcza. Czekanie = stracony momentum + ryzyko że konkurent zbiera szybciej |
| GO bez M5 napkin math done | **Hard blocker** — bez basic unit econ pierwsza rozmowa z VC kończy się badly. Napkin to 3-5 dni, no excuse |
| GO bez CEO | **Hard blocker dla pre-seed** — fundusze nie inwestują w "vision without executor". Recruit CEO ZANIM idziemy do VC |
| NOT YET z powodu M10 IP w pre-seed SaaS | **Stage-aware** — M10 IP dla SaaS pre-seed nie blocker. Dla MedTech tak. Adjust expectations |
| "GO" gdy materiały są "z 1 tygodnia pracy" | M11 wymaga **iterowane** materiały — pitch deck który prze szedł 3-5 wersji + pre-feedback od kogoś external. Świeży deck = badly received |
| Bez bi-weekly readiness check podczas active fundraising | Active fundraising = co tydzień nowy update od VC. Bi-weekly readiness check przesuwa się do **weekly** |

## Connect to other skills

- **Pełny stan projektu** → `/heart-vb:assessment` (12-row matrix)
- **Replan po NOT YET** → `vb-process/kickoff` (re-sequence sprintów żeby zamknąć must-haves)
- **Bi-weekly progress** → `vb-process/bi-weekly-summary` (continuous tracking)
- **Build M12 outreach list** → `vb-comms/investor-outreach`
- **Iterowane materiały M11** → `heart-pitch-deck` + `vb-comms/board-prep` + `vb-finance/financial-analyst`
- **Simulacja "co VC powie"** → `heart-orchestrate` Pattern E z personami "skeptyczny GP + believer + operator"
