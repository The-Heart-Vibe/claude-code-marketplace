# Onboarding: Venture Builder toolkit w Claude Code (The Heart)

Przewodnik dla analityków i konsultantów VB. **Jedna instalacja, kompletny VB stack.**

**Czas:** 20-30 minut (głównie czekanie na install i auth providerów).

---

## Co dostajesz po install

Jeden plugin `heart-vb` zawiera **30 skilli** w 8 kategoriach:

| Kategoria | Skille | Do czego |
|-----------|--------|----------|
| **council** ⭐ | council (multi-LLM debate) + 13 subagentów | Każda strategiczna decyzja |
| **self-improving** | si:remember, si:review, si:extract, si:promote, si:status, self-improving-agent | Agent uczy się z MEMORY.md — promote patterns, extract skills |
| **vb-research** | deep-research, market-research, exa-search | Discovery, TAM/SAM/SOM, sizing |
| **vb-product** | product-discovery, competitive-teardown, experiment-designer, ux-researcher-designer, product-strategist | Validation, persona, JTBD, smoke tests |
| **vb-finance** | financial-analyst, saas-metrics-coach | Unit economics, P&L, KPIs, projekcje |
| **vb-commercial** | pricing-strategist, deal-desk, commercial-forecaster, channel-economics | Pricing, deal screening, GTM forecasts |
| **vb-comms** | board-prep (IC memo), stress-test, hard-call, investor-materials, investor-outreach | IC memo, pitch deck, investor comms |
| **heart-custom** | heart-fintech-compliance, heart-healthtech-compliance, heart-realestate-context, heart-martech-ecosystem | Sector context dla portfolio (KNF/MDR/RODO/polskie specyfiki) |

➡️ Pełna mapa skilli per faza pracy: [venture-builder.md](venture-builder.md)

---

## 1. Załóż konta jeśli nie masz

| Konto | Po co | Link |
|-------|-------|------|
| Claude Code (Pro/Max) | Główny interfejs | https://claude.ai/code |
| ChatGPT Plus | Council provider `codex` (token-saving) | https://chatgpt.com |
| Google Workspace (@theheart.tech) | Council provider `gemini-cli` (token-saving) | (już masz) |

> ChatGPT Plus i Workspace **nie są wymagane** dla samych skilli. Wymagane tylko żeby `/council` używał alternatywnych providerów zamiast zjadać Twoją Claude Code session.

---

## 2. Install (~3 min)

W Claude Code:

```
/plugin marketplace add The-Heart-Vibe/claude-code-marketplace
/plugin install heart-vb@the-heart-vibe
```

Installer (run automatically) wykona w terminalu:
1. Instaluje `uv` (Python package manager) jeśli brak
2. Sprawdza Node.js
3. Instaluje `@google/gemini-cli` globalnie jeśli brak
4. Tworzy venv w `~/tools/council-env`
5. Instaluje `the-llm-council[gemini]>=0.7.16`
6. Tworzy wrapper `~/.local/bin/council`
7. Kopiuje config template
8. **Pyta: "Zainstalować Venture Builder hook? [y/N]"** → **odpowiedz `y`**
9. Odpala `council doctor` — pokazuje status providerów

Jeśli installer się nie uruchomił automatycznie:
```bash
bash <(curl -s https://raw.githubusercontent.com/The-Heart-Vibe/claude-code-marketplace/main/plugins/heart-vb/install.sh)
```

---

## 3. Auth providerów dla council (~5 min)

### Dwa profile — analityk vs tech

Council używa różnych LLM jako "rady" debaty. Realnie z poziomu Claude Code session:

| Provider | Profil ANALITYK / KONSULTANT | Profil TECH TEAM |
|----------|------------------------------|--------------------|
| `gemini-cli` | ✅ wymagany (login: `gemini`) | ✅ wymagany |
| `codex` | ⏸️ opcjonalny (wymaga ChatGPT Plus) | ✅ rekomendowany (`codex login`) |
| `claude` | ❌ nie działa z CC session | ❌ nie działa z CC session |

**Analityk bez ChatGPT Plus:** council degrade'uje się do 1-LLM (gemini) zamiast pełnej rady. To nadal **przydatne** — Gemini ma największy token pool przez Workspace OAuth, a inne skille (board-prep, competitive-teardown, sector contexts) działają niezależnie od council. Nie musisz kupować ChatGPT Plus tylko dla council.

**Tech team z Codex:** pełna 2-LLM debate (gemini vs gpt-5) — wykryta różnica zdań to często najcenniejszy sygnał.

### Setup

Otwórz terminal i odpal:

```bash
council doctor
```

Jeśli któryś **wymagany** dla Twojego profilu `FAIL`:

