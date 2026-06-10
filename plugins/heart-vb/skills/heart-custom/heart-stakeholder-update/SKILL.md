---
name: heart-stakeholder-update
description: "Pisze weekly/monthly stakeholder update dla portfolio company → investors lub IC The Heart. Atomic daily task — odpalasz raz, dostajesz structured update z progress/blockers/asks. Use when user pyta \"napisz update do investors za October\", \"monthly update dla IC za Q3\", \"co wpisać do email do stakeholders\"."
---

> 🔒 **heart-vb CORE — zawsze, niezależnie od załadowanego skilla:**
> (1) output = prosty polski, zero żargonu (pass/Voices/Pattern-F-internal) · (2) fakty do VC (TAM/multiple/exit/CAC-LTV/regulacje) → zaproponuj cross-check Pattern F zanim trafią do decka · (3) zmiana zadania lub milestone → **załaduj właściwy skill** (`/heart-vb:X`), nie improwizuj · (4) KROK -1 consent przed kosztownym spawnem · (5) taguj [Guessing] na niepewnych liczbach, nie udawaj cross-checku na jednym modelu.

# Heart Stakeholder Update

Atomic skill dla pisania regularnych updateów. Format zaprojektowany dla VB analyst → IC / external investors / corporate partners.

## Standardowy format Heart update (1-2 strony max)

### TL;DR (3-4 zdania na początku — ZAWSZE)

> "Q3 2026: zamknęliśmy pilot z 3 przychodniami w PL z 87% retention, MRR €18k (+24% MoM), zatrudniliśmy CTO. Główny challenge: regulator audit MDR wymaga +€80k unplanned. Ask: intro do 2 corporate partnerów w insurance (Allianz / Warta)."

Jeśli reader przeczyta tylko 4 zdania — wie czy iść dalej.

### Sekcje (per priorytet ważności)

| Sekcja | Co zawiera | Czego unikać |
|--------|-------------|---------------|
| **1. Highlights (top 3-5)** | Konkretne osiągnięcia z liczbami: revenue, customers, hires, milestones | Generic "we made progress", brak liczb |
| **2. Metrics dashboard** | MRR/ARR + delta, customer count + churn, burn rate + runway, kluczowe KPI per sektor | Cherry-picking tylko good metrics — pokaż też te które idą gorzej |
| **3. Lowlights / Blockers** | Co nie działa, co opóźnia. Explicit, nie sugarcoated | Pretending wszystko jest fine, vague descriptions |
| **4. Asks (max 3)** | Konkretne prośby: intro do X, decision od IC w sprawie Y, hire Z | "Wsparcie ogólne", "więcej funduszy" — vague asks |
| **5. Next 4-6 weeks plan** | Top 3 priorytety + measurable outcomes | Lista 10 wszystkich rzeczy które chcemy zrobić |
| **6. Risks** *(monthly only)* | Top 3 risks + mitigation status | Brak risk section / claim "no risks" |

## Frequency-specific patterns

### Weekly update (~1/3 strony)
- Skip metrics dashboard (no meaningful delta w tydzień)
- Focus: highlights (2-3), blockers (1-2), asks (1-2)
- Tone: operational, tactical
- Format: bullet points OK

### Monthly update (1 strona)
- Pełen format z dashboard
- Tone: balance operational + strategic
- Mix bullet + narrative paragraphs (2-3 dla context)

### Quarterly update / board update (1-2 strony)
- Pełen format + risks section + strategic context
- Tone: strategic, decision-oriented
- Forward look 3-6mc, nie tylko past quarter

## Sector-specific KPIs do uwzględnienia

| Sektor | Critical metrics na dashboard |
|--------|--------------------------------|
| **HealthTech** | Pilot sites count, patient enrollment, clinical advisory feedback, MDR audit status, NFZ kontrakt progress |
| **Academic spinout** | Patents filed/granted, NCBR/EU grant status, founder allocation (FTE %), publications, customer pilots from research |
| **Energy storage** | MW deployed, PSE/DSO pipeline value, capacity market participation status, EU Battery Reg compliance %, ESG metrics |
| **FinTech** | KNF licencja status, vendor security audit progress, bank pipeline (deals × value), AML reports processed |
| **Generic SaaS** | MRR, ARR, gross retention, net retention, CAC, payback period, burn rate, runway |

## Common anti-patterns

- **"Quiet update" — tylko good news** → IC wykryje. Lepiej explicit z bad + plan.
- **Asks ogólne** — "wsparcie biznesowe" zamiast "intro do CFO @ Allianz"
- **Brak liczb** — "growing nicely" zamiast "MRR +24% MoM to €18k"
- **Dłuższe niż 2 strony** — IC nie przeczyta. Cut ruthlessly.
- **Praising oneself** — "great quarter", "amazing team" — niepotrzebne, evidence > self-assessment
- **Vague timelines** — "soon", "kontynuujemy" → konkretne dates / weeks

## Inputs które potrzebuję

1. **Period** (week ending DD.MM / month / quarter)
2. **Sender role + audience** (analytic do IC / founder do investors / corporate VB lead do partners)
3. **Sektor** (HealthTech / Academic / Energy / FinTech / generic)
4. **Latest metrics** (revenue, customers, burn) — jeśli możesz, daj numbers + delta
5. **Highlights** (2-5 bullet points co się stało)
6. **Blockers** (co nie działa lub co cię opóźnia)
7. **Asks** (czego potrzebujesz od reader)
8. **Tone** (operational/strategic/board-level)

Jeśli brak metryki — pytaj user, NIE wymyślaj liczb.

## Output format

Markdown 1-2 stronic z sekcjami above. Zachowaj TL;DR na samym górze. Bullet points dla weekly, mix narrative+bullet dla monthly/quarterly.

## Use jako standalone

```
"Napisz monthly update za październik 2026 dla Wellnoted (HealthTech, AI cardiac
 monitoring) — audience: IC The Heart + external seed investors.
 
 Metrics: MRR €18k (+24% MoM), 3 pilot przychodnie, 87% retention, burn €45k/mo,
 runway 11mc. Hires: CTO start 1.11. Blocker: MDR audit zwlecze launch o 2 mc,
 +€80k unplanned. Asks: intro do Allianz / Warta dla insurance partnership."

→ Zwracam 1-stronicowy update z TL;DR + sekcjami + clean format
```

## Integration

Po wyjściu update możesz:
- `stress-test` żeby check czy nie pomijasz red flags
- `board-prep` jeśli wraz z update planujesz IC meeting
- `heart-deck-handoff` jeśli update ma trafić jako slajdy (board deck) → brief dla Claude Design
- `investor-outreach` jeśli update prowadzi do follow-up rozmów

Output = gotowy do wysłania update jako markdown / plain text email.
