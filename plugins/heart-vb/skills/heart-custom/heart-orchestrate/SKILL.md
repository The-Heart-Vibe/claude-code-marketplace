---
name: heart-orchestrate
description: |
  AUTO-orchestrator dla zadań analityka VB. Auto-triggeruje się gdy user prompt
  zawiera multi-entity work (research N firm, build M scenarios, draft K sections),
  comparative analysis (vs/landscape), lub explicit parallel hints. Sam decomposuje
  zadanie, spawnuje N workers przez Agent tool z model:"sonnet", synthesizes wyniki
  w main session (Opus). Implementuje pattern "main Opus = orchestrator, workers
  Sonnet, trivial helpers Haiku" automatycznie — analityk nie musi świadomie dobierać
  modeli ani spawnowac agentów.
  
  Triggery: 'porównaj 5 firm', 'top 10 konkurentów', 'base/bull/bear case',
  'sekcje IC memo', 'landscape scan', 'dla każdej z firm', 'spawn agents',
  multi-entity research/teardown.
  
  NIE używaj dla: pojedynczej decyzji (council solo), single lookup, sequential
  reasoning (krok N+1 zależy od kroku N), final synthesis (to robi main session).
---

# Heart Orchestrate — Auto-spawning workflow

**Cel:** Analityk pisze normalnie ("przebadaj 5 konkurentów", "zbuduj 3 scenariusze"). Ty (Claude w main session) **automatycznie** robisz orkiestrację bez wymagania świadomych wyborów od użytkownika.

**Reguła główna:** Main session = orchestrator (Opus). Workers = spawned Agents (Sonnet). Trivial helpers = Haiku gdy się da.

---

## Decision tree — czy orkiestrować?

**TAK orchestruj** jeśli prompt zawiera ≥1:
- Numeric multi-entity: "5 konkurentów", "top 10", "3 scenariusze", "4 sektory"
- Iteration markers: "dla każdej z firm", "po jednym na sektor", "per company"
- Multi-scenario: "base/bull/bear", "what-if", "sensitivity analysis"
- Comparative: "porównaj X vs Y vs Z", "landscape teardown"
- Multi-section deliverable: "sekcje IC memo" (thesis + risks + financials + ask)
- Explicit: "parallel", "równolegle", "spawn agents"

**NIE orchestruj** jeśli:
- Pojedyncza decyzja → użyj council solo (zostań w main)
- Single lookup → odpowiedz direct (rozważ /model haiku)
- Sequential reasoning (krok B zależy od A) → main session
- Final synthesis 5 outputów → main session (NIE spawn kolejnych)
- User explicit "BEZ COWORK:" / "SINGLE SESSION:" → respect

---

## Standard pattern — execution

### Step 1: Decompose (1-2 min w main)

Wyciągnij listę N entities z prompta:
```
"przebadaj 5 konkurentów AML" → N=5, entities = ["Actico", "Compliance Corp", ...]
"base/bull/bear case dla MarTech SaaS" → N=3, entities = ["base", "bull", "bear"]
"napisz IC memo z sekcjami" → N=4-6, entities = ["thesis", "market", "financials", "risks", "team", "ask"]
```

Jeśli entities nie są explicit — najpierw zapytaj usera lub zrób quick research żeby wygenerować listę. Potem decompose.

### Step 2: Spawn N workers (parallel, Agent tool)

**Critical:** używaj `model: "sonnet"` parameter explicit. Bez tego workers default na model main session (Opus) i przepłacasz.

Wzorzec:
```
Agent({
  description: "Research [entity_name] (1/N)",
  prompt: "Zbadaj [entity_name] przez competitive-teardown skill.
           Wyciągnij: business model, pricing tiers, target ICP, GTM channels,
           tech stack, kluczowe słabości. Jeśli pricing page jest JS-heavy
           użyj chrome-devtools-mcp z evaluate_script.
           
           Sector context: [załącz odpowiedni heart-* skill jeśli FinTech/HealthTech/RE/MarTech]
           
           Zwróć structured output:
           - Name + URL
           - Business model (1-2 sentences)
           - Pricing tiers (table)
           - Target ICP (segment, size, geo)
           - GTM (channels, sales motion)
           - Tech stack
           - Top 3 weaknesses
           - Threat level dla naszego venture (1-5)",
  model: "sonnet",
  subagent_type: "general-purpose"
})
```