| Provider | Komenda | Co da |
|----------|---------|-------|
| `gemini-cli` FAIL | `gemini` (otworzy przeglądarkę → OAuth Google Workspace) | Council używa Gemini |
| `codex` FAIL (tech) | `codex login` (wymaga ChatGPT Plus/Pro) | Council używa GPT-5 |
| `claude` FAIL | Normal jeśli odpalasz z CC session | Self-invocation block — działa tylko z terminala spoza CC |

### Po setupie — sprawdź config

Plik `~/.config/llm-council/config.yaml` ma 3 profile (odkomentuj swój):
- ANALITYK (domyślnie aktywny): `[gemini-cli]` solo
- TECH TEAM: `[gemini-cli, codex]`
- POWER (terminal-only): `[gemini-cli, codex, claude]`

Edytuj plik żeby odkomentować właściwy profil dla siebie.

---

## 4. Jak to faktycznie używać

### Tryb domyślny — z hookiem (rekomendowany)

Po prostu **pisz normalnie** do Claude. Hook wykrywa intent i Claude sugeruje właściwy skill:

> *"To wygląda na zadanie typu **modeling** — proponuję użyć **financial-analyst** lub **saas-metrics-coach**. Wolisz tak, czy odpowiedzieć od razu?"*

### Tabela co fires na co

| Twoja wiadomość | Hook intent | Sugerowany skill |
|------------------|-------------|-------------------|
| "cześć, jak się masz?" | ❌ nie fires | – |
| "Zbadaj TAM dla AML SaaS w CEE banking" | research | deep-research / market-research / exa-search |
| "Zbuduj unit econ MarTech: ARPU €49, CAC €600" | modeling | financial-analyst / saas-metrics-coach |
| "Napisz IC memo dla projektu X" | writing | board-prep / investor-materials |
| "Pricing $99/$299/$999 vs flat $2k — co wybrać?" | decision + pricing | /council Tier L + pricing-strategist |
| "Zaprojektuj fake door experiment dla brokerów RE" | validation | experiment-designer / ux-researcher-designer |
| "Profesor z patentem — fit dla nas?" | screening | deal-desk + heart-custom contexts |
| "Pricing FinTech B2B SaaS dla mid-market PL banków" | decision + pricing + sector | council + pricing-strategist + heart-fintech-compliance |

### Skip hook na konkretnej wiadomości

```
BEZ COUNCIL: szybko porównaj te 2 vendory
```

### Manualne wywołanie konkretnego skilla

Skille są auto-discovery przez Claude, ale możesz też nazwać explicit:

```
Użyj saas-metrics-coach: ARPU €49/mo, GM 78%, CAC €600, monthly churn 4% — pokaż LTV i payback.

Użyj heart-fintech-compliance + council: pricing dla AML monitoring SaaS dla mid-market PL banków.

/si:review              # przejrzyj MEMORY.md, pokaż promotion candidates
/si:status              # memory health dashboard
```

---

## 5. Self-improving agent — używaj systematycznie

Plugin zawiera `/si:` commands które robią agent samodoskonalącym:

- **`/si:remember <wiedza>`** — zapisz wprost do auto-memory. Używaj gdy uczy się ważnej rzeczy o kliencie/branży
- **`/si:review`** — raz na 1-2 tygodnie. Pokazuje co warto promote z auto-memory do trwałych rules
- **`/si:promote <pattern>`** — przenieś learning z MEMORY.md → CLAUDE.md (trwałe)
- **`/si:extract <pattern>`** — przekształć recurring pattern w nowy reusable skill
- **`/si:status`** — health dashboard auto-memory

**Praktyka:** kończ tydzień przez `/si:review` i `/si:promote` najbardziej powtarzających się wzorców. Po miesiącu Twoje CLAUDE.md staje się żywym playbookiem.

---

## 6. Co rób / czego nie rób

### ✅ Rób

- **Pisz konkretnie z kontekstem** — "Pricing FinTech B2B SaaS, ICP banki PL, target ARR €500k/24mc" jest 10× lepsze niż "pomóż z pricingiem"
- **Dołączaj artefakty przez `--files`** — masz brief? Persony? Wrzuć przez `--files brief.md,personas.md` (limit: 50KB/plik, 200KB łącznie)
- **Sprawdź `council doctor`** co tydzień — providerzy mogą wymagać re-login OAuth
- **Zapisuj wyniki w projekcie** (`decisions/2026-05-pricing-decision.md`) — następna sesja zaczyna z `--files <previous>`
- **Słuchaj hooka** — jeśli sugeruje skill X, zwykle ma rację
- **Używaj `/si:` regularnie** — bez tego agent się nie uczy

### ❌ Nie rób

