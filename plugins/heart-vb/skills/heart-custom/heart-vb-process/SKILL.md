---
name: heart-vb-process
description: "Master router procesu Venture Building (DD by Heart — 12 milestones). Front door gdy NOWY projekt trafia do venture buildera albo chcesz przeprowadzić projekt przez cały proces: oceń stan + ułóż plan. Wykrywa intencję i deleguje do assessment / kickoff / konkretnego milestone-skilla. Triggeruj na: 'nowy projekt do venture buildera', 'przepuść projekt przez proces', 'przeanalizuj projekt w ramach 12-milestone', 'oceń i ułóż plan dla venture', 'kickoff projektu', 'DD by Heart', 'cały proces dla projektu X'. Pojedyncze zadanie dnia → opisz zadanie, nie ten skill."
---

> 🔒 **heart-vb CORE — zawsze, niezależnie od załadowanego skilla:**
> (1) output = prosty polski, zero żargonu (pass/Voices/Pattern-F-internal) · (2) fakty do VC (TAM/multiple/exit/CAC-LTV/regulacje) → zaproponuj cross-check Pattern F zanim trafią do decka · (3) zmiana zadania lub milestone → **załaduj właściwy skill** (`/heart-vb:X`), nie improwizuj · (4) KROK -1 consent przed kosztownym spawnem · (5) taguj [Guessing] na niepewnych liczbach, nie udawaj cross-checku na jednym modelu.

# Heart VB Process — Master Orchestrator

Jeden entry point dla wszystkiego co dotyczy procesu **Venture Building w The Heart**. Zawiera framework 12 non-negotiable milestones, routing do sub-skilli per milestone, i tryb "full process" (przepuść projekt przez cały framework).

> **To jest tryb PROJEKTOWY — nie jedyny sposób użycia pluginu.** Większość codziennej pracy analityka/konsultanta NIE wymaga tego skilla: do ad-hoc zadań (szybki research, pricing sanity-check, draft update, porównanie konkurentów, deck, pytanie regulacyjne, analiza) **po prostu opisz zadanie** — plugin dobierze właściwy skill bez wchodzenia w proces. `heart-vb-process` odpalaj gdy realnie prowadzisz venture przez cały framework (kickoff, assessment, full pipeline) — nie do pojedynczego zadania dnia.

## Framework — 12 milestones w 4 fazach

```
Discovery (1-5) → Creation (6-8) → Validation (9-10) → Fundraising (11-12)
```

| # | Faza | Milestone | DoD (główne kryteria) | Sub-skill heart-vb |
|---|---|---|---|---|
| **1** | Discovery | **Analiza rynku** | TAM/SAM/SOM, 3-5 trendów, wzrost YoY, slajd Market | `vb-research/market-research` + `vb-research/deep-research` |
| **2** | Discovery | **Analiza konkurencji** | 5-10 konkurentów, funding, model, defensible advantage | `vb-product/competitive-teardown` |
| **3** | Discovery | **Walidacja z inwestorami (early signal)** | 2-3 rozmowy z networku, feedback, go/no-go | `vb-process/investor-early-signal` (W FAZIE 2 v0.7.0) |
| **4** | Discovery | **Walidacja problemu z klientami** | 10-20 rozmów, 2-3 segmenty, problem confirmed | `vb-product/product-discovery` + `vb-product/ux-researcher-designer` |
| **5** | Discovery | **Napkin math** | 1-strona, revenue model, unit econ (COGS/CAC/LTV), break-even, go/no-go | `vb-process/napkin-math` ⭐ |
| **6** | Creation | **Exit strategy & acquirers** | 5-10 acquirers, comparable exits, mnożniki, exit narrative | `vb-process/exit-strategy` ⭐ |
| **7** | Creation | **Zespół & cap table** | CEO/lead, equity, umowy, spółka założona | `vb-process/cap-table-helper` (FAZA 2) |
| **8** | Creation | **MVP / produkt & roadmapa** | Działający demo, roadmapa 6-18mc, %docelowego produktu | `vb-product/product-strategist` + `vb-product/experiment-designer` |
| **9** | Validation | **Walidacja rozwiązania & pricing** | 5+ LOI/pilotów, pricing potwierdzony, pipeline | `vb-commercial/pricing-strategist` + `vb-product/experiment-designer` |
| **10** | Validation | **IP, regulacje & prawo** | IP secured, regulatory path, no legal red flags | `heart-dd-checklist` + sector context (healthtech/academic/energy/fintech) |
| **11** | Fundraising | **Materiały fundraisingowe** | Pitch deck, one-pager, model finansowy, data room | `heart-pitch-deck` + `vb-comms/board-prep` + `vb-finance/financial-analyst` + `vb-comms/investor-materials` |
| **12** | Fundraising | **Lista inwestorów & outreach** | 20-30 targets, intro, CRM, gotowość | `vb-comms/investor-outreach` + `heart-stakeholder-update` |