Wywołaj N takich Agent({}) **w jednym message** (multi-tool-call) żeby działały parallel.

### Step 3: Wait + synthesize (main session, Opus)

Po wszystkich workers, synthesize w main (NIE spawn kolejnego agenta na to):

```
"Mam 5 teardownów. Synteza:
- Common weaknesses across vendors → [analiza]
- Vendor positioning gaps → [gdzie widzę okazję]
- Threat ranking od najbardziej do najmniej groźnego
- Top 3 rekomendacji dla naszego venture"
```

Optional: jeśli to decyzja, **teraz** wywołaj council w main z syntezą jako kontekstem (NIE w workerach).

---

## Common patterns — quick reference

### Pattern A: Multi-competitor research (Wt analyst flow)

Trigger: "przebadaj N konkurentów"

```
Main (Opus):
  1. Identify top N (deep-research solo, ~3 min)
  2. SPAWN N agents (sonnet, parallel):
     each: competitive-teardown + chrome-devtools-mcp + sector context
  3. Wait ~15-20 min
  4. Synthesize: common gaps, positioning, recommendations
  5. (Optional) Council na "czy widzimy fundable opportunity"
```

### Pattern B: Scenario modeling (Cz analyst flow)

Trigger: "base/bull/bear", "3 scenariusze", "what-if"

```
Main (Opus):
  1. Lock common assumptions (ARPU, churn baseline, CAC range)
  2. SPAWN 3 agents (sonnet, parallel):
     each: saas-metrics-coach + 1 scenariusz (base/bull/bear)
     każdy: explicit assumption delta vs baseline
  3. Wait ~10-15 min
  4. Synthesize: range of outcomes, breakeven sensitivity, risks
```

### Pattern C: IC memo multi-section drafting (Pt analyst flow)

Trigger: "napisz IC memo", "draft pitch deck"

```
Main (Opus):
  1. Define memo structure (thesis, market, team, financials, risks, ask)
  2. SPAWN 5-6 agents (sonnet, parallel):
     each: board-prep + 1 sekcja + relevant heart-* sector context
     każdy: dostaje już zebrane research/financials z poprzednich kroków
  3. Wait ~15 min
  4. Main: integrate sections into coherent narrative
     - Fix transitions
     - Ensure thesis-risk-ask consistency
     - Add executive summary (this only in Opus)
  5. (Optional) Stress-test memo przez stress-test skill solo
```

### Pattern D: Landscape teardown (multi-sector)

Trigger: "scan landscape", "porównaj sektory", "4 sektory"

```
Main (Opus):
  1. Define sectors + criteria framework
  2. SPAWN 4 agents (sonnet, parallel):
     each: market-research + deep-research + sector context (heart-fintech/health/real-estate/martech)
  3. Synthesize: cross-sector heat map, where Heart has best fit
```

### Pattern E: Lightweight council (dla analityka bez Codex) ⭐

Trigger: decision intent (pricing, GTM, build/buy) + profil ANALITYK (gemini-cli only, brak ChatGPT Plus)

**Idea:** Skoro `claude` provider w council CLI nie działa z poziomu Claude Code session, **emulujemy radę** przez:
- **Main session (Claude Opus)** = "Claude perspective" — Twoja własna perspektywa orchestrator
- **N spawned workers (sonnet)** = każdy wywołuje `gemini-cli` przez Bash z **inną PERSONĄ** (sector context to opcjonalny dodatek)
- **Main synthesize** = Claude widzi N gemini perspektyw + ma własną → "effectively 4-LLM debate" bez Codex

**Kluczowe:** **PERSONA jest primary**, sector context to opcjonalny dodatek. Heart pracuje w wielu sektorach (portfolio + corporate VB partnerships) — większość sectors nie jest pre-zdefiniowana w `heart-*-compliance` skillach. Persona reuses across sectors, sector context jest tylko gdy mamy dedykowany skill (FinTech/HealthTech/RealEstate/MarTech z Heart portfolio).

