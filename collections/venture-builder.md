# Venture Builder — The Heart edition

**Dla:** analitycy i konsultanci w The Heart pracujący nad budową nowych przedsięwzięć.

**Kontekst firmy:** The Heart to venture builder łączący ekspertyzę naukową z komercjalizacją. Trzy główne ścieżki:
1. **Research commercialization** — bringing breakthrough science z laboratoriów akademickich na rynek
2. **Founder partnerships** — building ventures z founderami przyprowadzającymi koncept
3. **Corporate venture building** — partnerstwa z korporatami

**Sektory portfolio:** FinTech (VASBOX, Digital Gateways), Real Estate (Flatte, HomeAlert), MarTech (UniPerks), HealthTech (Wellnoted).

**Metodologia:** design thinking workshops → PoC → MVP → market.

---

## Setup (jeden install)

```
/plugin marketplace add The-Heart-Vibe/claude-code-marketplace
/plugin install heart-vb@the-heart-vibe
```

Po tym masz wszystkie 30 skilli z tej kolekcji. Bez dodawania innych marketplaces. Pełne onboarding step-by-step → [onboarding-vb.md](onboarding-vb.md).

---

## Mapa skilli per faza

Wszystkie skille są w pluginie `heart-vb` (zainstalowane jednorazowo). Tu pokazujemy **gdzie ich szukać** podczas konkretnej fazy pracy.

### Faza 0 — Deal screening & opportunity intake

Przeglądasz incoming: naukowcy z technologią, founderzy z konceptem, corporate inquiry.

| Skill | Kategoria | Do czego |
|-------|-----------|----------|
| `deal-desk` | vb-commercial | Strukturalny filter dla incoming opportunities |
| `commercial-forecaster` | vb-commercial | Wstępne sizing potencjału |
| `board-prep` | vb-comms | Quick IC fit/no-fit memo |
| **`council`** ⭐ | council | Quick fit-or-not decision z multi-LLM debate |

**Przykładowy prompt — research opportunity z PAN:**
```
Profesor X z IBB PAN ma patent na AI-driven biomarker discovery 
dla early-stage cancer. Zespół 2 osoby (lider + postdoc), brak 
biznesowego co-foundera. Wstępna walidacja medyczna na 200 pacjentach. 
Fit dla The Heart? Top 3 commercialization paths.
```

→ Hook fires (screening intent + sector) → Claude pyta o `deal-desk` + `heart-healthtech-compliance` + opcjonalnie council.

---

### Faza 1 — Opportunity Discovery & Sizing

Mierzysz rynek, profilujesz konkurencję, ze focusem na Polskę/CEE i UE.

| Skill | Kategoria | Do czego |
|-------|-----------|----------|
| `deep-research` | vb-research | Multi-step research z syntheze evidence |
| `market-research` | vb-research | TAM/SAM/SOM, segmentacja, trendy makro |
| `exa-search` | vb-research | Token-efficient web search vs WebFetch |
| `competitive-teardown` | vb-product | Rozbiór konkurenta: model, pricing, GTM, tech |

**Przykładowy prompt — FinTech sizing CEE:**
```
Rozmiar rynku AML/KYC SaaS dla mid-market banków w CEE (PL, CZ, RO, 
HU, SK). TAM/SAM, top 5 graczy (local + global), kluczowe wymogi 
regulacyjne (AMLD6, MIFID2). Czy to fundable opportunity dla The Heart?
```

→ Hook fires (research + sector) → sugeruje `deep-research` + `heart-fintech-compliance` jako context.

