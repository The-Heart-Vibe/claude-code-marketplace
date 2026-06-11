---
name: heart-dd-prep
description: "Przygotowuje strukturalną ANALIZĘ POTENCJAŁU INWESTYCYJNEGO / DD case dla venture pre-IC (Investment Committee The Heart). Atomic daily task — one-page case z thesis/strengths/concerns/asks gotowy do IC. To DOMYŚLNY skill gdy ktoś prosi o ocenę/analizę projektu dla inwestora lub IC. Triggeruj na: 'analiza potencjału inwestycyjnego', 'analiza inwestycyjna projektu', 'oceń venture dla IC', 'przygotuj na Investment Committee', 'czy warto zainwestować', 'potencjał inwestycyjny X', 'przygotuj DD case dla X', 'pre-IC memo', 'zsyntezuj findings do IC', 'weryfikacja danych z pitch decku przed inwestycją', 'investment analysis', 'investment potential'."
---

> 🔒 **heart-vb CORE — zawsze, niezależnie od załadowanego skilla:**
> (1) output = prosty polski, zero żargonu (pass/Voices/Pattern-F-internal) · (2) fakty do VC (TAM/multiple/exit/CAC-LTV/regulacje) → zaproponuj cross-check Pattern F zanim trafią do decka · (3) zmiana zadania lub milestone → **załaduj właściwy skill** (`/heart-vb:X`), nie improwizuj · (4) KROK -1 consent przed kosztownym spawnem · (5) taguj [Guessing] na niepewnych liczbach, nie udawaj cross-checku na jednym modelu.

# Heart DD Prep

Atomic skill — bierze findings z DD process (odpowiedzi od founder, customer interviews, market data) i przygotowuje **structured one-page case** dla IC. NIE jest to process management — to synthesis output.

## Format one-page DD case

### Header (zawsze)
```
🏛️ DD CASE: [Venture Name] | [Sektor] | [Round size] | [Lead analyst]

THESIS (1 zdanie):
[Czemu wierzymy że venture warto sfinansować]

DECISION REQUESTED:
[Konkretne pytanie do IC: approve €X, reject, więcej diligence]
```

### Sekcje (per priority)

| # | Sekcja | Format | Max length |
|---|--------|--------|-------------|
| 1 | **Investment thesis** | 2-3 sentences max + 3 bullet support points | 6 linii |
| 2 | **Strengths** | Top 3 — explicit evidence, NIE generic ("strong team") | 6 linii |
| 3 | **Top concerns** | Top 3 — z explicit mitigation lub flag jako open question | 6 linii |
| 4 | **Key metrics snapshot** | Tabela: revenue/ARR, growth, gross margin, burn, runway, customers, churn | tabela 6-wierszowa |
| 5 | **Use of funds** | Konkretne: hires X (€Y), product Z (€W), marketing (€V), reserve (€U) | tabela |
| 6 | **18-mo milestones** | 4-6 measurable goals z deadlines | bullet list |
| 7 | **Cap table post-investment** | Tabela: founder X%, IP holder Y%, Heart Z%, option pool A%, future round headroom B% | tabela |
| 8 | **DD references status** | Customers (✓/✗), ex-employees (✓/✗), industry advisors (✓/✗) z key takeaways | 4-6 linii |
| 9 | **Sector-specific risks** | 2-3 risks specyficzne dla sektora (z compliance/regulatory/market) | 4 linii |
| 10 | **Recommendation** | Conditional approve / reject / further DD — z konkretnym warunkiem | 1-2 zdania |

**Total target:** 1 strona A4 (max 1.5 jeśli skomplikowany venture). NIC więcej — IC nie przeczyta.

## Sector-specific risk template (sekcja 9)

| Sektor | Top 3 ryzyk do flag w DD case |
|--------|---------------------------------|
| **HealthTech** | (1) MDR audit timeline — może opóźnić launch o 12-18mc; (2) NFZ procurement w wyborach 2027 może zmienić politykę; (3) Clinical advisory board status — czy mamy realnie autorityetowych członków |
| **Academic spinout** | (1) Founder dual employment — czy uniwersytet sabbatical proven path?; (2) IP ownership rozliczone z CTT przed wejściem? (3) Czy spinout ma CEO commercial — bez tego risk wysokoki |
| **Energy storage** | (1) EU Battery Regulation 2027 deadline — czy supply chain compliant?; (2) Battery cell supplier diversification — China dependency?; (3) Grid connection timeline + PSE/DSO partner committed? |
| **FinTech** (legacy) | (1) KNF licencja timeline — może opóźnić launch 12mc; (2) Bank vendor security audit — czy mamy ISO 27001/SOC 2 plan?; (3) DORA preparation status (od 2025) |

