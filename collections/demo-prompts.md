# Demo prompts — heart-vb v0.6.x

**Cel:** progressive demo z managerem/analitykiem żeby zobaczyć plugin w akcji. 10 promptów w 5 fazach, ~60-90 min.

**Pre-demo checklist:**
- [ ] User ma zainstalowane heart-vb (Cowork: Customize → Personal plugins → + → Add marketplace · CLI: `/plugin install heart-vb@the-heart-marketplace`)
- [ ] `~/.local/bin/council doctor` → minimum `gemini-cli OK`
- [ ] `cat ~/.claude/settings.json | grep heart-` → powinno być 4 hooki
- [ ] `claude mcp list | grep chrome-devtools` → MCP zainstalowany przez install.sh (wymagane dla Prompt 10). Jeśli FAIL: re-run install.sh — auto-instaluje przez `claude mcp add`
- [ ] User wie że może użyć `BEZ COUNCIL:` / `BEZ COWORK:` / `BEZ DEVTOOLS:` jako opt-out

**Co obserwować w trakcie demo:**
- Czy hooki fire (komunikaty 💡 / 🔧 / 🤖 / 🎚️ w UI)
- Czy Claude pyta o zgodę **plain language** (NIE "Pattern E/F")
- Czas response per prompt
- Czy output jest **briefing-style** (~150 słów) vs research dump

---

## FAZA 1 — Baseline (no orchestration, ~10 min)

### Prompt 1: Trivial lookup
```
Co znaczy ARPU w SaaS metrykach? 1 zdanie wystarczy.
```

**Expected behavior:**
- 🎚️ Model Router fires: tier haiku (trivial lookup)
- Inne hooki: silent ✅
- Solo Claude answer, ~3s
- **Bez** consent question — to tylko lookup

**Co pokazuje:** plugin NIE spamuje hookami trivial promptów. Zero friction dla quick questions.

---

### Prompt 2: Single sector lookup
```
Wyjaśnij prosto różnicę między MDR Class IIa a IIb dla SaaS medycznego. Max 4 zdania.
```

**Expected behavior:**
- 💡 vb-suggest fires: research intent + HealthTech sector
- Sugeruje aktywację `heart-healthtech-compliance` jako context
- Claude może spytać "Mam zaaplikować sector context HealthTech?" lub odpowiedzieć od razu z wiedzy
- Krótki structured output ~4 zdania

**Co pokazuje:** sector context auto-detection bez heavy orchestration.

---

## FAZA 2 — Heart skills auto-activation (~15 min)

### Prompt 3: DD checklist generation
```
Wygeneruj DD checklist dla academic spinout z IBB PAN — venture: AI-powered biomarker discovery dla early-stage cancer detection (HealthTech). 
Stage: PoC z 50 pacjentami WUM, looking for €800k seed. 
Profesor jako CSO 50% FTE, brak commercial CEO.
```

**Expected behavior:**
- vb-suggest: screening intent + 2 sectors (academic + HealthTech)
- Aktywacja `heart-dd-checklist` + `heart-academic-spinouts` + `heart-healthtech-compliance`
- Output: structured checklist z priority markers + sector-specific MDR/IRB/IP additions
- **Bez** consent dialog — single skill activation, nie orchestracja

**Co pokazuje:** single skill produkuje praktyczny artifact, sector-aware. Manager widzi że plugin "wie" o Heart sektorach.

---

### Prompt 4: Pitch deck dla BESS venture
```
Napisz 10-slide pitch deck outline dla "GridFlex" — BESS Storage-as-a-Service 
dla industrial peak shaving w PL. Stage: pilot z 1 zakładem CCS, ARR €120k. 
Target: €2M Series A. Konkurencja: Northvolt, kilka mniejszych integratorów.
```

**Expected behavior:**
- vb-suggest: writing intent + energy sector
- Aktywacja `heart-pitch-deck` + `heart-energy`
- Output: 10-12 slide outline z capacity market, EU Battery Reg compliance, BESS biz model

**Co pokazuje:** strukturyzowany deck-ready artifact dopasowany do Heart portfolio sektora.

---