```
Main (Opus, "Twoja perspektywa Claude"):
  1. Zdefiniuj decyzję + zbierz fakty (1-2 min)
  2. Wybierz 3 persony adekwatne do typu decyzji (patrz Persona Library niżej)
  3. SPAWN 3 agents (sonnet) parallel, każdy:
     - Wywołuje przez Bash: ~/.local/bin/council run planner --mode assess \
         "<decyzja>" --providers gemini-cli \
         --context "<persona prompt>" --json
     - OPCJONALNIE: dołącz heart-{sector} context jeśli dotyczy portfolio sektora
     - Zwraca structured gemini output
  4. Main (Opus): masz 3 gemini perspektyw + własną Claude perspective
     → Synthesize:
        - Gdzie wszyscy się zgadzają (high confidence)
        - Gdzie się różnią (kluczowe trade-offs)
        - Twoja finalna rekomendacja
```

### Persona Library — primary mechanism dla Pattern E

Persony pasują **do każdego sektora**. Wybierz 3 adekwatne do typu decyzji:

**Dla pricing / commercial decisions:**
- `pricing analyst` — value-based vs feature-based, elasticity, price floor analysis
- `growth lead / GTM lead` — conversion impact, sales motion fit, ICP signaling
- `VP product` — retention, expansion revenue, tier psychology, usage-based design
- `CFO / financial analyst` — unit economics implications, gross margin, payback

**Dla product / strategy decisions:**
- `product strategist` — market positioning, differentiation, moat building
- `UX researcher` — JTBD, friction analysis, behavioral signals
- `VP engineering` — feasibility, technical debt, scalability trade-offs
- `board member / IC` — strategic narrative, risk appetite, milestone clarity

**Dla GTM / launch decisions:**
- `growth lead` — channel ROI, CAC dynamics, viral coefficients
- `customer success leader` — onboarding friction, expansion paths, churn signals
- `sales leader` — pipeline mechanics, sales cycle, deal velocity
- `marketing lead` — positioning, content strategy, demand gen

**Dla research / opportunity screening:**
- `domain expert` (specific — np. "senior fintech advisor", "ex-McKinsey healthcare lead")
- `skeptic / red-team` — find weaknesses, missed assumptions, downside scenarios
- `customer voice` — would a real buyer pay? what would block them?
- `VC partner` — fundability, exit potential, comparable benchmarks

**Cross-cutting personas (zawsze przydatne):**
- `executive mentor` — long-term strategic angle, second-order effects
- `pragmatist` — what can we actually execute w naszym constraint
- `contrarian` — explicit devil's advocate

### Sector context — OPCJONALNY add-on

Mamy 4 sector contexts w `heart-custom/` które dodaję się DO persony (NIE zastępują):
- `heart-fintech-compliance` (gdy Heart portfolio FinTech: VASBOX, Digital Gateways)
- `heart-healthtech-compliance` (gdy HealthTech: Wellnoted)
- `heart-realestate-context` (gdy Real Estate: Flatte, HomeAlert)
- `heart-martech-ecosystem` (gdy MarTech: UniPerks)

**Reguła:** sector context dodaję się tylko jeśli decyzja DOTYCZY portfolio sektora. Dla NEW sectors (np. EdTech, Energy, Manufacturing) Heart pracuje bez dedykowanego skilla — persona alone jest wystarczająca, opcjonalnie z explicit "industry expert in <X>" w prompt persona.

### Przykład — pricing decision dla VASBOX (FinTech, portfolio)

```
Pytanie: "Pricing $99/$299/$999 tier vs flat $2k roczny dla AML SaaS"

Main (Opus):
  - Moja Claude perspective: dynamika cyklu sprzedaży banków, rolą platform...
  - Spawn 3 workers (sonnet, gemini-cli):
    Agent A → "pricing analyst" + heart-fintech-compliance (opcjonalny sector)
    Agent B → "growth lead" + heart-fintech-compliance
    Agent C → "VP product" + heart-fintech-compliance
  - Synthesize: tier vs flat vs usage-based, KNF compliance constraints
```

### Przykład — pricing decision dla EdTech venture (nowy sektor, brak heart-skilla)

```
Pytanie: "Pricing dla AI-powered tutoring platform dla polskich liceów"

Main (Opus):
  - Spawn 3 workers (sonnet, gemini-cli):
    Agent A → "pricing analyst" — bez sector skilla, focus na K-12 B2B2C dynamics
    Agent B → "growth lead" — focus na akwizycji szkół (przetargi, demos)
    Agent C → "customer voice" — rola rodziców/uczniów/szkół jako trzy buyer types
  - Brak heart-* sector context — persony niosą wystarczająco kontekstu
  - Synthesize bez dependency na portfolio sectorach
```