## Decision frameworks (sekcja 10)

DD case kończy się **clear recommendation**:

| Verdict | Co znaczy | Następny krok |
|---------|-----------|----------------|
| ✅ **Approve** | Wszystkie key concerns mitigated, thesis solid | Term sheet w 1-2 tyg |
| 🟡 **Conditional approve** | Approve under conditions (e.g. dependent on KNF license, second pilot) | IC zatwierdza warunki, sign condition na term sheet |
| 🟠 **Further DD** | Concerns wymagają więcej work przed IC decision | Plan kolejnych 2-4 tyg z konkretnymi pytaniami |
| 🔴 **Reject** | Fundamentalny gap (team / market / IP / regulator) | Krótkie polite decline letter + reason |
| ⏸️ **Park** | Interesting ale nie teraz — re-engage gdy X się zmieni | Set re-check date 3-6 mc |

## Inputs które potrzebuję

1. **Venture name + sektor + round size**
2. **DD findings** — paste lub `--files` z DD checklist responses + interview notes + financial data
3. **Lead analyst opinion** (1-2 zdania — co Ty myślisz po DD)
4. **Specific IC concerns** (jeśli IC ma pre-existing skepticism)

Jeśli brak DD findings → pytaj user żeby uzupełnił. Bez konkretnych evidence DD case staje się fluff.

## Common anti-patterns

- **DD case > 2 strony** → IC nie przeczyta. Cut ruthlessly.
- **Thesis składa się z buzzwordów** ("revolutionary AI", "disruptive") → trash. Konkretne "co" zamiast "wow".
- **Strengths bez evidence** — "strong team" zamiast "ex-Apple cardiac monitoring lead + 12-year clinical advisor"
- **Concerns hidden lub sugarcoated** → IC wykryje. Lepiej explicit + mitigation.
- **Brak recommendation** → IC nie wie czego od nich chcesz. ZAWSZE clear verdict.
- **Use of funds vague** ("rozwój produktu") zamiast bottom-up (3 engineers × €X × 18 mc + sales tools €Y + ...)
- **Founder allocation bez explicit FTE** dla academic spinouts → IC fail bez tej liczby

## Output format

Markdown one-page (max 1.5 page) z above sekcjami. Header zawsze top, recommendation zawsze bottom. Tabele zwięzłe.

Jeśli skomplikowany venture (>€2M round, multi-stakeholder) → dorzucisz **appendix 1-2 strony** z deep-dives na specific risks. Ale main case = 1 strona.

## Use jako standalone

```
"Przygotuj DD case dla BioMatrix (HealthTech academic spinout z IBB PAN, €800k seed).
 DD findings: 3 patenty + 1 pending, 5 customer pilots z WUM, prof. Kowalski jako CSO
 50% FTE, brak commercial CEO, 4-osobowy team, MDR Class IIa audit jeszcze nie zaczęty,
 NCBR Bridge Alpha matched €200k. Concerns ze strony IC: brak CEO commercial, MDR
 timeline, IP licensing rate z PAN (15% royalty trochę wysoko)."

→ Zwracam:
   - One-page DD case z thesis (founder traction + clear path do MDR + matched funding)
   - 3 strengths z evidence (patents, NCBR validation, customer pilots WUM)
   - 3 concerns z mitigations (CEO hire warunek inwestycji, MDR consultant na boardzie, 
     IP rate negotiowany)
   - Key metrics + use of funds + 18-mo milestones
   - Verdict: 🟡 Conditional approve — pending CEO hire w 90 dni od term sheet
```

## Integration

- Przed dd-prep: **dd-checklist** żeby zebrać findings, **deep-research** dla customer/market context
- W trakcie: **comps-analysis** dla valuation triangulation, **financial-analyst** dla projections check
- Po dd-prep: **board-prep** żeby zbudować pełen IC memo z this case jako appendix, **council** Tier L jeśli IC chce 2nd opinion

Output = **artifact ready do IC** — Ty edytujesz, dopracowujesz, wysyłasz do IC chair przed meetingiem.

## Co to NIE jest

- **NIE prowadzenie procesu DD** — to robi człowiek (analyst/lead). Skill bierze RESULTS i syntheszuje.
- **NIE pełny IC memo** — to robi board-prep. DD case = ~1-strona, IC memo = 3-5 stron.
- **NIE rekomendacja inwestycyjna** — to robi human IC. Skill prepares decision artifact.
