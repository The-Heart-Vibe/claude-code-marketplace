---
name: market-research
description: "Conduct market research, competitive analysis, investor due diligence, and industry intelligence with source attribution and decision-oriented summaries. Use when the user wants market sizing, competitor comparisons, fund research, technology scans, or research that informs business decisions."
origin: ECC
---

# Market Research

Produce research that supports decisions, not research theater.

## When to Activate

- researching a market, category, company, investor, or technology trend
- building TAM/SAM/SOM estimates
- comparing competitors or adjacent products
- preparing investor dossiers before outreach
- pressure-testing a thesis before building, funding, or entering a market

## Research Standards

1. Every important claim needs a source.
2. Prefer recent data and call out stale data.
3. Include contrarian evidence and downside cases.
4. Translate findings into a decision, not just a summary.
5. Separate fact, inference, and recommendation clearly.

## Common Research Modes

### Investor / Fund Diligence
Collect:
- fund size, stage, and typical check size
- relevant portfolio companies
- public thesis and recent activity
- reasons the fund is or is not a fit
- any obvious red flags or mismatches

### Competitive Analysis
Collect:
- product reality, not marketing copy
- funding and investor history if public
- traction metrics if public
- distribution and pricing clues
- strengths, weaknesses, and positioning gaps

### Market Sizing
Use:
- top-down estimates from reports or public datasets
- bottom-up sanity checks from realistic customer acquisition assumptions
- explicit assumptions for every leap in logic

### Technology / Vendor Research
Collect:
- how it works
- trade-offs and adoption signals
- integration complexity
- lock-in, security, compliance, and operational risk

## Output Format

Default structure:
1. executive summary
2. key findings
3. implications
4. risks and caveats
5. recommendation
6. sources

## Quality Gate

Before delivering:
- all numbers are sourced or labeled as estimates
- old data is flagged
- the recommendation follows from the evidence
- risks and counterarguments are included
- the output makes a decision easier

---

## DD by Heart — Milestone Mapping (M1 Analiza rynku)

Ten skill jest **primary tool dla M1** w procesie Venture Building w The Heart (12 non-negotiable milestones). Pełny framework: `/heart-vb-process`.

### Definition of Done (M1)

Output musi spełniać 3 wymiary (z dokumentu firmy):

| Wymiar | Co znaczy |
|---|---|
| **A. Wiedza w slajdzie pitch decka** | TAM/SAM/SOM z realnymi danymi, 3-5 kluczowych trendów, wzrost YoY — wszystko czytelne na 1 slajdzie "Market" |
| **B. Dokument jako suplement do data room** | Pełna analiza z metodologią + źródłami, do data room dla VC due diligence |
| **C. Menadżer / founder umie o tym opowiadać** | W 3 minuty, bez slajdów — narrative musi się przyjąć żeby menadżer nie czytał z kartki w rozmowie z VC |

### Check przed oznaczeniem M1 jako ✓

- [ ] TAM (total addressable market) — global, w EUR/USD, z source
- [ ] SAM (serviceable addressable market) — geografia + segment matching
- [ ] SOM (serviceable obtainable market) — realistic 3-5 lat
- [ ] 3-5 kluczowych trendów (regulatory, technological, demographic) — każdy z evidence
- [ ] Wzrost YoY — historic 3-5 lat + forecast
- [ ] Slajd "Market" w pitch deck'u draft (M11)
- [ ] Menadżer może odpowiedzieć na 3 najczęstsze VC pytania o rynek bez Notion

### Red flags (z dokumentu firmy)

- 🚩 "Rynek 15 mld w Polsce" bez source (typowy oversize)
- 🚩 "Rynek jest duży" bez liczb
- 🚩 Top-down only (no bottom-up sanity check)
- 🚩 Source > 3 lata stare bez aktualizacji
- 🚩 TAM == SAM (założenie że "całkowity rynek = nasz rynek")

### Connect to other milestones

- **Po M1 done** → M2 Analiza konkurencji (`competitive-teardown`) — często paralelnie w tygodniach 1-2
- **M1 + M2 razem** = wystarczające do M3 (early signal z inwestorami)
- **M1 feeds M11** — slajd Market w pitch deck'u
- **M1 inputs do M5** — SAM/SOM size używane do break-even calc