**Koszt vs prawdziwy council:**

| Opcja | Cost | Czas | Diverse perspectives |
|-------|------|------|---------------------|
| Pattern E (3 gemini workers z personami + main Claude) | ~3 gemini calls + main Opus | ~3-5 min | 4 (Claude + 3 personas) |
| Council CLI gemini solo (degraded analyst) | 1 gemini call | ~30s | 1 (gemini default) |
| Council CLI gemini+codex (tech profile) | 1 gemini + 1 codex | ~1-3 min | 2 (gemini vs gpt-5) |

Pattern E daje **najwięcej różnorodności** dla analityka bez Codex — kosztem ~3 calls gemini (a Workspace ma duży pool). I działa w **DOWOLNYM sektorze** dzięki persona library.

```

---

## Token budget — kiedy się opłaca

| Wzorzec | Cost | Time | Vs sequential |
|---------|------|------|---------------|
| 5 workers Sonnet + 1 main Opus | ~5×sonnet + 1×opus | 15-25 min | 4× szybciej |
| 5× wszystko na Opus w main | 5×opus | 60-80 min | baseline (drogie) |
| 5× wszystko na Sonnet w main | 5×sonnet | 60-80 min | tanie ale wolne |

Sweet spot: workers Sonnet (~10-20× tańsze od Opus per task), orchestrator Opus (deep reasoning na synthezie).

**Nie spawn 10+ workers** — diminishing returns, drogie. Cap na 5-6.

---

## Anti-patterns (NIE rób tego)

| Anti-pattern | Powód | Zamiast tego |
|--------------|-------|---------------|
| Spawn worker który wywołuje council | 5× zużycie limitów Gemini/Codex; inconsistent verdicts | Council solo w main na syntezy |
| Worker bez explicit `model: "sonnet"` | Domyślnie inherituje Opus = drogo | Zawsze `model: "sonnet"` lub "haiku" |
| Spawn na single-entity task | Marnowanie context window | Main solo |
| Spawn na sequential task (B wymaga A) | Workers blokują się | Sequential w main |
| Kolejne spawn na "synthesize results" | Synteza wymaga widzenia wszystkich → main session ma already context | Main robi synteza |
| Spawn 10+ workers | Diminishing returns + drogo | Cap 5-6 |
| Worker bez sector context dla The Heart venture | Drift od konkrety branży | Załącz `heart-fintech-compliance` etc. w prompcie |

---

## Error handling

**Worker fail/timeout:**
- Jeśli 1/5 fail — synthesize z 4. Wspomnij w wyniku że jeden vendor "data unavailable, recommend manual follow-up".
- Jeśli ≥50% fail — abort, spróbuj sequential w main z mniejszym scope.

**Inconsistent outputs:**
- Workers dali różne formaty → main robi normalization PRZED synthesis.
- Use rubryka explicit w prompcie żeby zapobiec.

**Conflicting findings:**
- 2 workers podają sprzeczne dane → flag, main re-verify główne źródła, NIE średnia.

---

## Integration z innymi heart-vb skillami

| Workflow | Workers wywołują | Main wywołuje |
|----------|--------------------|----------------|
| Multi-competitor | competitive-teardown, chrome-devtools-mcp, deep-research | board-prep, council |
| Scenarios | saas-metrics-coach, financial-analyst | hard-call, stress-test |
| IC memo sections | board-prep, investor-materials | board-prep (executive summary), stress-test |
| Landscape scan | market-research, deep-research, heart-* contexts | council (assess fundability) |

---

## Co user słyszy (przykładowa odpowiedź Claude)

Gdy auto-orchestracja fires:

> "Wykryłem multi-entity task (5 konkurentów AML). Aplikuję wzorzec heart-orchestrate:
> 
> 1. Spawnują 5 cowork agents (Sonnet) — każdy obsługuje 1 vendora przez competitive-teardown + chrome-devtools-mcp dla pricing pages
> 2. Czas ~15 min parallel
> 3. Po zakończeniu — synthesizem tu (Opus) w common weaknesses, positioning gaps, recommendations
> 
> Spawn workers teraz, czy chcesz inną decompozycję?"

(Krótkie potwierdzenie, nie ASCII art, nie tłumaczenie kosztów chyba że user pyta.)