## FAZA 3 — Decision z konsultacją 3 ekspertów (~20 min)

### Prompt 5: Pricing decision HealthTech
```
Pricing dla HealthTech SaaS B2B sprzedawanego do polskich przychodni:
A) Tier €99/€299/€999 per practice/mo
B) Flat €2500/rok per practice
Target ARR: €500k w 24mc, sales cycle 6-9 mc, decision-maker: zarząd przychodni.
Co wybrać?
```

**Expected behavior:**
- 4 hooki fire: vb-suggest, cowork-suggest, model-route OPUS, sector hint
- **KROK -1 (KEY MOMENT):** Claude pyta w **plain language**:
  > *"To wygląda na decyzję wartą konsultacji z kilkoma ekspertami. Mogę zapytać 3 ekspertów (pricing analyst / growth lead / VP product), różne perspektywy, ~60s. (a) Tak (b) Tylko Ty (c) Sam wiem co wybrać"*
- Manager odpowiada "a"
- Auth check (cache), spawn 3 cowork agents parallel → ~60s
- Briefing synthesis (~150 słów): rekomendacja + 2-3 verify points + bottom line

**Co pokazuje:**
- Explicit consent — Claude **NIE spawnuje** bez user yes
- Plain business language (NIE "Pattern E")
- Multi-perspective convergence/divergence
- Krótki actionable output, nie analytics dump

---

### Prompt 6: Build vs partner decision
```
Czy budować AI-powered contract review SaaS dla polskich kancelarii czy partnerować z istniejącym US vendorem (Harvey, Spellbook)? 
Stage: idea, mamy €200k pre-MVP budget i 3-osobowy team (2 dev + 1 sales).
```

**Expected behavior:**
- Decision intent (build-vs-buy keyword)
- KROK -1 consent w plain language
- 3 personas dobrane do typu decyzji: founder / strategic / financial advisor
- Synthesis: clear path forward + risks

**Co pokazuje:** persony są **adekwatne do typu decyzji** — Claude wybiera różne osoby dla pricing vs build/buy (nie statyczny zestaw).

---

## FAZA 4 — Research z cross-check 3 AI (~20 min)

### Prompt 7: NCBR funding facts
```
Jakie są aktualne wymagania NCBR Szybka Ścieżka dla deep tech spinouts 
w 2026? Konkretnie:
- Maksymalna kwota grantu
- Maksymalna długość projektu
- Minimum własności IP przez aplikanta
- Czy wymaga partner przemysłowy
```

**Expected behavior:**
- vb-suggest: research intent + academic spinout sector
- **KROK -1 consent:**
  > *"To wygląda na pytanie faktualne. Mogę zweryfikować przez 3 niezależne AI (Claude + Gemini + GPT-5), wykryje hallucinacje pojedynczego modelu, ~90s. (a) Tak (b) Tylko ze swojej wiedzy (c) Sam zweryfikuję"*
- Manager: "a"
- Auth check (jeśli codex OK → 3 workers, jeśli FAIL → 2 workers + note)
- Synthesis: konkretne liczby + "voices: X/3" + verify points dla disagreement

**Co pokazuje:** cross-LLM fact verification, graceful degradation jeśli codex nie zalogowany.

---

### Prompt 8: Energy regulatory check (cross-vertical)
```
Co MUSZE wiedzieć przed wejściem na polski rynek energetyczny z ofertą 
EnergyTech SaaS (forecasting + EMS) dla OZE wytwórców i DSO:
- RED III RFNBO targets — kto i kiedy musi raportować
- TGE day-ahead/intraday: czy SaaS wymaga licencji URE
- Capacity market 2026: nowe rules dla DR aggregators
- CSRD scope: kogo dotyczy w PL (próg pracownicy/przychody)
```

**Expected behavior:**
- Research + energy sector (cross-vertical: OZE + T&D + services + regulator) → cross-check 3 AI + heart-energy context
- Pattern catches potential hallucinacje regulatory data
- Synthesis: high-confidence facts vs flagged dla EUR-Lex / URE verify

