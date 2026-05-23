# Venture Builder

**Dla:** analitycy i konsultanci pracujący nad nowymi przedsięwzięciami (od opportunity discovery do investment committee).

**Nie dla:** inżynierów buildujących produkt (oni mają inną kolekcję — TBD).

Skille pogrupowane wg fazy venture building. **Każdy instalujesz osobno** — kliknij link w kolumnie "Install" lub skopiuj komendę.

---

## Faza 1 — Opportunity Discovery & Sizing

Co robisz: szukasz problemów wartych rozwiązania, mierzysz rynek, profilujesz konkurencję.

| Skill | Co daje | Install |
|-------|---------|---------|
| `everything-claude-code:market-research` | TAM/SAM/SOM, segmentacja, trendy makro | `/plugin install market-research@everything-claude-code` |
| `everything-claude-code:deep-research` | Multi-step research z syntheze evidence | `/plugin install deep-research@everything-claude-code` |
| `product-skills:competitive-teardown` | Rozbiór konkurenta: model biznesowy, pricing, GTM, tech stack | `/plugin install competitive-teardown@product-skills` |
| `marketing-skills:competitor-profiling` | Strukturalne profile do tabel porównawczych | `/plugin install competitor-profiling@marketing-skills` |

**Przykładowy prompt (council Tier L, non-tech):**
```
/council Czy rynek AI-powered legal contract review w Polsce jest 
fundable? TAM/SAM, top 5 konkurentów, kluczowe ryzyka.
```

---

## Faza 2 — Validation & Customer Research

Co robisz: walidujesz hipotezy z realnymi userami zanim wydasz $ na build.

| Skill | Co daje | Install |
|-------|---------|---------|
| `product-skills:product-discovery` | JTBD, persona, problem-solution fit framework | `/plugin install product-discovery@product-skills` |
| `product-skills:ux-researcher-designer` | Plan interviews, syntheze, friction mapping | `/plugin install ux-researcher-designer@product-skills` |
| `product-skills:experiment-designer` | Smoke test, fake door, MVP — projekt eksperymentu | `/plugin install experiment-designer@product-skills` |
| `marketing-skills:customer-research` | Customer interviews + analytics → insights | `/plugin install customer-research@marketing-skills` |

**Przykładowy prompt:**
```
Zaprojektuj fake-door experiment dla AI legal review — landing 
page + waitlist signup, sukces criteria, czas trwania, sample size.
```

---

## Faza 3 — Strategy & Decision-making

Co robisz: podejmujesz duże decyzje (build/buy, pricing, scope, GTM strategy).

| Skill | Co daje | Install |
|-------|---------|---------|
| **`council`** ⭐ | Multi-LLM debate dla każdej dużej decyzji | `/plugin install council@the-heart-vibe` |
| `superpowers:brainstorming` | Strukturalne generowanie opcji przed decyzją | `/plugin install brainstorming@superpowers` |
| `product-skills:product-strategist` | Positioning, differentiation, narrative | `/plugin install product-strategist@product-skills` |

**Przykładowy prompt (council Tier L):**
```
/council Pricing tier dla AI legal review B2B: $99/$299/$999 per 
seat/month vs $2k/$5k/$15k flat annual. Target ICP: 50-500 employee 
law firms. Co wybrać?
```

---

## Faza 4 — Financial Modeling

Co robisz: liczysz unit economics, projekcje, valuation, returns.

| Skill | Co daje | Install |
|-------|---------|---------|
| `private-equity:unit-economics` | CAC, LTV, payback, contribution margin | `/plugin install unit-economics@private-equity` |
| `model-builder:3-statement-model` | P&L + balance + cashflow, 5-yr projection | `/plugin install 3-statement-model@model-builder` |
| `model-builder:dcf-model` | DCF valuation gdy potrzebny exit case | `/plugin install dcf-model@model-builder` |
| `private-equity:returns` | IRR, MOIC, base/bull/bear scenarios | `/plugin install returns@private-equity` |

