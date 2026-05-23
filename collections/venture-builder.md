# Venture Builder — The Heart edition

**Dla:** analitycy i konsultanci w The Heart pracujący nad budową nowych przedsięwzięć.

**Kontekst firmy:** The Heart to venture builder łączący ekspertyzę naukową z komercjalizacją. Trzy główne ścieżki:
1. **Research commercialization** — bringing breakthrough science z laboratoriów akademickich na rynek
2. **Founder partnerships** — building ventures z founderami przyprowadzającymi koncept
3. **Corporate venture building** — partnerstwa z korporatami

**Sektory portfolio:** FinTech (VASBOX, Digital Gateways), Real Estate (Flatte, HomeAlert), MarTech (UniPerks), HealthTech (Wellnoted).

**Metodologia:** design thinking workshops → PoC → MVP → market.

Skille pogrupowane wg fazy. **Każdy instalujesz osobno**. Sekcje [Token-efficient practices](#token-efficient-practices) i [Sector addenda](#sector-addenda) mają kluczowe znaczenie dla rozsądnego użycia zasobów i kontekstu domenowego.

---

## Faza 0 — Deal screening & opportunity intake

Co robisz: przeglądasz incoming pipelines — naukowcy z technologią, founderzy z konceptem, corporate inquiry. Trzeba szybko ocenić **fit + potential** zanim się zaangażujesz głębiej.

| Skill | Co daje | Install |
|-------|---------|---------|
| `private-equity:screen-deal` | Strukturalny filter dla incoming opportunities (fit, size, risk) | `/plugin install screen-deal@private-equity` |
| `private-equity:dd-checklist` | Wczesny DD checklist — co sprawdzić zanim pójdziemy dalej | `/plugin install dd-checklist@private-equity` |
| `private-equity:dd-prep` | Przygotowanie deep DD case dla IC | `/plugin install dd-prep@private-equity` |
| **`council`** ⭐ | Quick fit/no-fit decyzja z 2-3 perspektyw | (już w marketplace) |

**Przykładowy prompt — research opportunity z PAN:**
```
/council Profesor X z IBB PAN ma patent na AI-driven biomarker 
discovery dla early-stage cancer. Zespół 2 osoby (lider + postdoc), 
brak biznesowego co-foundera. Wstępna walidacja medyczna na 200 pacjentach. 
Fit dla The Heart? Top 3 commercialization paths.
```

---

## Faza 1 — Opportunity Discovery & Sizing

Co robisz: szukasz problemów wartych rozwiązania, mierzysz rynek **z naciskiem na Polskę/CEE i UE**, profilujesz konkurencję.

| Skill | Co daje | Install |
|-------|---------|---------|
| `everything-claude-code:market-research` | TAM/SAM/SOM, segmentacja, trendy makro | `/plugin install market-research@everything-claude-code` |
| `everything-claude-code:deep-research` | Multi-step research z syntheze evidence | `/plugin install deep-research@everything-claude-code` |
| `everything-claude-code:exa-search` | Token-efficient web search (vs WebFetch per URL) | `/plugin install exa-search@everything-claude-code` |
| `product-skills:competitive-teardown` | Rozbiór konkurenta: model, pricing, GTM, tech | `/plugin install competitive-teardown@product-skills` |
| `marketing-skills:competitor-profiling` | Strukturalne profile do tabel porównawczych | `/plugin install competitor-profiling@marketing-skills` |

**Przykładowy prompt — FinTech sizing CEE:**
```
/council Rozmiar rynku AML/KYC SaaS dla mid-market banków w CEE 
(Polska, Czechy, Rumunia, Węgry, Słowacja). TAM/SAM, top 5 graczy 
(local + global), kluczowe wymogi regulacyjne (AMLD6, MIFID2). 
Czy to fundable opportunity dla The Heart?
```

> 💡 Dla CEE i Polski browser tooling z `chrome-devtools-mcp:chrome-devtools` jest **znacznie tańszy** niż wielokrotne WebFetch — patrz [Token-efficient practices](#token-efficient-practices).

---

## Faza 2 — Validation & Customer Research

Co robisz: walidujesz hipotezy z realnymi userami przed kosztownym build. **Różny workflow dla różnych typów ventures:**

- **Research-based** → wymaga walidacji u "naukowo-świadomych" buyerów (CTO, R&D heads, lab directors)
- **Founder-led** → klasyczne JTBD + persona interviews
- **Corporate VB** → walidacja u sponsorów korporacyjnych (CIO/CMO/Head of Innovation)

| Skill | Co daje | Install |
|-------|---------|---------|
| `product-skills:product-discovery` | JTBD, persona, problem-solution fit framework | `/plugin install product-discovery@product-skills` |
| `product-skills:ux-researcher-designer` | Plan interviews, syntheze, friction mapping | `/plugin install ux-researcher-designer@product-skills` |
| `product-skills:experiment-designer` | Smoke test, fake door, MVP | `/plugin install experiment-designer@product-skills` |
| `marketing-skills:customer-research` | Customer interviews + analytics → insights | `/plugin install customer-research@marketing-skills` |

**Przykładowy prompt — Real Estate (Flatte-style validation):**
```
Zaprojektuj fake-door experiment dla AI-powered apartment valuation 
dla brokerów real estate w Warszawie. Sample: 30 brokerów z 5 agencji. 
Sukces criteria, czas trwania, sample size, jak skonstruować landing 
po polsku z language relevant dla branży.
```

---

## Faza 3 — Strategy & Decision-making

Co robisz: podejmujesz duże decyzje (build/buy, pricing, scope, GTM, founder hire).

| Skill | Co daje | Install |
|-------|---------|---------|
| **`council`** ⭐ | Multi-LLM debate dla każdej dużej decyzji | `/plugin install council@the-heart-vibe` |
| `superpowers:brainstorming` | Strukturalne generowanie opcji przed decyzją | `/plugin install brainstorming@superpowers` |
| `product-skills:product-strategist` | Positioning, differentiation, narrative | `/plugin install product-strategist@product-skills` |
| `business-growth-skills:contract-and-proposal-writer` | Term sheets, founder agreements, corporate deal proposals | `/plugin install contract-and-proposal-writer@business-growth-skills` |

**Przykładowy prompt — pricing decision dla HealthTech:**
```
/council Wellnoted v2 pricing dla medycznego rynku PL: 
A) Freemium dla doctors + paid pacjent tier (€7/mo) 
B) B2B kontrakty z przychodniami (€500/mo per practice) 
C) Hybrid: free pacjent + paid B2B z analytics dashboard. 
Co wybrać dla 2026 mając target ARR €300k/24mc i compliance ze 
ustawą o ochronie danych medycznych?
```

---

## Faza 4 — Financial Modeling

Co robisz: liczysz unit economics, projekcje, valuation, returns scenarios.

| Skill | Co daje | Install |
|-------|---------|---------|
| `private-equity:unit-economics` | CAC, LTV, payback, contribution margin | `/plugin install unit-economics@private-equity` |
| `model-builder:3-statement-model` | P&L + balance + cashflow, 5-yr projection | `/plugin install 3-statement-model@model-builder` |
| `model-builder:dcf-model` | DCF valuation gdy potrzebny exit case | `/plugin install dcf-model@model-builder` |
| `private-equity:returns` | IRR, MOIC, base/bull/bear scenarios | `/plugin install returns@private-equity` |
| `model-builder:comps-analysis` | Trading + transaction comps dla benchmarków | `/plugin install comps-analysis@model-builder` |

**Przykładowy prompt — VASBOX-style unit economics:**
```
Unit economics dla FinTech SaaS B2B w PL (AML monitoring): 
- ARPU €450/mo per bank klient 
- gross margin 72% (z kosztem compliance audit) 
- CAC €18k (long sales cycle 9 mc, account-based marketing) 
- 8% rocznego churn (banki nie zmieniają vendor często) 
Pokaż payback, LTV, LTV/CAC, breakeven w mc i przy ilu klientach.
```

---

## Faza 5 — Build Prep & Spec

Co robisz: przekładasz strategy na konkretne artefakty dla buildera (PM/dev/zewnętrzny zespół).

| Skill | Co daje | Install |
|-------|---------|---------|
| `product-management:write-spec` | PRD/spec format dla zespołu dev | `/plugin install write-spec@product-management` |
| `product-skills:landing-page-generator` | Landing do smoke testów + fake door | `/plugin install landing-page-generator@product-skills` |
| `product-skills:saas-scaffolder` | Scaffold MVP — useful gdy briefujesz dev | `/plugin install saas-scaffolder@product-skills` |
| `product-management:roadmap-update` | Kwartalny roadmap z OKR mapping | `/plugin install roadmap-update@product-management` |

**Przykładowy prompt — MVP brief dla UniPerks-style MarTech:**
```
Napisz PRD dla MVP "Heart Loyalty" — micro-rewards SaaS dla 
e-commerce SME w PL (10-100 employees). Scope MVP (8 tyg, 2 dev): 
user stories, integracje (Shopify, WooCommerce), success metrics 
(activation, weekly active merchants), out-of-scope (mobile app, 
advanced analytics), kluczowe dependencies.
```

---

## Faza 6 — Investment Committee & Pitch

Co robisz: przedstawiasz tezę inwestycyjną IC The Heart lub external investors / corporate sponsors.

| Skill | Co daje | Install |
|-------|---------|---------|
| `private-equity:ic-memo` | IC memo: thesis, risks, returns, ask | `/plugin install ic-memo@private-equity` |
| `pitch-agent:pitch-deck` | Pitch deck dla inwestorów / komitetu | `/plugin install pitch-deck@pitch-agent` |
| `everything-claude-code:investor-materials` | One-pagery, teaser, data room prep | `/plugin install investor-materials@everything-claude-code` |
| `product-management:stakeholder-update` | Regularne update'y dla stakeholders | `/plugin install stakeholder-update@product-management` |
| `everything-claude-code:investor-outreach` | Lista i outreach do potential investors | `/plugin install investor-outreach@everything-claude-code` |

**Przykładowy prompt — IC memo:**
```
Napisz IC memo dla "Heart [Venture Name]" dla The Heart IC: 
thesis, market opportunity (z polską perspektywą), team (lider + 
co-founder profile), traction-to-date (jeśli jest), 3-yr P&L 
+ unit economics summary, competitive moat (vs local + global), 
top 3 risks z mitigations, ask (kwota + ekwity + 18-mc milestones).
```

---

## Cross-cutting — używaj zawsze

| Skill | Co daje | Install |
|-------|---------|---------|
| **`council`** ⭐ | Każda znacząca decyzja → 2nd opinion via multi-LLM | `/plugin install council@the-heart-vibe` |
| `stop-slop` | Wycina AI slop ze wszystkich outputów | `/plugin install stop-slop` |
| `chrome-devtools-mcp:chrome-devtools` | Token-efficient browsing dla research | `/plugin install chrome-devtools@chrome-devtools-mcp` |

---

## Sector addenda

Dla ventures w danym sektorze sięgaj po dodatkowe skille:

### FinTech (VASBOX, Digital Gateways)
- **Regulatory awareness:** każde IC memo musi pokrywać compliance z KNF, AMLD6, MIFID2, PSD2, RODO (artykuł 9 dla danych biometrycznych)
- **Skille extra:** brak dedykowanego — używaj `council` z personą "senior fintech compliance officer" + `--files` z relevant regulacją
- **Pricing realities:** banki PL kupują z 9-12mc cyklem; SaaS w finansach często wymaga on-prem / sovereign cloud option

### HealthTech (Wellnoted)
- **Regulatory:** MDR (Medical Device Regulation), RODO art. 9 (dane szczególnych kategorii), ustawa o systemie informacji w ochronie zdrowia
- **Skille extra:** `council` z personą "clinical advisor + health data privacy expert"
- **Validation:** wymaga clinical advisory board, nie samych user interviews. IRB approval gdy idziemy w pilot z pacjentami
- **Pricing:** B2B do przychodni/NFZ zwykle przez przetarg, nie self-serve

### Real Estate (Flatte, HomeAlert)
- **Polish specifics:** rynek bardzo lokalny (Warszawa ≠ Kraków ≠ Trójmiasto), niski cyfryzacji u brokerów
- **Validation:** broker interviews + data partnerships z OtoDom/Morizon
- **Pricing:** zwykle commission-based lub freemium z paid lead-gen tier

### MarTech (UniPerks)
- **Klient:** e-commerce SME (10-500 employees) używa Shopify/WooCommerce/PrestaShop
- **Skille extra:** `marketing-skills:revops` dla GTM, `marketing-skills:pricing-strategy` dla tier design
- **Distribution:** App Store w Shopify/WooCommerce, partnerships z agencjami

---

## Token-efficient practices

⚠️ **Najważniejsza sekcja**. Bez tych praktyk zespół spali Claude Code session quota w 2 tygodnie zamiast w 2 miesiące.

### 1. Browser tools > WebFetch dla research

**Problem:** Każdy `WebFetch` to fetch+LLM-summarize → drogie i powolne dla multi-page research.

**Rozwiązanie:** Użyj **Chrome DevTools MCP** lub **Playwright**:
- Otwiera jedną sesję przeglądarki
- Naviguj między stronami bez re-fetch
- Wyciągaj tekst przez `evaluate_script` selektywnie (tylko to co potrzebne)
- Screenshoty zamiast pełnego HTML gdy szukasz visual context

```
# Zamiast:
"Sprawdź 10 konkurentów AML w Polsce" → 10× WebFetch (drogie)

# Zrób:
"Użyj chrome-devtools-mcp żeby otworzyć ranking AML vendors na 
G2.com, wyciągnij top 10 nazw+pricing, potem dla każdej firmy 
otwórz pricing page i wyciągnij tier structure"
```

### 2. Context7 zamiast generic web search dla docs

Jeśli potrzebujesz docs do biblioteki/API/SDK → `context7-plugin:docs` (bezpośredni dostęp do docs index) zamiast WebFetch/WebSearch.

### 3. `council` zawsze z `--json`

Bez `--json` council zwraca rich text z ramkami ASCII art zjadający tokeny przy parsowaniu.

### 4. `--files` zamiast wklejania długich treści

Masz brief 5-stronicowy? Daj go jako plik:
```bash
council run planner --mode assess "Oceń ten brief" \
  --files brief.md,personas.md,benchmarks.csv \
  --providers gemini-cli,codex --json
```
Limit: 50KB/plik, 200KB łącznie. Lepiej niż 5 wiadomości z paste.

### 5. Delegate to subagents

W trakcie sesji Claude Code, używaj agentów do pracochłonnych tasks:
- **research** → użyj `Explore` lub `gsd-phase-researcher` zamiast main session
- **code analysis** → `code-explorer` zamiast samodzielnego grepowania w main
- **document review** → przekazuj plik agentowi z konkretnym pytaniem

Każdy spawn agenta = osobny context window. Twój main session pozostaje czysty.

### 6. Council provider strategy

- **Domyślnie:** `gemini-cli,codex` (omiń Claude Code session) — patrz [council SKILL.md](../plugins/council/skills/council/SKILL.md)
- **Dla quick check:** `gemini-cli` solo (Workspace OAuth ma największe limity)
- **`claude` provider:** ❌ NIE z poziomu aktywnej Claude Code session (self-invocation block)

### 7. `--no-artifacts` dla quick checks

Tier S council runs — dodaj `--no-artifacts`. Nie zapisuje na disk, szybciej, mniej overhead.

### 8. Caching wyników

Council i deep-research wyniki **zapisuj do plików** w projekcie (`research/`, `decisions/`). Następnym razem ktoś z zespołu nie odpala ponownie tego samego — dołącza przez `--files`.

### 9. Suggested session pattern

```
1. Załaduj kontekst raz: --files brief.md,prior-research.md
2. Decyzje robi council Tier M/L
3. Quick clarifications odpowiada Claude z kontekstu (bez nowych call)
4. Outputy zapisuj do /research, /decisions, /memos folderów
5. Następna sesja zaczyna z tymi plikami
```

---

## Sugerowany flow tygodnia

| Dzień | Faza | Skille |
|-------|------|--------|
| Pn | Pipeline screening: nowe inquires | screen-deal, dd-checklist, council |
| Wt | Discovery: deep dive w wybrane opportunities | market-research, exa-search, competitive-teardown |
| Śr | Validation: interviews / experiment design | product-discovery, experiment-designer |
| Cz | Modeling: unit econ + projekcje | unit-economics, 3-statement-model |
| Pt | Komunikacja: IC update / pitch refinement | ic-memo, stakeholder-update |

---

## Co NIE pasuje dla tej roli

| Skill | Dlaczego nie |
|-------|--------------|
| `engineering:*`, `rust-*`, `go-*`, `cpp-*` | Inżynierskie — niech robi team techniczny |
| `marketing-skills:popup-cro`, `signup-flow-cro`, `paid-ads` | Growth-stage skille — dopiero po PMF |
| `pdf-viewer:fill-form`, `pdf-viewer:sign` | Operacyjne admin tasks |
| `wealth-management:*` | Inny use case (planowanie majątkowe klienta indywidualnego) |
| Sektor-specific dla branż których nie robimy (oil&gas, manufacturing, defense) | Nie nasze sektory |

> Note: `chrome-devtools-*` i `playwright-*` SĄ przydatne (token-saving) — patrz Token-efficient practices powyżej.

---

## Maintenance

Lista będzie ewoluować w miarę feedbacku zespołu. PR mile widziane.
Last update: 2026-05-23 (sesja v0.2.0 — The Heart calibration, sector addenda, token-saving practices)
