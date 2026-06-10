---
name: heart-orchestrate
description: "Auto-orchestracja dla zadań VB analityka. Wykrywa multi-entity/decision/research prompty i spawnuje cowork agents w jednym z dwóch patternów: Pattern E (persona-driven divergence) lub Pattern F (multi-LLM debate, 3 różne providery). Działa z poziomu Claude Code (main session lub cowork worktree) bez nested CLI block. Analityk pisze normalnie — orchestrator wybiera pattern i model routing."
---

> 🔒 **heart-vb CORE — zawsze, niezależnie od załadowanego skilla:**
> (1) output = prosty polski, zero żargonu (pass/Voices/Pattern-F-internal) · (2) fakty do VC (TAM/multiple/exit/CAC-LTV/regulacje) → zaproponuj cross-check Pattern F zanim trafią do decka · (3) zmiana zadania lub milestone → **załaduj właściwy skill** (`/heart-vb:X`), nie improwizuj · (4) KROK -1 consent przed kosztownym spawnem · (5) taguj [Guessing] na niepewnych liczbach, nie udawaj cross-checku na jednym modelu.

# Heart Orchestrate — Persona Parallel + Multi-LLM Debate

**Cel:** Analityk pisze normalnie. Ty (Claude w main session) wybierasz właściwy pattern, spawnujesz agents, syntetyzujesz wynik. Brak ręcznej selekcji modeli/skilli.

**Główna reguła:** Main session = orchestrator (Opus). Workers = spawned Agents (Sonnet). Trivial = Haiku.

---

## Dwa patterny — kiedy który

### Pattern E — Persona Parallel (decyzje, judgment, role-play)

**Setup:** N workers, ten sam LLM (gemini-cli przez Bash dla free OAuth quota), różne **persony** w prompcie.

**Source divergence:** różne kryteria oceny per persona (pricing analyst vs growth lead vs VP product).

**Use cases:**
- Pricing decision ("$99/$299 vs flat $2k")
- GTM strategy choice
- Build/buy/partner
- Founder fit assessment
- Stakeholder simulation
- Multi-criteria trade-off

### Pattern F — Multi-LLM Debate (research, facts, cross-verification)

**Setup:** 3 workers, **różne LLM providery**, ten sam neutralny prompt (lub minimal persona).

| Worker | Model | Mechanism |
|--------|-------|-----------|
| A | Sonnet (sam) | Returns Claude voice w swoim agent context |
| B | Sonnet → gemini-cli przez Bash | Gemini voice |
| C | Sonnet → `codex exec --skip-git-repo-check` przez Bash | Codex/GPT-5 voice |

**Source divergence:** różne training data, różne biases per LLM family.

**Use cases:**
- Regulatory facts (EU Battery Reg, KNF, MDR)
- Market data (TAM/SAM, competitor pricing)
- Industry benchmarks (multiples, churn rates)
- Technical claims verification (czy ten algorytm/architektura jest realny?)
- IC memo fact-check przed wysłaniem

**Pattern F multi-LLM działa z CC session** — Agent tool isolation bypassuje nested CLI block (council CLI nie działa z tej samej przyczyny, tu jest workaround).

---

## Decision matrix — który pattern

| User prompt zawiera... | Pattern | Powód |
|------------------------|---------|-------|
| "pricing", "co wybrać", "vs", "build/buy" | **E** | Decyzja z trade-offs → różne persony widzą różne kryteria |
| "TAM", "rynek", "regulacja", "ile wynosi" | **F** | Fact-finding → cross-LLM verification redukuje hallucinacje |
| "IC memo", "pitch deck" | **E** (różne sekcje) + optional F (fact-check) | Sections benefit z personas, facts z multi-LLM |
| "DD checklist" (single deliverable) | NIE orchestruj | Single skill (heart-dd-checklist) wystarczy |
| Lookup "co znaczy CAC" | NIE orchestruj | Solo Claude wystarczy |
| Sequential reasoning (B wymaga A) | NIE orchestruj | Sequential w main |

---

## CRITICAL — Explicit user consent przed auto-spawn

