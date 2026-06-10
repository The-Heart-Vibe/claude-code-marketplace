---
name: heart-comps-analysis
description: "Robi trading + transaction comps dla ventures w portfolio Heart — analizuje 3-7 porównywalnych firm z multiplami (EV/Revenue, EV/EBITDA, EV/ARR), benchmarki rynkowe, valuation range. Atomic daily task — odpalasz raz, dostajesz structured comps table. Use when user pyta \"comps dla X\", \"ile warta jest firma taka jak Y\", \"benchmark valuation dla HealthTech SaaS przy €5M ARR\"."
---

> 🔒 **heart-vb CORE — zawsze, niezależnie od załadowanego skilla:**
> (1) output = prosty polski, zero żargonu (pass/Voices/Pattern-F-internal) · (2) fakty do VC (TAM/multiple/exit/CAC-LTV/regulacje) → zaproponuj cross-check Pattern F zanim trafią do decka · (3) zmiana zadania lub milestone → **załaduj właściwy skill** (`/heart-vb:X`), nie improwizuj · (4) KROK -1 consent przed kosztownym spawnem · (5) taguj [Guessing] na niepewnych liczbach, nie udawaj cross-checku na jednym modelu.

# Heart Comps Analysis

Atomic skill dla buildowania trading + transaction comparable analyses. Daily task — single session.

## Dwa typy comps (każda inna logika)

### Trading comps (public market)
- Porównanie z **publicznie notowanymi** firmami w sektorze
- Mnożniki obliczane z current market cap / latest financials
- Use case: "co rynek wycenia firmy takie jak nasza" — directionally
- Caveats: liquidity premium (public > private), scale effects

### Transaction comps (M&A precedents)
- Porównanie z **niedawnymi przejęciami** firm w sektorze (2-3 lata)
- Mnożniki z deal value / target's financials at acquisition
- Use case: "co strategic acquirer zapłacił za firmy podobne do nas" — exit narrative
- Caveats: strategic premium, synergies, deal-specific structure

**Heart angle:** dla early-stage ventures (pre-revenue lub <€2M ARR) trading/transaction comps są **directionally useful ale NIE precyzyjne**. Główna wartość: framing dla IC narrative, NIE faktyczna wycena (która polega na DCF + market evidence).

## Standardowy comps table format

| Firma | HQ | Stage | ARR (€M) | Growth (YoY) | Gross margin | EV (€M) | EV/Revenue | EV/ARR | Notes |
|-------|-----|-------|----------|---------------|---------------|---------|------------|---------|-------|
| Comp 1 | UK | Public | 45 | 35% | 78% | 540 | 12x | 12x | Premium for retention |
| Comp 2 | US | Acquired 2024 | 18 | 60% | 72% | 270 | 15x | 15x | Strategic by Microsoft |
| Comp 3 | DE | Private (Series C) | 8 | 80% | 68% | 95 | 11.9x | 11.9x | Last round implied |
| Comp 4 | PL | Private (Series A) | 2.5 | 120% | 75% | 22 | 8.8x | 8.8x | Local benchmark |
| ... | | | | | | | | | |
| **MEAN** | | | | | | | **12.0x** | **12.0x** | |
| **MEDIAN** | | | | | | | **11.9x** | **11.9x** | |

## Mnożniki używane w VB (per stage)

| Metric | Pre-revenue | Early SaaS (<€2M ARR) | Growth SaaS (€2-20M ARR) | Mature SaaS (>€20M) |
|--------|-------------|------------------------|---------------------------|----------------------|
| **EV/Revenue** | N/A | 8-15x | 6-12x | 4-8x |
| **EV/ARR** | N/A | 10-20x | 8-15x | 5-10x |
| **EV/Gross Profit** | N/A | 12-25x | 10-18x | 7-12x |
| **EV/EBITDA** | N/A | N/A (unprofitable) | N/A or negative | 15-30x |

**Sector premium/discount:**
- HealthTech (regulated, sticky customers) → premium 1.2-1.5x vs generic SaaS
- DeepTech (academic spinouts) → premium 1.5-2x na patents/moat, discount na execution risk
- Energy storage (hardware-heavy) → discount 0.6-0.8x na CapEx burden
- FinTech (compliance burden) → flat lub slight premium dla banking customers

## Sources do real-world comps

### Public companies (trading comps)
- **Yahoo Finance** / **Bloomberg** — current multiples
- **CapIQ** / **PitchBook** (paid) — best quality
- **SEC EDGAR** — direct 10-K/10-Q dla US, Stockholm Exchange dla EU
- **GPW** — polskie firmy notowane (LiveChat, Cyfrowy Polsat tech segment)