⭐ = nowe skille w v0.7.0

## Główne zasady (z dokumentu projektowego firmy)

1. **Grube klocki, nie 100 tasków** — guardrails, nie mikromanagement
2. **Deliverable, nie task** — każdy milestone kończy się konkretnym artefaktem (dokument, slajd, model)
3. **Sprinty 2-3 tygodnie** — żaden task >1 mies., 5-6 tasków/tydzień per osoba
4. **Zacznij od największego ryzyka** — co jest deal-breakerem → tym najpierw
5. **Zunifikowane dla wszystkich** — ta sama checklista niezależnie od domeny (regulacje/IP jako add-on)
6. **Stempel The Heart** — wszystkie 12 milestones ✓ = gotowy do fundraisingu (quality gate, nie administracja)
7. **Weryfikacja, nie tylko odhaczyć** — "jest" ≠ "jest dobrze". Menadżer weryfikuje jakość każdego deliverable.

## Kiedy ten skill fire'uje (router behaviors)

### Mode A — Milestone detection z konwersacji

User pisze coś specyficznego dla pojedynczego milestone'a → wykryj który milestone i deleguj do właściwego sub-skill.

| User mówi… | Wykryty milestone | Deleguj do |
|---|---|---|
| "TAM", "SAM", "rozmiar rynku", "trendy", "rynek X bilionów" | **M1** | `vb-research/market-research` |
| "konkurenci", "kto już robi", "5 firm na tym rynku", "defensible advantage" | **M2** | `vb-product/competitive-teardown` |
| "co inwestorzy o tym sądzą", "early signal", "rozmowa z VC z networku" | **M3** | `investor-early-signal` (lub product-discovery jako fallback) |
| "rozmowy z klientami", "JTBD", "10 wywiadów", "segmenty klientów", "problem confirmed" | **M4** | `vb-product/product-discovery` |
| "napkin math", "unit economics", "czy to się spina", "CAC LTV szybko", "ROI na kartce" | **M5** | `vb-process/napkin-math` ⭐ |
| "exit", "kto to kupi", "acquirers", "comparable exits", "mnożniki przy sprzedaży" | **M6** | `vb-process/exit-strategy` ⭐ |
| "cap table", "equity split", "CEO", "ESOP", "advisory agreements", "spółka" | **M7** | `cap-table-helper` (lub `deal-desk` fallback) |
| "MVP", "prototyp", "demo", "roadmapa produktowa", "milestones produktu" | **M8** | `vb-product/product-strategist` |
| "LOI", "pilot agreement", "pricing potwierdzony", "willingness to pay", "5 klientów chce" | **M9** | `vb-commercial/pricing-strategist` |
| "IP", "patent", "regulatory", "CE/FDA", "MDR", "AML", "legal red flags" | **M10** | `heart-dd-checklist` + sector context |
| "pitch deck", "IC memo", "one-pager", "data room", "model finansowy 3Y" | **M11** | `heart-pitch-deck` lub `board-prep` lub `financial-analyst` → po gotowej treści `heart-deck-handoff` (wizualny deck przez Claude Design) |
| "lista inwestorów", "outreach plan", "intro do funduszy", "CRM funduszy" | **M12** | `vb-comms/investor-outreach` |

**KROK -1 (consent gate, jak heart-orchestrate):** jeśli wykryto milestone i jest dedicated sub-skill, spytaj user'a plain language:

> *"To wygląda na temat z milestone **M5 — napkin math**. Mogę uruchomić strukturalny workflow (1-strona z unit econ + go/no-go), albo odpowiedzieć inline. (a) tak, workflow (b) inline (c) sam wiem co chcę."*

### Mode B — Full process orchestration

User mówi: *"przepuść projekt X przez cały proces"*, *"kickoff dla nowego projektu"*, *"zbuduj DD by Heart dla naszej spółki Y"*.

→ Uruchom **pełny pipeline** w 3 krokach:

1. **Krok 1: Assessment** (`vb-process/assessment`) — wykonaj 12-row matrix oceny stanu zastanego (✓/◐/☐ + jakość)
2. **Krok 2: Kickoff** (`vb-process/kickoff`) — risk ranking, harmonogram sprintów, capacity planning, OKR per milestone
3. **Krok 3: Execute** — przejdź milestone po milestone w kolejności wynikającej z risk ranking. Per milestone deleguj do dedicated sub-skill. Po każdym milestone update statusu w outputie.