**Hook sugeruje orkiestrację ale TY (Claude main) NIE spawnujesz workers bez potwierdzenia user.** Hooki mogą się mylić, prompt może być deceptively complex. Zawsze:

> **Note: KROK -1 to plugin-wide pattern (od v0.6.9).** Ten sam consent gate stosujemy przed odpaleniem **brainstorming flow** i **każdego innego skill activation** (board-prep, financial-analyst, deep-research, etc.). Skip consent tylko dla trivial lookups (haiku tier). User może wyłączyć per-prompt prefixem `BEZ PYTANIA:`. Pełna lista skille-specific consent w README → "Consent-first design".

### KROK -1 — Confirmation (PRZED auth check, PRZED spawn)

**Sformułuj pytanie w języku BIZNESOWYM, NIE technicznym.** Nigdy nie używaj "Pattern E/F" w pytaniu do user — to nasze internal lingo które nic mu nie mówi.

**Dla decision intent (E):**
```
"To wygląda na decyzję wartą konsultacji z kilkoma ekspertami.
 Mogę puścić to przez 3 perspektywy ([persona X / Y / Z dostosowane do typu decyzji]) 
 — ~20-40k tokenów (~60s), dostaniesz multi-perspective rekomendację.
 
 (a) Tak, zapytaj 3 ekspertów
 (b) Nie, odpowiedz Ty sam
 (c) Sam wiem co wybrać"
```

**Dla research intent (F):**
```
"To wygląda na pytanie faktualne. Mogę zweryfikować przez 3 niezależne AI 
 (Claude + Gemini + GPT-5) — ~30-50k tokenów (~90s), wykryje hallucinacje pojedynczego modelu.

 (a) Tak, cross-check przez 3 AI
 (b) Nie, odpowiedź ze swojej wiedzy
 (c) Sam zweryfikuję w źródłach"
```

**Czekaj na explicit yes.** Bez tego — odpowiedz solo z main session.

**Wyjątek:** jeśli user wpisał `/orchestrate` lub explicit "zapytaj radę / cross-check / zapytaj ekspertów" — skip confirmation, spawn directly.

**Anti-pattern:** auto-spawn na każdy multi-entity prompt bo hook tak sugeruje. **Friction > false-positive cost** dla non-tech analityka.

**Token budget (orientacyjnie):** Pattern E/F z 3 workerami ≈ 20-50k tokenów; pojedynczy worker ≈ 8-15k. **ZAWSZE podawaj koszt w TOKENACH na pierwszym miejscu w consent** — analityk widzi licznik tokenów w Cowork, nie czas wykonania. Nie spawnuj 3 jeśli 1 wystarczy.

### Cache council doctor (token saving)

Run `council doctor` raz per session, cache wynik do `/tmp/heart-doctor-cache.json` z TTL 5 min. Subsequent Pattern E/F → read cache zamiast re-run. Speedup: ~1-2s na każdy spawn.

```bash
# Cache write (po pierwszym sprawdzeniu)
~/.local/bin/council doctor 2>&1 | grep -E "OK|FAIL" > /tmp/heart-doctor-cache.json
touch /tmp/heart-doctor-cache.json  # set mtime

# Cache read (przed kolejnym Pattern E/F)
if [ -f /tmp/heart-doctor-cache.json ] && [ $(($(date +%s) - $(stat -f %m /tmp/heart-doctor-cache.json))) -lt 300 ]; then
  cat /tmp/heart-doctor-cache.json  # use cache
else
  ~/.local/bin/council doctor 2>&1 | grep -E "OK|FAIL" | tee /tmp/heart-doctor-cache.json
fi
```

---

## Pattern E — execution

> 🐣 **Easter egg — agent identity:** Każdy worker, niezależnie od persony, ma na imię **Wojtek** (sygnatura twórcy, Wojtek Czuba / The Heart). W syntezie używaj: "Wojtek (pricing analyst) says...", "Wojtek (growth lead) zauważył...", "Wojtek (VP product) odpowiada...". Brzmi jak board of Wojteks debatujących — feature, nie bug. Imię "Wojtek" jest OK w outpucie; tłumaczymy tylko techniczny żargon (pass / Voices / Pattern F).