- **Nie pytaj council o trywialne rzeczy** — "co znaczy CAC" → odpowie Claude solo
- **Nie kopiuj output 1:1 do dokumentów** — to syntheza, nie deliverable. Przetwórz, dodaj kontekst Heart, zweryfikuj liczby
- **Nie odpalaj 5 rad council pod rząd** — limity providerów się skończą. Z 1-2 odpowiedzi zwykle wynika dalsze pytania
- **Nie ufaj ślepo w sprawach regulacyjnych** — KNF/MDR/RODO modele mogą podawać przestarzałe info. Zweryfikuj z prawnikiem
- **Nie skip hooka "BEZ COUNCIL:" gdy to NAPRAWDĘ decyzja** — bo zjesz tokeny Claude Code zamiast oddelegować

---

## 7. Cowork mode dla analityków (główny tryb pracy)

Większość Twojej pracy z heart-vb **nie będzie** typowym "edytuj mi kod". Będziesz robić:
- Conversational research i synthesis (interviews, market data, competitors)
- Modeling i analizy (unit econ, projections, scenarios)
- Document drafting (IC memos, pitch decks, briefs, stakeholder updates)
- Strategic decisions (pricing, GTM, prioritization)

Cowork to **wielo-agent pattern w Claude Code** — równolegli agenci pracują nad różnymi częściami zadania w osobnych worktree. Idealnie sprawdza się w VB gdy:

| Wzorzec | Kiedy używać | Jak to zrobić |
|---------|---------------|---------------|
| **Parallel research** | Porównujesz 3-5 firm/ventures/sektorów | "Spawn 3 cowork agents — każdy przebada inną firmę przez deep-research, potem synthesize" |
| **Parallel modeling** | Base/bull/bear scenarios, sensitivity analysis | "Spawn 3 agents — każdy zbuduje 1 scenariusz przez saas-metrics-coach" |
| **Parallel writing** | IC memo z różnych perspektyw (PM, finance, GTM) | "Spawn 3 agents — każdy napisze sekcję przez board-prep z innym focus" |
| **Single Claude (no cowork)** | Decyzja, council debate, quick lookup, single IC memo | Pisz normalnie w jednym oknie |

### Jak cowork odnosi się do hooków

**Oba hooki fire w KAŻDYM cowork agencie** (są user-level w `~/.claude/`). Każdy agent:
- Dostaje vb-suggest (intent classification) i devtools-suggest (URL routing)
- Może wywołać `~/.local/bin/council` przez Bash tool — agent ma normalny access
- Może wywołać dowolny skill z heart-vb (auto-loaded)

### Cowork token budget

- 5 cowork agents × 1 council każdy = 5× zużycie limitów Gemini/Codex
- Ale: każdy agent ma osobny context window → twój main session pozostaje czysty
- Dla research/synthesis 5 agents oszczędza CAŁKOWITY czas (parallel) ale nie tokeny w sumie

### Pułapki cowork w VB

1. **Inconsistent decisions** — 5 agents debate niezależnie przez council → różne werdykty na to samo pytanie. Rozwiązanie: SAM zadawaj council, agenci tylko dostarczają input
2. **Brak shared context** — agent A nie wie co odkrył agent B. Rozwiązanie: synteza na końcu w main session, nie przez cowork
3. **Drift od kontekstu Heart** — agent w worktree może zapomnieć o sektorze. Rozwiązanie: każdy agent musi dostać explicit `heart-fintech-compliance` (lub odpowiedni) w prompt

---

## 8. Pierwsze 5 zadań (~2.5-3.5h)

Wykonaj te 5 w pierwszym tygodniu — każde używa **innego skilla** + ostatnie pokazuje cowork pattern.

### Zadanie 1: Research z URL (~30 min) — devtools hook fires
> Zbadaj TAM/SAM/SOM dla AI-powered legal contract review SaaS w Polsce. Profil top 5 konkurentów. Trendy regulacyjne. Sprawdź też https://www.g2.com/categories/contract-management-software dla benchmark vendors.

**Oczekiwany flow:** 
- vb-suggest fires (research intent) → sugeruje `deep-research`
- devtools-suggest fires (G2 to JS-heavy domain) → sugeruje chrome-devtools-mcp z evaluate_script zamiast WebFetch
- Claude pyta o oba, zgadzasz się, dostajesz strukturalny report bez wypalonych tokenów na shell HTML

### Zadanie 2: Modeling — konwersacyjnie (~20 min)
> Zbuduj unit economics dla MarTech SaaS: ARPU €49/mo, GM 78%, CAC €600 z paid+content mix, 4% monthly churn. Pokaż LTV, payback, contribution margin month-on-month. Wytłumacz mi też dlaczego payback period to ważniejsze niż LTV/CAC w naszej fazie.

**Oczekiwany flow:** vb-suggest fires (modeling) → sugeruje `saas-metrics-coach` → odpowiada strukturalnie + wyjaśnia kontekst pro-konwersacyjnie. Nie ma file edits — tylko chat.