**Przykładowy prompt:**
```
Zbuduj unit economics dla AI legal review SaaS: ARPU $399/mo, 
gross margin 78%, CAC $1,200 z paid + content mix, 5% monthly churn. 
Pokaż payback, LTV, LTV/CAC, contribution margin month-on-month.
```

---

## Faza 5 — Build Prep & Spec

Co robisz: przekładasz strategy na konkretne artefakty do builderów (PM/dev).

| Skill | Co daje | Install |
|-------|---------|---------|
| `product-management:write-spec` | PRD/spec format dla zespołu dev | `/plugin install write-spec@product-management` |
| `product-skills:landing-page-generator` | Landing do smoke testów + fake door | `/plugin install landing-page-generator@product-skills` |
| `product-management:roadmap-update` | Kwartalny roadmap z OKR mapping | `/plugin install roadmap-update@product-management` |

**Przykładowy prompt:**
```
Napisz PRD dla MVP AI legal review: scope, user stories, success 
metrics, out-of-scope, dependencies. Target: 6-tyg build z 2-osobowym 
zespołem.
```

---

## Faza 6 — Investment Committee & Pitch

Co robisz: przedstawiasz tezę inwestycyjną IC lub external investors.

| Skill | Co daje | Install |
|-------|---------|---------|
| `private-equity:ic-memo` | IC memo: thesis, risks, returns, ask | `/plugin install ic-memo@private-equity` |
| `pitch-agent:pitch-deck` | Pitch deck dla inwestorów / komitetu | `/plugin install pitch-deck@pitch-agent` |
| `everything-claude-code:investor-materials` | One-pagery, teaser, data room prep | `/plugin install investor-materials@everything-claude-code` |
| `product-management:stakeholder-update` | Regularne update'y dla stakeholders | `/plugin install stakeholder-update@product-management` |

**Przykładowy prompt:**
```
Napisz IC memo dla "Heart Legal AI": thesis, market opportunity, 
team, traction, financials (3-yr P&L + unit economics), competitive 
moat, top 3 risks z mitigations, ask ($500k seed for 18mc runway).
```

---

## Cross-cutting — używaj zawsze

| Skill | Co daje | Install |
|-------|---------|---------|
| **`council`** ⭐ | Każda znacząca decyzja → 2nd opinion via multi-LLM | `/plugin install council@the-heart-vibe` |
| `stop-slop` | Wycina AI slop ze wszystkich outputów | `/plugin install stop-slop` |

---

## Sugerowany flow tygodnia

| Dzień | Faza | Skille |
|-------|------|--------|
| Pn | Discovery: skanujesz 3 obszary | market-research, competitive-teardown |
| Wt | Validation: interviews z 5 prospects | ux-researcher-designer, customer-research |
| Śr | Strategy: decyzje go/no-go | council, product-strategist |
| Cz | Modeling: unit econ + projekcje | unit-economics, 3-statement-model |
| Pt | Komunikacja: IC update / pitch refinement | ic-memo, stakeholder-update |

---

## Co NIE pasuje dla tej roli

Skille które wyglądają kusząco ale są dla innych ról (engineerów / późnego stage):

| Skill | Dlaczego nie |
|-------|--------------|
| `engineering:*`, `rust-*`, `go-*`, etc. | Inżynierskie — niech robi to team techniczny |
| `marketing-skills:popup-cro`, `signup-flow-cro` | Late-stage growth — dopiero gdy masz produkt i traffic |
| `pdf-viewer:fill-form`, `pdf-viewer:sign` | Operacyjne admin tasks |
| `chrome-devtools-*`, `playwright-*` | QA / debugging tools |

---

## Maintenance

Lista będzie ewoluować w miarę feedbacku zespołu. PR mile widziane.
Last update: 2026-05-23 (sesja v0.1.0 marketplace bootstrap)