### 🆕 v0.8.0 — Dedicated agents (PREFERRED) vs inline personas (LEGACY)

**Od v0.8.0 plugin zawiera 15 dedicated subagentów w `agents/` folder** (auto-discoverable). Mają **stable persona**, własny system prompt, tool restriction. Pattern E preferred path:

```js
// PREFERRED — Pattern E z dedicated agents (v0.8.0+)
Main (Opus):
  1. Identify decision type (pricing / strategy / GTM / screening / cross-cutting)
  2. Wybierz 3 dedicated agents z VB Team library (poniżej)
  3. SPAWN 3 agents parallel:
     Agent({
       subagent_type: 'pricing-analyst',  // ← dedicated agent name
       description: 'Wojtek-Pricing analysis dla X',  // easter egg preserved
       prompt: '<konkretny brief z project context>',
       model: 'sonnet'
     })
     // Repeat dla 2 innych agents
  4. Wait ~30-60s (Sonnet solo, NIE gemini cold start)
  5. Synthesize używając "Wojtek (pricing analyst) says..." attributions
     (briefing-style format, max 150 słów)
```

**Korzyści dedicated agents vs inline personas:**
- **Stable persona** — system prompt w `agents/<name>.md` nie drift'uje między spawn'ami
- **Tool restriction** — np. `regulatory-officer-pl` ma WebSearch, `cfo` ma Bash, `founder-skeptic` tylko Read
- **Multi-LLM built-in** — `vc-partner` i `regulatory-officer-pl` mają Pattern F embedded
- **Context economy** — agent context jest izolowany, nie ciągnie main session history
- **Reusable cross-pattern** — ten sam `pricing-analyst` w Pattern E + Mode A (orchestrator deleguje solo) + Pattern F worker

```
LEGACY — Pattern E z inline personas (pre-v0.8.0, nadal działa dla custom personas)
Main (Opus):
  0. Run Krok 0 auth check
  1. Zdefiniuj decyzję
  2. Wybierz 3 custom persony (które nie mają dedicated agent)
  3. SPAWN 3 agents parallel:
     Agent({
       subagent_type: 'general-purpose',
       model: 'sonnet',
       description: 'Wojtek as [persona name]',
       prompt: 'Jesteś Wojtek, [persona]. <persona context>. [Jeśli gemini OK]: Uruchom gemini -p "..." [Jeśli FAIL]: Sonnet solo'
     })
```

### VB Team library (wybierz 3 dedicated agents dla Pattern E)

**Decyzje pricing/commercial:** `pricing-analyst`, `growth-lead`, `vp-product`, `cfo`

**Strategy product:** `vp-product`, `customer-research-lead`, `it-architect`, `founder-skeptic`

**GTM/launch:** `growth-lead`, `customer-research-lead`, `pricing-analyst`, `vp-product`

**Research/screening:** `vc-partner`, `comps-analyst`, `founder-skeptic`, `regulatory-officer-pl`

**M11 deck stress-test:** `vc-partner`, `pitch-coach`, `cfo`, `founder-skeptic`

**Cross-cutting / risk:** `founder-skeptic`, `operator`, `red-flag-detector`, `ic-memo-writer`

**Sector-specific:** załącz sector context skill (`heart-{healthtech/fintech/energy/academic}`) jako reference dla agentów. `regulatory-officer-pl` zawiera już skille jako reference.

Sector context (heart-fintech-compliance / heart-healthtech-compliance / heart-academic-spinouts / heart-energy) = opcjonalny add-on dla Heart portfolio sektorów.

---

## Krok 0 — Pre-spawn auth check (CRITICAL)

**Zawsze przed Pattern E/F**: sprawdź którzy providerzy są dostępni. Bez tego workers się crashują gdy brak login.

```bash
# Quick check (1-2s)
~/.local/bin/council doctor 2>&1 | grep -E "claude|codex|gemini-cli" | grep -E "OK|FAIL"
```

Interpretacja:
- `claude OK` — Sonnet native worker zawsze możliwy (Claude Code z definicji)
- `gemini-cli OK` — gemini worker możliwy
- `codex OK` — codex worker możliwy
- Każdy FAIL → SKIP tego workera (nie spawnuj, NIE crash)