### Zadanie 3: IC memo synthesis (~30 min)
> Mając output z Zadań 1-2, napisz mi IC memo dla wymyślonego venture "Heart Legal AI" — thesis, market opportunity (z polską perspektywą), team profile (1-osobowy lider + 2 advisors), 3-yr financials summary, top 3 risks z mitigations, ask (€500k seed for 18mc runway).

**Oczekiwany flow:** vb-suggest fires (writing) → sugeruje `board-prep` → dostajesz IC memo template który dopracujesz ręcznie.

### Zadanie 4: Council decision + sector context (~30 min)
> Skoro mam już IC memo i unit economics — uruchom council żeby ocenić czy ten venture jest fundable dla The Heart. Uwzględnij FinTech-like compliance constraints (legal AI dotyka data privacy + professional regulations).

**Oczekiwany flow:** vb-suggest fires (decision + sector hint) → council Tier L z `--context heart-fintech-compliance` jako reference → dostajesz syntezę 2-3 LLM + compliance check + scoring 0-10.

### Zadanie 5: Cowork — parallel competitor research (~40 min)
> Spawn 3 cowork agentów (przez `/cowork` lub manualnie przez Task tool) — każdy ma przebadać innego z top 5 konkurentów z Zadania 1. Każdy używa `competitive-teardown` (skill z heart-vb). Po 20 min synthesize w main session: porównanie cech, pricingu, GTM, kluczowych słabości każdego.

**Oczekiwany flow:**
- Agenci pracują równolegle, każdy z własnym context window (nie polluje main)
- Każdy dostaje hooks (vb-suggest + devtools-suggest fires u nich osobno)
- Po 20 min wracają z structured outputami
- Ty w main session synthesize przez prompt "Porównaj te 3 teardowny — common weaknesses, vendor positioning gaps, gdzie widzę okazję dla naszego venture"

### Zadanie bonus: self-improving po tygodniu (~15 min)
> Pod koniec tygodnia: `/si:review` — pokaż mi co Claude się nauczył o moich preferencjach. Następnie `/si:promote` najbardziej powtarzających się wzorców do CLAUDE.md.

**Oczekiwany flow:** `/si:review` pokazuje promotion candidates z auto-memory. Wybierasz 2-3 i `/si:promote` → trafiają do trwałego CLAUDE.md. Następna sesja zaczyna z tą wiedzą.

---

## 9. Troubleshooting

| Problem | Rozwiązanie |
|---------|-------------|
| `command not found: council` | PATH nie zawiera `~/.local/bin` — dodaj `export PATH="$HOME/.local/bin:$PATH"` do `~/.zshrc` |
| `Provider claude failed: unknown` | Council nie może odpalić zagnieżdżonego Claude Code (self-invocation block). To NIE jest błąd — fala kontynuuje z innymi providerami |
| `Gemini CLI timed out` | Cold start Gemini ~10s. Dla Tier L+ dodaj `--timeout 600` |
| Plugin install fail | Sprawdź `gh auth status`; jeśli OK, retry. Jeśli upstream zmieniony — zgłoś |
| Hook fires zbyt często | Edit `~/.claude/hooks/council-vb-suggest.sh` — usuń niektóre patterny |
| Hook nie fires nigdy | `cat ~/.claude/settings.json \| grep council-vb-suggest` — sprawdź czy zarejestrowany |
| Zła rekomendacja od council | To opinion model, nie sąd. Zweryfikuj liczby, dodaj kontekst Heart, decyduj jako człowiek |

---

## 10. Cheat sheet

```
# Najczęstsze patterny
<piszesz normalnie>                          # Hook decyduje czy fires
/council <pytanie>                           # Wymuszone wywołanie rady
BEZ COUNCIL: <pytanie>                       # Skip hook na tę wiadomość
council doctor                               # Status providerów (terminal)
codex login                                  # Re-auth ChatGPT Plus
gemini                                       # Re-auth Google Workspace OAuth

# Self-improving (run weekly)
/si:review                                   # Co warto promote
/si:promote                                  # Pattern → CLAUDE.md
/si:status                                   # Memory health

# Token-saving wzorce
"Użyj chrome-devtools-mcp z evaluate_script..."  # Multi-page research
"Użyj context7 żeby sprawdzić docs..."           # Library docs lookup
```

**Pełna referencja:** [Venture Builder map](venture-builder.md) · [Plugin README](../plugins/heart-vb/README.md)

---

## 11. Feedback po 1-2 tygodniach

Daj znać:
- Patterny hookowe są za szerokie / za wąskie?
- Które skille faktycznie używasz, które ignorujesz?
- Brakuje skill dla konkretnego use case?
- Sector context (heart-custom) działa czy zbyt powierzchowny?

Issue lub PR: https://github.com/The-Heart-Vibe/claude-code-marketplace