W trybie full process **NIE pytaj o consent per milestone** — user już zatwierdził cały pipeline. Pytaj tylko o blockery (np. "M3 wymaga rozmów z inwestorami — masz listę? Czy mam pomóc ją zbudować?").

### Mode C — Status check

User pyta: *"gdzie jesteśmy z projektem X"*, *"ile milestones done"*, *"co jeszcze przed fundraisingiem"*.

→ Jeśli user dał link do Notion (lub Notion connector aktywny przez MCP):
- Czytaj Project Card → progress bar X/12 → status per milestone → next steps
- Jeśli brak Notion → spytaj user'a o link albo o ręczny update stanu

→ Jeśli brak Notion access:
- Powiedz wprost: *"Plugin nie ma dostępu do Twojego Notion. Możesz: (a) podać link do project page, (b) dodać Notion MCP connector w Cowork settings, lub (c) opowiedzieć mi w której fazie jest projekt — zaktualizuję świadomość kontekstu w tej sesji."*

## Notion structure (z dokumentu firmy)

Plugin **nie zarządza** Notion automatycznie, ale **zna strukturę** żeby pomóc menadżerowi pracować zgodnie:

### Warstwa 1 — Project Card (widok zarządu)
- Database: **Projects Pipeline**
- Kto patrzy: zarząd, menadżerowie
- Properties: Nazwa, Faza, Progress (X/12), Manager, Status Dashboard z linkami do deliverables (Pitch Deck, Business Case, Lista inwestorów, Teaser, Roadmapa, Cap Table)

### Warstwa 2 — Streams / Milestones (12 klocków)
- Linked database per projekt
- Kto patrzy: Menadżer, zespół
- Per stream: Nazwa, Faza, Status (Backlog → In Progress → Done), Objective, Key Results, Deliverable, Timeline
- Max 2-3 streamy in progress jednocześnie

### Warstwa 3 — Sprint Tasks (Kanban)
- Board view wewnątrz streamu
- Kanban: Backlog → To Do → In Progress → Done
- ~5-6 tasków/tydzień, 2-3 tyg. sprint

## Anti-patterns (NIE rób)

| Anti-pattern | Co zrobić zamiast |
|---|---|
| "Rynek 15 bilionów w Polsce" bez source'a | M1 wymaga **realnych danych** — TAM/SAM/SOM z konkretnych raportów/Statista/branżowych źródeł |
| "Nie mamy konkurencji" | M2 red flag — **zawsze są konkurenci** (substytuty, alternative solutions). Jeśli naprawdę brak — to znaczy że albo rynek nie istnieje, albo źle szukałeś |
| Napkin math pomijany "bo to deep-tech" | M5 jest **kluczowe dla projektów naukowych** — założyciele często nie wiedzą jak to się ma do biznesu. To Twoja rola żeby policzyć |
| Exit strategy ostawione na końcu | M6 to **pierwsze pytanie z funduszy** — najczęściej pomijane. Bez exit narrative nie ma fundraising |
| 12/12 przed pierwszą rozmową z VC | M3 (early signal) **jest specjalnie w fazie Discovery** — idziemy do inwestorów wcześnie z wiedzą o rynku + konkurencji, NIE czekamy na gotowe materiały |
| Materiały fundraisingowe gotowe, lista inwestorów = 0 | M12 powinna **żyć od dnia 1** — sukcesywnie buduj listę, intro identyfikuj, CRM aktualny |

## Co ten skill NIE robi

- **Nie wykonuje milestone'ów sam** — deleguje do dedicated skilli (market-research, competitive-teardown, napkin-math, etc.)
- **Nie zarządza Notion za użytkownika** — wymaga że menadżer prowadzi swoją Notion zgodnie z framework
- **Nie zastępuje weryfikacji jakości** — "stempel The Heart" wymaga że menadżer **zweryfikuje** każdy deliverable, plugin tylko pomaga go wytworzyć
- **Nie pomija KROK -1 consent gate** — w Mode A (milestone detection) zawsze pyta przed odpaleniem sub-skill (chyba że full process Mode B)

## Quick reference dla menadżera

```
Stuck? → /heart-vb-process
  └─ "co dalej?" → assessment
  └─ "kickoff" → assessment + kickoff
  └─ "M5 napkin math" → vb-process/napkin-math
  └─ "M6 exit strategy" → vb-process/exit-strategy
  └─ "rynek?" → vb-research/market-research (M1)
  └─ "konkurenci?" → vb-product/competitive-teardown (M2)
  └─ "klienci?" → vb-product/product-discovery (M4)
  └─ "LOI/pilot?" → vb-commercial/pricing-strategist (M9)
  └─ "deck?" → heart-pitch-deck (M11)
  └─ "inwestorzy?" → vb-comms/investor-outreach (M12)
  └─ "status?" → /heart-status
```