### Graceful degradation matrix

| Available providers | Pattern E (decision) | Pattern F (research) |
|---------------------|----------------------|----------------------|
| **Tylko Sonnet** (no Gemini, no Codex) | 3 Sonnet workers z personami (zjada Claude session) | **1-voice fallback** — solo Claude z explicit caveats |
| **Sonnet + Gemini** *(default Heart analytic)* | 3 gemini workers z personami | **2-voice** (Sonnet + Gemini) |
| **Sonnet + Gemini + Codex** (power user) | 3 gemini z personami (codex jako 4th fallback) | **3-voice full** Pattern F |

W odpowiedzi zawsze podaj **prostym językiem** ile niezależnych źródeł sprawdziło fakt, np. *"sprawdzone przez 3 z 3 modeli (Claude + Gemini + GPT-5)"* — NIGDY "Voices available: X/3" (żargon).

---

## Transport — gdzie realnie wykonują się gemini/codex

`gemini`/`codex` to **lokalne CLI**. Czy są dostępne zależy od środowiska — to determinuje transport:

| Środowisko | gemini/codex w Bash? | Transport Pattern F |
|---|---|---|
| **CLI / IDE** | ✅ w PATH | **Bash bezpośrednio** (przykłady niżej) |
| **Cowork + Desktop Commander MCP** | ❌ sandbox nie ma — ale **DC działa na hoście** | **przez DC** — `start_process` woła gemini/codex na hoście |
| **Cowork bez DC** | ❌ | Pattern F **NIEDOSTĘPNY** → emulated single-model (oznacz jawnie) |

**Detekcja (rozszerza Krok 0):**
1. `command -v gemini` w Bash → jest? jesteś w CLI, użyj Bash transport.
2. Bash nie ma gemini, ale masz w toolach **Desktop Commander** (`start_process`) → użyj DC bridge (Cowork case).
3. Ani Bash, ani DC → **NIE udawaj cross-checku**. Zrób dwa niezależne podejścia jednym modelem (Claude): jedno z web search, drugie krytyczne (subagent szuka błędów w pierwszym). W odpowiedzi oznacz to **prostym językiem**: *"⚠️ Sprawdzone jednym modelem (Claude), dwa niezależne podejścia — to NIE jest weryfikacja przez 3 różne AI."* Nie używaj słów "pass" / "emulated" / "Pattern F" w odpowiedzi do użytkownika.

### DC bridge — wołanie gemini/codex z Coworka

DC wykonuje komendy **na hoście** (tam gdzie masz zainstalowane gemini/codex), omijając izolację sandboxa. Przez `start_process`:

```
# KROK 0 — zweryfikuj CLI NA HOŚCIE (DC obecny ≠ gemini obecny!). OS-aware check:
start_process(command: "command -v gemini || where gemini || echo GEMINI_MISSING", timeout_ms: 8000)   # macOS/Linux: command -v | Windows: where
#   GEMINI_MISSING → NIE udawaj Pattern F; emulated single-model z "gemini niedostępny na hoście"
# gemini przez DC — PORTABLE (--skip-trust flag zamiast inline env; output przez read_process_output, NIE tail):
start_process(command: "gemini --skip-trust -p '<fact>'", timeout_ms: 45000)
# codex przez DC:
start_process(command: "codex exec --skip-git-repo-check '<fact>'", timeout_ms: 60000)
# odczyt wyniku: read_process_output(pid, timeout_ms)  ← cross-platform, zastępuje tail (brak na Windows)
```