### M&A transactions
- **Mergermarket** / **Dealroom** (paid)
- **CB Insights** — startup deals
- **Crunchbase** — early-stage rounds (proxy dla valuation through implied multiples)
- **TechCrunch / EU-Startups / Money.pl** — PL local deal news

### Polish/CEE-specific
- **Dealroom.co** — CEE startup landscape
- **PFR Ventures** — polskie VC deals
- **PARP / NCBR** — government-supported deal data
- **GPW infosfera** — public PL companies

## Workflow per analysis

### Step 1: Define comps universe (5 min)
- 3-5 trading comps (publicly listed, sektor adjacent)
- 2-4 transaction comps (M&A 2024-2026, similar size)
- Mix lokalne (PL/CEE) + global (US/UK) — local relevance + global benchmark

### Step 2: Collect data (15-30 min)
- ARR / Revenue / Growth / Gross margin / EV
- Filter: NO peer wycen sprzed >3 lat (rynek się zmienił)
- Adjust dla outlierów (firmy z 80%+ growth lub massive losses skewują)

### Step 3: Calculate multiples + apply premium/discount
- Compute mean + median + 25th/75th percentile
- Stage adjustment (lower multiple jeśli our venture earlier)
- Sector premium/discount

### Step 4: Triangulate range
- Output: "Implied EV range €X-Y na current ARR, €Z-W na projected 3-yr ARR"
- ZAWSZE z confidence interval: "median 12x ± 4x given 7 comps"

## Inputs które potrzebuję

1. **Venture name + sector**
2. **Current metrics** (ARR / customer count / growth / gross margin if known)
3. **Stage** (PoC / pilot / early revenue / Series A / etc.)
4. **Geography** (PL only / CEE / EU / global)
5. **Purpose** (IC narrative / fundraise pitch / exit prep / academic exercise)

Jeśli brak metryk → pytaj user.

## Common anti-patterns

- **Cherry-picking comps** które dają wysoką wycenę → IC wykryje, lower trust
- **Brak transactions** → tylko trading multiples zazwyczaj overvaluates private companies
- **Stale data** > 2 lat → market shifted, irrelevant
- **Sample size 1-2 comps** → 1 firma to anecdote, nie analysis. Min 5 comps razem.
- **Ignoring growth rate** → 50% growth firma ≠ 10% growth firma, multiplier MUST adjust
- **EV without debt adjustment** → market cap ≠ enterprise value dla firm z debt

## Output format

3-część output:
1. **Comps table** (markdown table z above format)
2. **Summary stats** — mean / median / percentyle multiples
3. **Implied range dla nas** — EV €X-Y z confidence note + caveats

Plus optional sections:
- "Why we differ from median" — uzasadnienie premium/discount
- "Comparable transactions we should track" — early signal for future
- "Data gaps" — co nie mogłem znaleźć (informuj user explicit)

## Use jako standalone

```
"Comps dla Wellnoted (HealthTech AI cardiac monitoring, €1.2M ARR, 65% YoY growth,
 72% gross margin, polski market). Sample: 5-7 firm. Use case: pre-IC valuation
 narrative dla seed extension."

→ Zwracam:
   - Tabela 6 comps (mix UK/DE/US/PL, public + acquired)
   - Mean 14x ARR, median 12x ARR
   - HealthTech sector premium +20%
   - Stage discount -30% (we're Series A vs growth-stage comps)
   - Implied EV €11-17M na current ARR
   - Caveats: cardiac monitoring niche → liczne comps są broader HealthTech AI
```

## Integration

- Przed comps: **deep-research** dla ostatnich deals + **competitive-teardown** dla landscape map
- Razem z comps: **financial-analyst** dla DCF triangulation (DCF + comps = valuation range)
- Po comps: **board-prep** żeby wcisnąć valuation w IC memo narrative

**Output = analytical artifact ready do IC memo / pitch deck slide 11 / fundraising deck**.


---

## 🤝 Agent-bliźniak

Ten skill ma agenta-bliźniaka: **`comps-analyst`** — spawn jako persona z live data (Bash+WebSearch) + Pattern F verify exitów.

**Skill (ten plik) = dialog w main context** (iterujesz na żywo z userem). **Agent `comps-analyst` = spawn w izolowanym kontekście** (delegated, jeden głos w panelu Pattern E). Ta sama metodyka (ten skill jest single source of truth), dwa tryby wywołania. Wybór: >3 wymiany z userem → skill; autonomous research/raport lub panel → agent.
