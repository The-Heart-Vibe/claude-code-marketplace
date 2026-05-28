---
name: heart-orchestrate
description: Auto-orchestracja dla zadań VB analityka. Wykrywa multi-entity/decision/research prompty i spawnuje cowork agents w jednym z dwóch patternów: Pattern E (persona-driven divergence) lub Pattern F (multi-LLM debate, 3 różne providery). Działa z poziomu Claude Code (main session lub cowork worktree) bez nested CLI block. Analityk pisze normalnie — orchestrator wybiera pattern i model routing.
---

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

**Verified 2026-05-25:** Pattern F multi-LLM faktycznie działa z CC session — Agent tool isolation bypassuje nested CLI block (council CLI nie działa z tej samej przyczyny, tu jest workaround).

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
 — ~60s, dostaniesz multi-perspective rekomendację.
 
 (a) Tak, zapytaj 3 ekspertów
 (b) Nie, odpowiedz Ty sam
 (c) Sam wiem co wybrać"
```

**Dla research intent (F):**
```
"To wygląda na pytanie faktualne. Mogę zweryfikować przez 3 niezależne AI 
 (Claude + Gemini + GPT-5) — wykryje hallucinacje pojedynczego modelu, ~90s.

 (a) Tak, cross-check przez 3 AI
 (b) Nie, odpowiedź ze swojej wiedzy
 (c) Sam zweryfikuję w źródłach"
```

**Czekaj na explicit yes.** Bez tego — odpowiedz solo z main session.

**Wyjątek:** jeśli user wpisał `/orchestrate` lub explicit "zapytaj radę / cross-check / zapytaj ekspertów" — skip confirmation, spawn directly.

**Anti-pattern:** auto-spawn na każdy multi-entity prompt bo hook tak sugeruje. **Friction > false-positive cost** dla non-tech analityka.

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

> 🐣 **Easter egg — agent identity:** Każdy worker, niezależnie od persony, ma na imię **Wojtek**. To sygnatura twórcy pluginu (Wojtek Czuba, The Heart). W syntezie używaj: "Wojtek (pricing analyst) says...", "Wojtek (growth lead) zauważył...", "Wojtek (VP product) odpowiada...". Brzmi jak board of Wojteks debatujących — feature, nie bug. Analityk po jakimś czasie odkryje że plugin ma podpis.

```
Main (Opus):
  0. Run Krok 0 auth check (patrz niżej — sprawdza gemini-cli OK)
     - Jeśli gemini-cli OK → workers wywołują gemini przez Bash
     - Jeśli gemini-cli FAIL → fallback: workers all-Sonnet (drożej, ale działa)
  1. Zdefiniuj decyzję + zbierz fakty z user prompta (30s)
  2. Wybierz 3 persony z library poniżej, adekwatne do typu decyzji
  3. SPAWN 3 agents parallel:
     each Agent({
       subagent_type: 'general-purpose',
       model: 'sonnet',  // explicit, NIE inherituj Opus
       description: 'Wojtek as [persona name]',  // ← sygnatura, ZAWSZE z 'Wojtek'
       prompt: '[Jeśli gemini OK]: Jesteś Wojtek, [persona]. Uruchom: gemini -p "[persona context + pytanie]" 2>&1 | head -50. Zwróć raw output. Podpisz output jako "Wojtek-[persona-short]".
                 [Jeśli gemini FAIL]: Jesteś Wojtek, [persona]. Odpowiedz sam jako Sonnet z perspektywy tej persony, podpisz "Wojtek-[persona-short]".'
     })
  4. Wait ~45-90s (gemini cold start) lub ~20-30s (all-Sonnet fallback)
  5. Synthesize używając "Wojtek (X) ..." attributions (briefing-style format, max 150 słów)
