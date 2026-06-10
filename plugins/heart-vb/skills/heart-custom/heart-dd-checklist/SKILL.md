---
name: heart-dd-checklist
description: "Generuje sector-aware due diligence checklist dla venture na etapie pre-IC. Atomic daily task — odpalasz raz, dostajesz structured checklist który możesz dac founderowi/zespołowi do uzupełnienia. Use when user pyta \"wygeneruj DD checklist dla X\", \"co sprawdzić na DD dla HealthTech venture\", \"checklist do DD dla academic spinout\"."
---

> 🔒 **heart-vb CORE — zawsze, niezależnie od załadowanego skilla:**
> (1) output = prosty polski, zero żargonu (pass/Voices/Pattern-F-internal) · (2) fakty do VC (TAM/multiple/exit/CAC-LTV/regulacje) → zaproponuj cross-check Pattern F zanim trafią do decka · (3) zmiana zadania lub milestone → **załaduj właściwy skill** (`/heart-vb:X`), nie improwizuj · (4) KROK -1 consent przed kosztownym spawnem · (5) taguj [Guessing] na niepewnych liczbach, nie udawaj cross-checku na jednym modelu.

# Heart DD Checklist

Atomic skill — odpalasz raz, dostajesz gotowy DD checklist dopasowany do sektora i etapu venture. NIE jest to workflow management ani process tracking — tylko **generation** checklist'a (czy ktoś go potem realizuje — to user's job).

## Standardowa struktura DD checklist (12-15 sekcji)

### Sekcje universal (każdy venture)

| # | Sekcja | Co MUSI być sprawdzone |
|---|--------|--------------------------|
| 1 | **Company basics** | KRS / NIP / REGON, status registracji, beneficial owners, address operacyjny |
| 2 | **Cap table** | Aktualny cap table z full dilution, vesting schedules dla foundera, anti-dilution provisions |
| 3 | **Founders** | CVs + referencje, FTE commitment, dual employment, non-compete history, criminal background check |
| 4 | **Team** | Headcount + role split, key hires risk, retention plan, advisory board structure |
| 5 | **Financial** | 3-yr P&L history (jeśli post-revenue), monthly burn, runway, audited financials (jeśli >€500k revenue) |
| 6 | **Tech / Product** | Architecture overview, tech debt assessment, IP ownership, third-party dependencies, security audit status |
| 7 | **Customers** | Customer concentration (>20% z 1 customer = risk), retention curves, NPS, references |
| 8 | **Commercial** | Pricing structure, contract terms (MSAs), payment terms, accounts receivable aging |
| 9 | **Legal** | Pending litigation, IP disputes, regulatory inquiries, employment disputes |
| 10 | **Compliance** | RODO, IP transfers, regulator licensing status (specific per sector niżej) |
| 11 | **References** | 3-5 customer refs, 2-3 ex-employee refs, 2 industry advisor refs |
| 12 | **Use of funds** | Konkretny plan na 18-24 mc, key hires + their cost, marketing/CapEx breakdown |

### Sekcje SECTOR-SPECIFIC (dodaję do uniwersalnych)

#### HealthTech (Wellnoted-style)
- **MDR classification + technical file status** (Class IIa+ = formal Notified Body audit)
- **IRB approvals** dla pilot studies + protocols
- **Clinical advisory board** members + relevant credentials
- **RODO Art. 9 compliance** dla danych medycznych + DPIA assessment
- **NFZ procurement readiness** (jeśli B2G strategy)
- **Reimbursement narrative** + payer evidence
- **Quality management system** (ISO 13485) status
- **Software lifecycle docs** (IEC 62304)

#### Academic spinout
- **IP ownership** — uniwersytecki regulamin, tech transfer agreement z CTT
- **NCBR/NCN grant warunki** — IP rights, commercialization obligations, milestones
- **Foundation patents** — issued / pending / planned, prior art search
- **Founder allocation** — sabbatical vs dual employment, conflict of interest disclosure
- **Publications strategy** — co publikujemy vs co trzymamy jako trade secrets
- **CTT equity/royalties structure** — typowo 5-15% equity + 2-5% royalties
- **Research infrastructure** — lab access, equipment ownership, dependence na uniwersytet
- **IP Box / Ulga B+R** — kwalifikowalność, dokumentacja