**Co pokazuje:** real value Pattern F dla regulatory research — gdzie pojedynczy model może mylić daty/procenty. Plus szeroki scope heart-energy (NIE tylko storage — pokrywa OZE/T&D/SaaS/regulator naraz).

---

## FAZA 5 — Edge cases (~10 min)

### Prompt 9: Opt-out behavior
```
BEZ COWORK: szybko podsumuj 3 główne różnice między PSE jako TSO a PGE jako utility. Max 5 zdań.
```

**Expected behavior:**
- Prefix `BEZ COWORK:` → cowork-suggest SILENT (mimo multi-entity signal)
- vb-suggest może fire (research intent), ale Claude respect user opt-out
- Solo Claude answer ~10s

**Co pokazuje:** user retains control — opt-out działa per-prompt. Kontrasty: jak ten sam prompt bez prefixu wywołałby cowork-suggest.

---

### Prompt 10: Multi-signal stress test
```
Porównaj 5 polskich konkurentów na rynku AI-powered EHR (Electronic Health Records) dla polskich szpitali. Sprawdź ich pricing pages na https://www.g2.com/categories/electronic-medical-records-emr-software i https://www.capterra.com/p/category/ehr/. Stwórz tabelę: feature set, pricing tier, target ICP, integracje z systemem P1.
```

**Expected behavior:**
- Wszystkie 4 hooki fire:
  - vb-suggest: research + HealthTech
  - devtools-suggest: 2 URLs + G2/Capterra JS-heavy domains
  - cowork-suggest: 5 entities multi-research
  - model-route: complex
- KROK -1: Claude pyta o **kombinację** — multi-research + multi-LLM verification
- Możliwe: spawn z chrome-devtools-mcp dla page scraping + cross-check

**Co pokazuje:** plugin koordynuje multiple hooks bez crash. Token-efficient browsing (devtools vs N×WebFetch).

---

## Follow-up — pytania do managera po demo

| Pytanie | Co chcesz wyciągnąć |
|---------|---------------------|
| "Które prompty czuły się najbardziej naturalne?" | Adoption barriers |
| "Czy 4 hooki naraz to za dużo noise w UI?" | Decyzja: combine hooki czy nie |
| "Czy explicit consent (KROK -1) jest blocking czy welcome?" | UX preference |
| "Kiedy ostatni raz miałbyś tak skomplikowane pytanie w realnej pracy?" | Pattern relevance check |
| "Co dodać/usunąć?" | v0.7.0 roadmap |
| "Dla których teammate'ów to **NIE** zadziała?" | Persona segmentation |

---

## Troubleshooting podczas demo

| Symptom | Quick fix |
|---------|-----------|
| Hook nie fire | `cat ~/.claude/settings.json \| grep heart-` (powinno być 4 entries) |
| `gemini` command not found | `npm install -g @google/gemini-cli` + `gemini` (browser login) |
| `codex` FAIL w doctor | User nie ma ChatGPT Plus — OK, Pattern F będzie 2-voice fallback. NIE blocker. |
| Workers crash | Sprawdź `~/.local/bin/council doctor` — który provider FAIL |
| Synthesis za długa (>200 słów) | Flag jako issue — SKILL.md mówi briefing-style |
| Claude pyta "Pattern E?" zamiast plain language | Issue dla v0.6.4 — SKILL.md powinien był to wyłapać |

---

## Quick reference — co plugin daje

| Kategoria | Skille | Kiedy auto-activate |
|-----------|--------|---------------------|
| **Decyzje** | konsultacja 3 ekspertów | "vs", "co wybrać", "build/buy" |
| **Research/facts** | cross-check 3 AI | "TAM", "regulacja", "ile wynosi" |
| **Modeling** | financial-analyst, saas-metrics-coach | "CAC", "LTV", "DCF" |
| **Writing** | board-prep, heart-pitch-deck, heart-stakeholder-update | "IC memo", "pitch deck", "update" |
| **Screening** | deal-desk, heart-dd-checklist, heart-dd-prep | "fit?", "founder", "patent" |
| **Sectors** | heart-{healthtech/academic/energy/fintech} | sector keywords w prompcie |

---

**Last update:** 2026-05-25 (v0.6.3 — plain language consent + demo prompts)