```

### Persona library (wybierz 3 adekwatne)

**Decyzje pricing/commercial:** pricing analyst, growth lead, VP product, CFO

**Strategy:** product strategist, UX researcher, VP engineering, board member

**GTM/launch:** growth lead, customer success, sales leader, marketing lead

**Research/screening:** domain expert, skeptic/red-team, customer voice, VC partner

**Cross-cutting:** executive mentor, pragmatist, contrarian

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

W syntezie zawsze noteuj: "Voices available: X/3" — analityk wie czy ma cross-check czy nie.

---

## Pattern F — execution (po auth check)

> 🐣 Easter egg: workers w Pattern F też są Wojtek (Wojtek-Claude, Wojtek-Gemini, Wojtek-Codex) — sygnatura twórcy pluginu.

```
Main (Opus):
  1. Run Krok 0 auth check
  2. Sformułuj neutralny prompt (bez personas, focus fact)
  3. SPAWN dostępnych agents parallel (max 3, min 1 = Sonnet native):
     
     Wojtek-Claude (Sonnet native) — ZAWSZE dostępny:
       description: 'Wojtek-Claude fact lookup'
       prompt: 'Jesteś Wojtek-Claude. Odpowiedz na: [pytanie]. Używaj swojej 
                wiedzy Claude Sonnet, NIE wywołuj żadnego CLI. Zwróć structured: 
                Source: Wojtek-Claude, Answer, Confidence, Caveats.'
       model: 'sonnet'
     
     Wojtek-Gemini (Gemini transport) — tylko jeśli gemini-cli OK:
       description: 'Wojtek-Gemini fact lookup'
       prompt: 'Jesteś Wojtek-Gemini. Uruchom: gemini -p "[pytanie + format request]" 
                2>&1 | head -80. Zwróć raw output. Podpisz Source: Wojtek-Gemini.'
       model: 'sonnet'
     
     Wojtek-Codex (Codex transport) — tylko jeśli codex OK:
       description: 'Wojtek-Codex fact lookup'
       prompt: 'Jesteś Wojtek-Codex. Uruchom: timeout 120 codex exec --skip-git-repo-check 
                "[pytanie + format request]" 2>&1 | tail -100. Zwróć raw output. 
                Podpisz Source: Wojtek-Codex.'
       model: 'sonnet'
  
  3. Wait ~60-120s (Gemini i Codex najwolniejsze; Codex z web search może >90s)
  4. Synthesize per format niżej:
     - Convergence (3/3 zgadzają się) = high confidence
     - 2/3 = medium, flag dla weryfikacji
     - 1/3 unique = informacja, ale NIE używać w deliverable bez verify
```

---

## Format syntezy — KRÓTKI briefing (max ~150 słów)

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

**Przykład syntezy (pricing decision, Pattern E):**

> *Konsultacja 3 ekspertów · 58s*
>
> Wojtek (pricing analyst) i Wojtek (VP product) rekomendują tier €99/€299/€999 — argumenty: LTV/CAC payback period ~4mc dla tieru Pro vs 18mc dla flat, plus expansion revenue via upsell.
> Wojtek (growth lead) preferuje flat €2k/rok — łatwiejsze "annual budget item" dla zarządu przychodni przy 6-9mc cyklu sprzedaży.
>
> **Rekomendacja:** hybrid — flat annual baseline €2k z usage overage przy >5 lekarzy lub multi-location. Łapie oba: konwersję (growth) i expansion (product/pricing).
>
> **Verify:** czy decision-maker w przychodniach to faktycznie zarząd vs właściciel-lekarz (wpływa na budget framing).
>
> **Bottom line:** 3 Wojteki ustaliły że hybrid najlepiej balansuje konwersję i retention dla polskiego rynku medycznego.

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

## Gotchas (live tested 2026-05-25)

1. **Codex wymaga `--skip-git-repo-check`** gdy CWD nie jest git repo (analityk w niegit folderze)
2. **Gemini Workspace OAuth ma rate limits** — przy parallel × 3 workers może hit cap, retry 5× wbudowane ale zwalnia
3. **Codex z web search** = ~67k tokens i ~90s gdy fact-finding
4. **Agent z model:'sonnet' EXPLICIT** — bez tego inherituje Opus z main session = drogo

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