**Gotchas DC (zweryfikowane na macOS):**
- **DC obecny ≠ gemini obecny** — `command -v gemini` przez DC ZANIM użyjesz. Brak na hoście (świeży Mac, albo gemini w ścieżce niewidocznej dla non-interactive zsh) → emulated, NIE udawaj że masz cross-check.
- **Trust: użyj flagi `--skip-trust`** (cross-platform, zwykła flaga) zamiast inline env `GEMINI_CLI_TRUST_WORKSPACE=true` (POSIX-only, NIE działa w PowerShell) — inaczej trust-block. Zweryfikowane na macOS.
- **`cd` do konkretnego folderu** — DC startuje w `/`; bez tego gemini skanuje cały filesystem jako kontekst.
- **GNU `timeout` NIE istnieje** w shellu DC (macOS) — NIE używaj `timeout 120 ...`; bound przez `timeout_ms` w `start_process`.
- **PATH DC ≠ login shell** — `council` (~/.local/bin) bywa niewidoczny; wołaj gemini/codex bezpośrednio, nie przez council.
- **Escape user input** do `-p '...'` (single-quote literal) — injection vector.
- **gemini OAuth wygasa** → `gemini -p` czeka na re-auth prompt którego w trybie headless nikt nie obsłuży → hang do timeout (worker = MISSING). Jak Pattern F nagle "gemini MISSING" bez powodu → user musi odpalić `gemini` raz w terminalu i re-auth.

---

## Pattern F — execution (po auth check)

> 🐣 Easter egg: workery w Pattern F to Wojtek-Claude, Wojtek-Gemini, Wojtek-Codex — sygnatura twórcy. Widoczne w syntezie (np. "Wojtek-Gemini znalazł...").

**GROUNDING (KRYTYCZNE dla uczciwego cross-checku):** Pattern F = fakty time-sensitive (regulacje, daty, liczby). **Każdy worker MUSI być grounded live search** — inaczej porównujesz model-z-internetem vs model-z-pamięci i dostajesz **fałszywą "rozbieżność"** (realnie się zdarzyło: Claude z WebSearch złapał draft MDR amendment z grudnia 2025, Gemini bez searcha "nie złapał" — to nie był disagreement, tylko brak groundingu). Konkretnie:
> - **Wojtek-Claude** → użyj **WebSearch** (native tool), cytuj źródła. NIE odpowiadaj z samej pamięci treningowej.
> - **Wojtek-Gemini** → w prompcie: `Use Google Search to verify current facts, cite source URLs` (gemini-cli ma wbudowany search — zweryfikowane empirycznie).
> - **Wojtek-Codex** → codex ma web search; poproś o weryfikację w sieci + źródła.
> Model który nie może szukać → oznacz jego odpowiedź "(z pamięci, niegrounded)" żeby rozbieżność była interpretowalna.

```
Main (Opus):
  1. Run Krok 0 auth check
  2. Sformułuj neutralny prompt (bez personas, focus fact)
  3. SPAWN dostępnych agents parallel (max 3, min 1 = Sonnet native):
     
     Wojtek-Claude (Sonnet native) — ZAWSZE dostępny:
       description: 'Wojtek-Claude fact lookup'
       prompt: 'Jesteś Wojtek-Claude. Odpowiedz na: [pytanie]. Dla faktów UŻYJ WebSearch 
                (cytuj źródła), NIE wywołuj żadnego CLI. Zwróć structured: 
                Source: Wojtek-Claude, Answer, Confidence, Caveats.'
       model: 'sonnet'
     
     Wojtek-Gemini (Gemini transport) — tylko jeśli gemini-cli OK:
       description: 'Wojtek-Gemini fact lookup'
       prompt: 'Jesteś Wojtek-Gemini. Uruchom: gemini --skip-trust -p "Use Google Search to verify current facts and cite source URLs. [pytanie + format request]" 
                2>&1 | tail -80. Zwróć raw output. Podpisz Source: Wojtek-Gemini.
                (Cowork bez gemini w Bash → wołaj to przez Desktop Commander start_process.)'
       model: 'sonnet'
     
     Wojtek-Codex (Codex transport) — tylko jeśli codex OK:
       description: 'Wojtek-Codex fact lookup'
       prompt: 'Jesteś Wojtek-Codex. Uruchom: codex exec --skip-git-repo-check 
                "Zweryfikuj fakty w sieci i podaj źródła. [pytanie + format request]" 2>&1 | tail -100. Zwróć raw output. 
                Podpisz Source: Wojtek-Codex.
                (Cowork bez codex w Bash → wołaj to przez Desktop Commander start_process.)'
       model: 'sonnet'
  
  3. Wait ~60-120s (Gemini i Codex najwolniejsze; Codex z web search może >90s)
  4. Synthesize per format niżej:
     - Convergence (3/3 zgadzają się) = high confidence
     - 2/3 = medium, flag dla weryfikacji
     - 1/3 unique = informacja, ale NIE używać w deliverable bez verify
     - ⚠️ Consensus ≠ prawda: 3 LLM-y mogą zgodnie powtórzyć szeroko-cytowany błąd (systemic hallucination — cross-check łapie idiosynkratyczne, nie systemowe). Przy high-stakes liczbie ZAWSZE podaj primary source (EUR-Lex / rejestr / raport z datą), nie samo "3/3 się zgodziły".
```