#### Energy storage / cleantech
- **EU Battery Regulation 2023/1542 compliance** — carbon footprint, recycled content, due diligence supply chain
- **Capacity market eligibility** + URE certification status
- **Grid connection agreements** — PSE/DSO (jeśli relevant)
- **Battery supply chain** — sourcing diversification, China dependency analysis
- **Environmental impact assessment** + ESG reporting (CSRD)
- **EU Taxonomy alignment** dla green funding eligibility
- **Insurance** — battery fire, environmental liability, professional indemnity
- **Disposal / recycling** strategy (regulatory + cost)

#### FinTech (legacy)
- **KNF licencja status** — required permits + application timeline
- **AMLD6 / MIFID2 / PSD2 compliance** roadmap
- **Vendor security audit** readiness — banki będą pytać
- **DORA preparation** (od 2025 dla critical financial vendors)
- **AML/KYC operational procedures**
- **Outsourcing register** (KNF wymóg dla cloud)
- **Operational continuity plan**

## Inputs które potrzebuję

1. **Venture name + 1-sentence pitch**
2. **Sektor** (HealthTech / Academic / Energy / FinTech / inny — jeśli inny → universal only + suggest custom additions)
3. **Stage** (idea / PoC / MVP / pilot / revenue / growth — wpływa na zakres financial DD)
4. **Round size** (małe seed €200k = lighter DD; €5M Series A = full DD)
5. **Specific concerns** (jeśli user ma red flags — dodam dedicated questions)

## Output format

Markdown checklist z:
- Universal sekcje (12) — bullets z "Sprawdzić: ..."
- Sector-specific sekcje (z odpowiedniego appendix)
- Priority markers: 🔴 (deal-breaker if missing), 🟠 (significant concern), 🟡 (good to have)
- Każda sekcja kończy się z "Status: [ ] not started / [ ] in progress / [ ] complete" jako placeholder

Total checklist length: **3-5 stron** dla typical Series A pre-IC DD.

## Common anti-patterns

- **Generic checklist bez sector adaptation** → marnuje czas, missing sector-specific risks
- **Za długie (>10 stron)** → analyst nie skończy, founder się załamie. Ruthless prioritization.
- **Brak priority markers** → wszystko wygląda na 🔴 equal. Distinguish must-have od nice-to-have.
- **Pomijanie founder/team DD** → kluczowy ryzyko VB, najtrudniejsze do naprawienia post-investment
- **Pytania bez "why" context** → founder odbierze jako biurokratyczne. Każda sekcja: krótka note co badamy

## Use jako standalone

```
"Wygeneruj DD checklist dla 'BioMatrix' — academic spinout z IBB PAN (HealthTech +
 academic), pre-revenue PoC stage, looking for €800k seed extension. Trzy patenty
 filed. Profesor jako CSO 50% time, brak CEO. Concerns: dual employment professor,
 IP licensing z PAN."

→ Zwracam: 
  - 12 universal sections z priority markers
  - HealthTech section (MDR, IRB, clinical advisory, RODO art.9)
  - Academic spinout section (IP, NCBR, founder allocation)
  - Specifically flagged sections (founder, IP) z dodatkowymi pytaniami based on concerns
  - Łącznie ~4 strony, ready do udostępnienia founderowi/zespołowi
```

## Integration

- Generated checklist → daj founderowi/team do uzupełnienia
- Po otrzymaniu odpowiedzi → **board-prep** z findings + **stress-test** dla IC narrative
- Jeśli concerns → **council** Tier L lub Pattern E dla "czy ten venture jest fundable mimo X risk"

Output = **artifact ready do wysłania** founderowi / zespołowi DD. Nie tracker, nie process — same checklist.

## Co to NIE jest

- **NIE process management** — generuję checklist, NIE śledzę progress
- **NIE valuation tool** — to oddzielny job dla comps-analysis / financial-analyst  
- **NIE legal advice** — checklist jest starting point, legal review z prawnikiem za każdym razem osobno
- **NIE one-size-fits-all** — sector + stage + concerns wpływają na zawartość