> 💡 Dla CEE/Polski browser tooling (chrome-devtools-mcp) jest **tańszy niż WebFetch** TYLKO przy multi-page + `evaluate_script` z konkretnym selektorem. Patrz [Token-efficient practices](#token-efficient-practices).

---

### Faza 2 — Validation & Customer Research

Walidujesz hipotezy zanim wydasz $ na build. Różny workflow per typ venture:
- **Research-based** → walidacja u "naukowo-świadomych" buyerów (CTO, R&D heads, lab directors)
- **Founder-led** → klasyczne JTBD + persona interviews
- **Corporate VB** → walidacja u sponsorów (CIO/CMO/Head of Innovation)

| Skill | Kategoria | Do czego |
|-------|-----------|----------|
| `product-discovery` | vb-product | JTBD, persona, problem-solution fit framework |
| `ux-researcher-designer` | vb-product | Plan interviews, syntheze, friction mapping |
| `experiment-designer` | vb-product | Smoke test, fake door, MVP design |
| `product-strategist` | vb-product | Positioning + narrative testing |

**Przykładowy prompt — Real Estate validation:**
```
Zaprojektuj fake-door experiment dla AI-powered apartment valuation 
dla brokerów RE w Warszawie. Sample: 30 brokerów z 5 agencji. 
Sukces criteria, czas trwania, sample size, jak skonstruować landing 
po polsku z language relevant dla branży.
```

→ Hook fires (validation + RE sector) → sugeruje `experiment-designer` + `heart-realestate-context`.

---

### Faza 3 — Strategy & Decision-making

Duże decyzje: build/buy, pricing, scope, GTM, founder hire.

| Skill | Kategoria | Do czego |
|-------|-----------|----------|
| **`council`** ⭐ | council | Multi-LLM debate dla każdej dużej decyzji |
| `pricing-strategist` | vb-commercial | Tier design, value-based vs feature-based |
| `product-strategist` | vb-product | Positioning, differentiation, narrative |
| `channel-economics` | vb-commercial | Sales channel ROI, partner economics |
| `hard-call` | vb-comms | Framework dla trudnych decyzji strategicznych |

**Przykładowy prompt — pricing dla HealthTech:**
```
Wellnoted v2 pricing dla medycznego rynku PL: 
A) Freemium dla doctors + paid pacjent tier (€7/mo) 
B) B2B kontrakty z przychodniami (€500/mo per practice) 
C) Hybrid: free pacjent + paid B2B z analytics dashboard. 
Co wybrać dla 2026 mając target ARR €300k/24mc + compliance z ustawą 
o ochronie danych medycznych?
```

→ Hook fires (decision + pricing + HealthTech) → council Tier L z `--context heart-healthtech-compliance` + `pricing-strategist`.

---

### Faza 4 — Financial Modeling

Unit economics, projekcje, valuation, returns scenarios.

| Skill | Kategoria | Do czego |
|-------|-----------|----------|
| `financial-analyst` | vb-finance | Pełne 3-statement (P&L + balance + cashflow) |
| `saas-metrics-coach` | vb-finance | CAC, LTV, payback, churn, MRR/ARR, magic number |
| `commercial-forecaster` | vb-commercial | Top-down + bottom-up rev forecast |

**Przykładowy prompt — VASBOX-style unit economics:**
```
Unit economics dla FinTech SaaS B2B w PL (AML monitoring): 
- ARPU €450/mo per bank klient 
- gross margin 72% (z kosztem compliance audit) 
- CAC €18k (long sales cycle 9 mc, account-based marketing) 
- 8% rocznego churn (banki nie zmieniają vendor często) 
Pokaż payback, LTV, LTV/CAC, breakeven w mc i przy ilu klientach.
```

→ Hook fires (modeling) → sugeruje `saas-metrics-coach`.

---

### Faza 5 — Build Prep & Spec

Przekładasz strategy na artefakty dla builderów (PM/dev/zewn. zespół).

| Skill | Kategoria | Do czego |
|-------|-----------|----------|
| `product-strategist` | vb-product | High-level scope + roadmap |
| `experiment-designer` | vb-product | PoC + MVP scope (Heart-methodology aligned) |
| `deal-desk` | vb-commercial | Terms dla pilot/early customers |

**Note:** product-management:write-spec NIE jest bundled — jeśli potrzebujesz PRD format, użyj `product-strategist` + ręczny outline.

---

### Faza 6 — Investment Committee & Pitch

Tezę inwestycyjną przedstawiasz IC The Heart, external investors, lub corporate sponsors.

| Skill | Kategoria | Do czego |
|-------|-----------|----------|
| `board-prep` | vb-comms | IC memo (thesis, risks, returns, ask) |
| `investor-materials` | vb-comms | One-pagery, teaser, data room prep |
| `investor-outreach` | vb-comms | Lista i outreach do potential investors |
| `stress-test` | vb-comms | Pre-IC scenario stress test (devil's advocate) |

**Przykładowy prompt — IC memo:**
```
Napisz IC memo dla "Heart [Venture Name]" dla The Heart IC: 
thesis, market opportunity (z polską perspektywą), team (lider + 
co-founder profile), traction-to-date, 3-yr P&L + unit economics 
summary, competitive moat (vs local + global), top 3 risks z 
mitigations, ask (kwota + ekwity + 18-mc milestones).
```

→ Hook fires (writing intent) → sugeruje `board-prep` + odpowiedni `heart-*-context` per sektor.

---

### Cross-cutting — używaj zawsze

| Skill | Kategoria | Do czego |
|-------|-----------|----------|
| **`council`** ⭐ | council | Każda znacząca decyzja → 2nd opinion via multi-LLM |
| `self-improving-agent` | self-improving | Agent auto-uczy się z MEMORY.md |
| `/si:review` | self-improving | Cotygodniowy review: co warto promote do CLAUDE.md |
| `/si:promote` | self-improving | Pattern → CLAUDE.md (permanent) |
| `/si:extract` | self-improving | Recurring pattern → reusable skill |
| `/si:status` | self-improving | Memory health dashboard |
| `/si:remember` | self-improving | Save knowledge explicitly |

---

## Sector addenda — heart-custom skills

Pakiet zawiera 4 sector-specific loadery context. Używaj jako `--context` dla council lub jako standalone reference w IC memo.

### `heart-fintech-compliance` (VASBOX, Digital Gateways)

KNF, AMLD6, MIFID2, PSD2, RODO, DORA. Sales cycle 9-18mc, often on-prem requirement. Vendor security questionnaire mandatory.

### `heart-healthtech-compliance` (Wellnoted)

MDR classification (zwykle IIa+), RODO art. 9 (dane szczególnych kategorii), IRB approval przed pilotem, NFZ procurement realities, integracje z systemem P1.

### `heart-realestate-context` (Flatte, HomeAlert)

Polski rynek RE: dominujące portale (OtoDom, Morizon, Domiporta), regionalność (WAW ≠ KRK ≠ Trójmiasto), licencja RPI, niski digital adoption u brokerów.

### `heart-martech-ecosystem` (UniPerks)

Shopify/WooCommerce/Allegro ecosystem, polski SME e-commerce, distribution patterns (App Store, agency partnerships), niższy willingness-to-pay vs US/UK.

---

## Token-efficient practices

⚠️ **Najważniejsza sekcja.** Bez tych praktyk zespół spali Claude Code session quota w 2 tygodnie zamiast w 2 miesiące.

### 1. Browser tools vs WebFetch — kiedy co

**Zasada:** Chrome DevTools NIE jest automatycznie tańszy. Wygrywa tylko w specyficznych scenariuszach + przy użyciu `evaluate_script` z konkretnym selektorem (nie `take_snapshot`).

| Scenariusz | Wybierz | Powód |
|------------|---------|-------|
| 1 statyczna strona, lookup | **WebFetch** | ~500 tok summary vs 2-8k tok snapshot |
| 2-4 strony, ad-hoc | **WebFetch** | Cache 15min, brak setup browsera |
| 5+ stron, multi-step research | **DevTools + evaluate_script** | Jedna sesja, brak re-load tax, targeted extraction <500 tok |
| JS-heavy SPA / login required | **DevTools** | WebFetch widzi tylko shell HTML |
| Forms / interactive flows | **DevTools** | WebFetch nie umie |

**Wzorzec użycia (token-efficient):**

```
# Bad — eats 6000+ tokenów na całą stronę
"Otwórz https://g2.com/aml-software i zrób take_snapshot"

# Good — targeted, ~200 tokenów
"Otwórz https://g2.com/aml-software, 
 evaluate_script: document.querySelectorAll('.product-card .title')
   .map(el => el.textContent)
 zwróć tylko listę nazw"

# Best — workflow z compounding savings
"Otwórz G2 AML listing → evaluate_script: top 10 nazw + URLs → 
 dla każdej z 10 firm: navigate + evaluate_script pricing tier
 (1 sesja, 11 calls, ~3000 tok total vs 11× WebFetch = 6600+ tok)"
```

### 2. Council provider strategy

- **Domyślnie:** `--providers gemini-cli,codex` (NIE Claude Code session)
- **Tier S:** `--providers gemini-cli` solo
- `claude` provider: ❌ NIE z poziomu aktywnej Claude Code session (self-invocation block)

### 3. `--json` zawsze z council

Bez `--json` council zwraca rich text z ramkami ASCII art zjadający tokeny przy parsowaniu.

### 4. `--files` zamiast wklejania długich treści

Brief 5-stronicowy? Daj jako plik:
```bash
council run planner --mode assess "Oceń ten brief" \
  --files brief.md,personas.md,benchmarks.csv \
  --providers gemini-cli,codex --json
```
Limit: 50KB/plik, 200KB łącznie.

### 5. Subagent delegation

Pracochłonny task → delegate do agenta (osobny context window):
- research → `Explore` lub `gsd-phase-researcher`
- code analysis → `code-explorer`
- document review → przekaż plik agentowi z konkretnym pytaniem

Main session pozostaje czysty.

### 6. `--no-artifacts` dla Tier S

Tier S quick checks — dodaj flag, nie zapisuje na disk.

### 7. Cache wyniki do plików

Council i deep-research wyniki **zapisuj** w projekcie (`research/`, `decisions/`). Następnym razem ktoś z zespołu nie odpala ponownie — dołącza przez `--files`.

### 8. Session pattern

```
1. Załaduj kontekst raz: --files brief.md,prior-research.md
2. Decyzje robi council Tier M/L
3. Quick clarifications odpowiada Claude z kontekstu (bez nowych call)
4. Outputy zapisuj do /research, /decisions, /memos
5. Następna sesja zaczyna z tymi plikami
```

### 9. Self-improving raz w tygodniu

`/si:review` raz na 1-2 tygodnie. Co cyklicznie się powtarza → `/si:promote` do CLAUDE.md. Po 2 miesiącach CLAUDE.md staje się żywym playbookiem zespołu.

---

## Sugerowany flow tygodnia

| Dzień | Faza | Skille |
|-------|------|--------|
| Pn | Pipeline screening: nowe inquires | deal-desk, council, board-prep |
| Wt | Discovery: deep dive w wybrane opportunities | deep-research, exa-search, competitive-teardown |
| Śr | Validation: interviews / experiment design | product-discovery, experiment-designer |
| Cz | Modeling: unit econ + projekcje | saas-metrics-coach, financial-analyst |
| Pt | Komunikacja: IC update / pitch refinement | board-prep, investor-materials, /si:review |

---

## Co NIE pasuje dla tej roli

| Skill | Dlaczego nie |
|-------|--------------|
| `engineering:*`, `rust-*`, `go-*`, `cpp-*` | Inżynierskie — niech robi team techniczny |
| `marketing-skills:popup-cro`, `signup-flow-cro`, `paid-ads` | Growth-stage skille — dopiero po PMF |
| `pdf-viewer:fill-form`, `pdf-viewer:sign` | Operacyjne admin tasks |
| `wealth-management:*` | Inny use case (planowanie majątkowe klienta) |
| Sektor-specific dla branż których nie robimy (oil&gas, manufacturing, defense) | Nie nasze sektory |

> Note: `chrome-devtools-*` i `playwright-*` SĄ przydatne (token-saving) — patrz Token-efficient practices.

---

## Maintenance

Lista będzie ewoluować w miarę feedbacku zespołu. PR mile widziane.

**Last update:** 2026-05-24 (v0.2.0 — single-install bundle, 30 skilli w heart-vb, dodano self-improving + heart-custom sector contexts)