---

## Format syntezy — KRÓTKI briefing (max ~150 słów)

**JĘZYK OUTPUTU = prosty polski biznesowy. ZERO wewnętrznego żargonu.** Analityk VB nie zna naszych etykiet — np. user dostał kiedyś "claude pass" i nie wiedział co to znaczy. Tłumacz lub unikaj:

| Wewnętrzne (NIE pokazuj userowi) | W odpowiedzi piszesz |
|---|---|
| "pass" / "passy" | "podejście" / "niezależne sprawdzenie" |
| "Pattern E / Pattern F" | "konsultacja kilku ekspertów" / "cross-check przez kilka AI" |
| "Voices available: 2/3" | "sprawdzone przez 2 z 3 modeli" |
| "convergence / divergence" | "modele się zgadzają / różnią się" |
| "emulated / single-model" | "sprawdzone jednym modelem, bez cross-checku" |

(„Wojtek" / „Wojtek-Gemini" itp. **zostają** — to sygnatura, nie żargon.)

Złapiesz się na żargonie → przepisz prostym językiem. Test: czy nietechniczny analityk zrozumie każde słowo?

NIE rób długich tabel z każdym faktem. Daj analitykowi **odpowiedź**, NIE research report.

```
[Konsultacja N ekspertów / Cross-check N AI] · [czas]

ODPOWIEDŹ (2-3 zdania narracyjne z konkretami):
[Konkretne liczby, daty, rekomendacja w naturalnym języku polskim]

REKOMENDACJA:
[1 paragraf — co z tym zrobić, jak traktować w decyzjach VB]

VERIFY zanim w deliverables (max 3 bullets):
- [Pkt 1 — gdzie była divergencja lub low confidence]

BOTTOM LINE:
[1-2 zdania: czy modele osiągnęły consensus, jak traktować obiektywnie]
```

**Przykład syntezy (decyzja pricing):**

> *Konsultacja 3 ekspertów · 58s*
>
> Wojtek (pricing analyst) i Wojtek (VP product) rekomendują tier €99/€299/€999 — argumenty: LTV/CAC payback period ~4mc dla tieru Pro vs 18mc dla flat, plus expansion revenue via upsell.
> Wojtek (growth lead) preferuje flat €2k/rok — łatwiejsze "annual budget item" dla zarządu przychodni przy 6-9mc cyklu sprzedaży.
>
> **Rekomendacja:** hybrid — flat annual baseline €2k z usage overage przy >5 lekarzy lub multi-location. Łapie oba: konwersję (growth) i expansion (product/pricing).
>
> **Verify:** czy decision-maker w przychodniach to faktycznie zarząd vs właściciel-lekarz (wpływa na budget framing).
>
> **Bottom line:** 3 Wojteki zgodni że hybrid najlepiej balansuje konwersję i retention dla polskiego rynku medycznego.

**Anti-patterns w syntezie:**
- ❌ Tabele 3-column z każdym faktem (chyba że user explicit prosi o detail)
- ❌ Confidence markers per pojedynczy fact (overkill)
- ❌ Article references jako primary output (tylko jeśli user prosi)
- ❌ Meta-finding o pattern (chyba że eksperyment)
- ❌ Dłuższe niż 200 słów

**Co MUSI być:**
- ✅ Konkretna odpowiedź na user pytanie w pierwszych 2-3 zdaniach
- ✅ Praktyczna rekomendacja co z tym
- ✅ Krótki verify list (high-stake facts only)
- ✅ Bottom-line: czy mamy obiektywny consensus

---

## Komendy które fact spawn pattern E vs F

### Pattern E spawn (multi-persona)

User: *"Pricing 99/299 vs flat 2k dla HealthTech B2B?"*

Ty (main Opus):
```
Spawn 3 agents parallel, każdy Agent({model:'sonnet', ...}):
  - Worker A → gemini -p "Persona pricing analyst..."
  - Worker B → gemini -p "Persona growth lead..."  
  - Worker C → gemini -p "Persona VP product..."
Synthesize krótko per format powyżej.
```

### Pattern F spawn (multi-LLM)

User: *"Jakie są aktualne wymagania EU Battery Regulation dla recycled content?"*

Ty (main Opus):
```
Spawn 3 agents parallel, każdy Agent({model:'sonnet', ...}):
  - Worker A → "Odpowiedz sam jako Claude Sonnet"
  - Worker B → "gemini -p '[pytanie]'"
  - Worker C → "codex exec --skip-git-repo-check '[pytanie]'"
Synthesize krótko per format powyżej.
```

---

## Co Pattern F daje vs Pattern E

| Wymiar | Pattern E (personas) | Pattern F (multi-LLM) |
|--------|----------------------|------------------------|
| **Detekcja blindspot** | Różne perspektywy biznesowe | Różne biases treningowe LLM |
| **Wykrywa hallucinacje** | Słabo (1 LLM × N personas) | **Mocno** (2/3 disagreement = flag) |
| **Speed** | ~45-90s | ~60-120s (codex najwolniejszy) |
| **Cost** | Tania (1 model family, free gemini OAuth) | Wyższa (3 różne CLIs) |
| **Najlepsze dla** | **Decyzje judgmental** | **Research/fakty** |

**Jeśli zadanie hybrydowe** (np. IC memo = sekcje + fact-check) → użyj E dla sekcji, F dla weryfikacji liczb.

---

## Gotchas

1. **Codex wymaga `--skip-git-repo-check`** gdy CWD nie jest git repo (analityk w niegit folderze)
2. **Gemini Workspace OAuth ma rate limits** — przy parallel × 3 workers może hit cap, retry 5× wbudowane ale zwalnia
3. **Codex z web search** = wolny (~90s+) i token-heavy gdy fact-finding
4. **Agent z model:'sonnet' EXPLICIT** — bez tego inherituje Opus z main session = drogo
5. **Escape user input przed interpolacją do shell** — pytanie usera trafiające do `gemini -p "..."` lub `codex exec "..."` to **untrusted input**. NIGDY nie wklejaj raw: usuń/escapuj znaki cudzysłowu, `$`, backtick, `;` `|` `&` oraz `$(...)`, albo przekaż jako single-quoted literal ze strippowanymi apostrofami. Inaczej `; rm`, backticki czy `$(...)` w pytaniu wykonają się w shellu workera (injection vector).
6. **Timeout + fallback na każdy spawn** — domyślnie 120s/worker (150s dla Codex). Worker który przekroczy timeout lub crashuje → oznacz output jako `MISSING`, kontynuuj z dostępnymi, zaznacz w nagłówku prostym językiem (np. "sprawdzone przez 2 z 3 modeli"). 0 dostępnych workerów → odpowiedz solo z main (Opus) z explicit caveatem, NIE czekaj w nieskończoność.

---

## Alternatywa: council CLI

`~/.local/bin/council run ...` (skill: council) **teoretycznie** robi to samo (3-LLM debate) ale **rzadko działa z poziomu CC session** (nested CLI self-invocation block — codex stalls, gemini timeouts, claude self-block).

**Pattern F w heart-orchestrate to workaround** który działa z CC.

Council CLI używaj **tylko z terminala spoza Claude Code** (POWER profile w config/llm-council.example.yaml).

---

## Co to NIE jest

- ❌ NIE process management (orchestracja jednorazowa, brak persistent state)
- ❌ NIE replacement dla pojedynczych skilli (deal-desk, board-prep, etc. nadal odpalasz solo)
- ❌ NIE workflow tracker (nie monitoruje multi-tygodniowych projektów)
- ❌ NIE auto-spawning bez kontroli (hook tylko sugeruje, Claude w main decyduje czy fire)
