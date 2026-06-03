# heart-vb — The Heart Venture Builder toolkit

**Jedna instalacja, kompletny VB stack.** 36 skilli w 8 kategoriach pod jednym pluginem.

```
/plugin marketplace add The-Heart-Vibe/claude-code-marketplace
/plugin install heart-vb@the-heart-vibe
```

I masz wszystko. Bez dodawania innych marketplaces.

## DD by Heart — 12 milestones framework

Plugin aligned z firmowym procesem Venture Building. **12 non-negotiable milestones w 4 fazach.** Każdy projekt przechodzi przez te same milestones — od kickoffu do fundraisingu.

```
Discovery (1-5) → Creation (6-8) → Validation (9-10) → Fundraising (11-12)
```

| # | Faza | Milestone | Primary skill |
|---|---|---|---|
| 1 | D | Analiza rynku | `vb-research/market-research` |
| 2 | D | Analiza konkurencji | `vb-product/competitive-teardown` |
| 3 | D | Walidacja z inwestorami (early signal) | `vb-process/investor-early-signal` ⭐ |
| 4 | D | Walidacja problemu z klientami | `vb-product/product-discovery` |
| 5 | D | **Napkin math** (czy się spina) | `vb-process/napkin-math` ⭐ |
| 6 | C | **Exit strategy & acquirers** | `vb-process/exit-strategy` ⭐ |
| 7 | C | Zespół & cap table | `vb-process/cap-table-helper` ⭐ |
| 8 | C | MVP / produkt & roadmapa | `vb-product/product-strategist` |
| 9 | V | Walidacja rozwiązania & pricing | `vb-commercial/pricing-strategist` |
| 10 | V | IP, regulacje & prawo | `heart-dd-checklist` + sector context |
| 11 | F | Materiały fundraisingowe | `heart-pitch-deck` + `board-prep` + `financial-analyst` |
| 12 | F | Lista inwestorów & outreach | `vb-comms/investor-outreach` |

⭐ = nowe skille w v0.7.0 (vb-process category)

**Master orchestrator:** `/heart-vb-process` — wykrywa milestone z konwersacji i deleguje do sub-skill, lub prowadzi przez cały proces ("przepuść projekt przez framework").

**Workflow skille (Krok 1-4 z dokumentu firmy):**
- `vb-process/assessment` — Krok 1: 12-row checker stanu projektu
- `vb-process/kickoff` — Krok 2: risk ranking + sprint planning
- `vb-process/bi-weekly-summary` — Krok 3: side product co 2 tyg.
- `vb-process/fundraising-readiness` — Krok 4: go/no-go gate

## Co dostajesz

| Kategoria | Skille | Source |
|-----------|--------|--------|
| **council** ⭐ | Multi-LLM debate z routingiem domain × tier (Claude Code + Codex + Gemini CLI) | The Heart Vibe |
| **self-improving** | si:* commands (`remember`, `review`, `extract`, `promote`, `status`) — agent auto-uczy się z MEMORY.md | alirezarezvani (MIT) |
| **vb-research** | deep-research, market-research (M1), exa-search | affaan-m (MIT) |
| **vb-product** | product-discovery (M4), competitive-teardown (M2), experiment-designer, ux-researcher-designer, product-strategist (M8) | alirezarezvani (MIT) |
| **vb-finance** | financial-analyst (M11), saas-metrics-coach (unit economics, P&L, KPIs) | alirezarezvani (MIT) |
| **vb-commercial** | pricing-strategist (M9), deal-desk, commercial-forecaster, channel-economics | alirezarezvani (MIT) |
| **vb-comms** | board-prep (M11 IC memo), stress-test, hard-call, investor-materials (M11), investor-outreach (M12) | mixed (MIT) |
| **vb-process** ⭐ NEW v0.7 | assessment (Krok 1), kickoff (Krok 2), bi-weekly-summary (Krok 3), fundraising-readiness (Krok 4), napkin-math (M5), exit-strategy (M6), cap-table-helper (M7), investor-early-signal (M3) | The Heart Vibe |
| **heart-custom** | **Master:** heart-vb-process (12-milestone orchestrator). **Sector contexts:** heart-healthtech-compliance ⭐, heart-academic-spinouts ⭐, heart-energy ⭐ (cała branża energetyczna), heart-fintech-compliance (legacy). **Atomic daily tools:** heart-pitch-deck (M11), heart-stakeholder-update, heart-comps-analysis (M6 inputs), heart-dd-checklist (M10), heart-dd-prep. **Meta:** heart-orchestrate (auto-cowork Pattern E/F). **Utility:** brainstorming (generic thinking partner), status (/heart-vb:status self-diagnostic) | The Heart Vibe + obra (MIT) |

**Total: 47 skilli w 9 kategoriach.** Pełna lista [w plugin.json](.claude-plugin/plugin.json). Atrybucja w [skills/ATTRIBUTION.md](skills/ATTRIBUTION.md).

## Gdzie plugin działa

| Środowisko | Skille | Hooki (UserPromptSubmit) | Heart-orchestrate Pattern E/F | Council CLI (binary) | Gemini/Codex CLI w Pattern F worker |
|---|---|---|---|---|---|
| **Claude Code (CLI/IDE)** | ✅ przez `/plugin install` | ✅ auto-load z `hooks/hooks.json` | ✅ Agent tool spawn | ❌ self-invocation block | ✅ przez `bash -c "gemini -p ..."` |
| **Claude Desktop → Cowork tab** | ✅ przez `/plugin install` (w Cowork session) | ✅ auto-load z `hooks/hooks.json` (od v0.6.10) | ✅ Agent tool spawn | ❌ self-invocation block + sandbox | ✅ przez `bash -c "gemini -p ..."` |
| **Terminal (standalone, poza CC)** | ❌ brak Agent tool | ❌ | ❌ brak orchestratora | ✅ działa natywnie | ✅ działa natywnie |
| **claude.ai (web)** | ❌ brak plugin support | ❌ | ❌ brak Agent tool | ❌ | ❌ brak Bash |
| **Claude Desktop (standardowy chat)** | ⚠️ via MCP/Extensions | ❌ | ❌ | ❌ | ❌ |

### Council CLI vs Pattern F — częsta konfuzja

**`council` jako CLI binary NIE działa z poziomu Claude Code ani Cowork** (terminal-only), z dwóch powodów:

1. **Self-invocation block** — council odpala `claude` jako jednego z 3 providers. Wewnątrz aktywnej Claude session `claude` CLI wykrywa nested invocation i odmawia. Council failuje przy pierwszym provider call.
2. **Subprocess fork w sandbox** — Cowork ma per-session isolation; council jako standalone binary z multi-subprocess orchestracją źle koegzystuje z sandboxem.

**Pattern F bypassuje obie sprawy** przez Agent tool isolation:
- Zamiast jednego `council run ...` binary → 3 osobne `Agent({...})` calls
- Każdy worker w isolated context, spawnuje 1 CLI (`bash -c "gemini -p ..."`, `bash -c "codex exec ..."`) lub używa Sonnet native
- Self-invocation block nie pojawia się bo workery nie wywołują nested Claude — wywołują tylko gemini/codex

Czyli: **gemini-cli i codex CLI działają w Cowork** (przez Pattern F workers), tylko `council` binary nie. Pattern F to pełna funkcjonalna alternatywa.

> **Cowork install:** w Cowork tab wpisz `/plugin marketplace add The-Heart-Vibe/claude-code-marketplace` → `/plugin install heart-vb@the-heart-vibe`. Hooki auto-load przy starcie sesji. Sprawdź stan przez `/heart-vb:status`.

## Co robi install.sh

Plugin sam się instaluje przez `/plugin install` (skille + hooki). Install.sh dorabia **wyłącznie dependencies systemowe** dla council CLI, gemini-cli i chrome-devtools-mcp — rzeczy poza scope pluginu:

1. Sprawdza/instaluje `uv` (Python package manager)
2. Sprawdza Node.js (wymagany dla Gemini CLI)
3. Instaluje globalnie `@google/gemini-cli` jeśli brak
4. Tworzy izolowany venv w `~/tools/council-env`
5. Instaluje `the-llm-council[gemini]>=0.7.16`
6. Tworzy wrapper w `~/.local/bin/council`
7. Kopiuje config template do `~/.config/llm-council/config.yaml`
8. Odpala `council doctor` i pokazuje status providerów
9. **Cleanup legacy:** usuwa stare wpisy hooków z `~/.claude/settings.json` (z wersji do v0.6.9) — od v0.6.10 hooki są auto-loaded przez plugin
10. Sprawdza/instaluje chrome-devtools-mcp przez `claude mcp add`
11. (Opcjonalnie) detect codex CLI dla pełnego Pattern F multi-LLM

### Ręczne uruchomienie installer

```bash
bash <(curl -s https://raw.githubusercontent.com/The-Heart-Vibe/claude-code-marketplace/main/plugins/heart-vb/install.sh)
```

### Override paths

```bash
COUNCIL_VENV=/custom/path/venv \
COUNCIL_WRAPPER_DIR=/custom/bin \
bash install.sh
```

## Auth providerów dla council

Po install odpal w terminalu:

```bash
council doctor
```

| Provider | Jeśli FAIL | Co daje |
|----------|-----------|---------|
| `claude` | Już zalogowany (Claude Code) | ❌ **NIE z poziomu aktywnej Claude Code session** — self-invocation block. Używaj tylko z terminala |
| `codex` | `codex login` (wymaga ChatGPT Plus/Pro) | Council używa GPT-5 zamiast Claude session |
| `gemini-cli` | `gemini` (OAuth przez Google Workspace) | Council używa Gemini — największa pula tokenów |

## Hooks (4 rekomendowane — install.sh instaluje wszystkie)

Plugin instaluje 4 hooki UserPromptSubmit. Wszystkie opcjonalne ale wzajemnie dopełniające. Każdy ma własny opt-out prefix.

### 1. Venture Builder Suggest (`vb-suggest.sh`)

Wykrywa promptów wyglądających na zadania VB (decision/research/modeling/writing/validation/screening) i sugeruje właściwy skill. Pyta: **"To wygląda na <intent> — proponuję użyć <skill>. Wolisz tak czy odpowiedzieć od razu?"**

### 2. Research Tool Router (`devtools-suggest.sh`) — token saver

Auto-wykrywa **URL-e + sygnały complex page** i kieruje Claude na `chrome-devtools-mcp` zamiast WebFetch dla **token-efficient browsing**.

> ⚠️ **Wymaga `chrome-devtools-mcp`.** Install.sh **instaluje automatycznie** przez `claude mcp add chrome-devtools npx chrome-devtools-mcp@latest`. Po instalacji wymagany restart Claude Code aby MCP server był aktywny. Bez tego hook fire'uje, ale Claude fallbackuje na WebFetch.

### 3. Cowork Spawn Router (`cowork-suggest.sh`) — parallel work detector

Wykrywa **multi-entity tasks** (5 konkurentów, 3 scenariusze, sekcje IC memo, landscape scan) i sugeruje spawn N parallel cowork agents zamiast sequential roboty w main. Każdy worker dostaje 1 entity.

| Sygnał | Akcja |
|--------|-------|
| "5 konkurentów", "top 10 firm", "3 sektory" | Spawn N agentów × 1 entity |
| "base/bull/bear scenario" | Spawn 3 agentów × 1 scenariusz |
| "porównaj A vs B vs C" | Spawn N agentów × 1 option |
| "landscape teardown", "scan rynek" | Spawn agentów × 1 segment |
| "dla każdej z tych firm" | Spawn × 1 firma |

### 4. Model Router (`model-route.sh`) — cost/quality tiering

Klasyfikuje complexity i sugeruje **model tier**:

| Tier | Trigger keywords | Reasoning |
|------|------------------|-----------|
| **Haiku** | "co znaczy X", format, rename, krótkie pytania | 3× tańsze, wystarczające dla lookup |
| **Sonnet** | (default) — wszystkie routine VB tasks | Balanced cost/quality, większość pracy |
| **Opus** | strategic, IC memo, board prep, council, deep research, ambiguous trade-off | Najdeepsze reasoning dla high-stake decisions |

**Cowork pattern reminder w outpucie:**
- Main session (orchestrator) → opus
- Workers (Agent tool calls) → sonnet
- Trivial helpers → haiku
- Explicit `model: "sonnet"` parameter w `Agent({...})` calls

| Sygnał | Akcja |
|--------|-------|
| ≥2 URL-i w jednym prompcie | Multi-page workflow → DevTools z jedną sesją |
| JS-heavy domain (G2, Crunchbase, Linkedin, app.*, dashboard.*, etc.) | WebFetch widzi shell HTML → DevTools |
| Interactive flow (click/fill/login/scroll) | WebFetch nie umie → DevTools |
| Dynamic content (infinite scroll, SPA, lazy load) | DevTools renderuje JS |
| Targeted extraction (top 10, każdy, tabela) | DevTools `evaluate_script` ~200 tok vs WebFetch ~600+ |
| Workflow keywords (porównaj konkurentów, scan landscape) | Multi-page DevTools wins |

Skip threshold: 1 statyczna URL + brak signals → milczy (WebFetch jest OK).

### Multi-intent classification (vb-suggest)

Hook klasyfikuje 7 intentów (6 VB + brainstorming jako fall-through) i sugeruje właściwy skill:

| Intent | Trigger keywords | Suggested skill |
|--------|------------------|------------------|
| **decision** | "vs", "co wybrać", "build-vs-buy" | **heart-orchestrate Pattern E** (3 personas → judgment przez role-play) |
| **research** | "TAM", "konkurenci", "regulacja" | **heart-orchestrate Pattern F** (3 LLMs: Claude+Gemini+Codex → fact verification + hallucination detection) |
| **modeling** | "CAC", "LTV", "DCF", "unit econ" | financial-analyst, saas-metrics-coach (+ Pattern E dla interpretacji) |
| **writing** | "IC memo", "pitch deck", "term sheet" | board-prep, heart-pitch-deck, investor-materials (+ Pattern E dla multi-section) |
| **validation** | "JTBD", "interview", "fake door" | product-discovery, experiment-designer, ux-researcher-designer |
| **screening** | "founder fit", "patent", "spin-out" | deal-desk, heart-dd-checklist, heart-dd-prep |
| **brainstorm** (fall-through) | "pomyśl ze mną", "pomóż mi ułożyć", "jak zorganizować/zaplanować/podejść", "nie wiem jak", "agenda spotkania" | **brainstorming** — generic thinking partner dla non-VB tasków (organizacja eventu, struktura spotkania, ad-hoc decyzja, draft komunikacji) |
| **+sector** | HealthTech / academic / energy / FinTech | adds sector context z heart-custom (np. heart-healthtech-compliance) |

**Council CLI**: terminal-only (z poziomu CC session zazwyczaj failuje — nested invocation block). Pattern F to workaround który daje multi-LLM debate z CC bez tego problemu.

### Consent-first design (KROK -1)

**Plugin zawsze pyta przed odpaleniem skill'a lub workflow.** Nie ma "magicznego" auto-spawn 3 ekspertów ani auto-brainstorm bez Twojej zgody. Pattern:

> *"To wygląda na [intent w plain language] — proponuję [skill/dialog/3 ekspertów]. (a) tak (b) odpowiedz inline bez skill (c) sam wiem co chcę."*

**Co wymaga consent:**
- Cowork spawn (Pattern E/F z heart-orchestrate) — ~60-90s + tokeny
- Brainstorming flow (multi-turn dialog ~5-10 min)
- Skill activation z istotnym scope'em (board-prep, financial-analyst, deep-research)

**Co skip consent:**
- Trivial lookups (Haiku tier) — "co znaczy ARPU"
- Single Read/Bash commands
- Slash commands (`/...`)

Power user może wyłączyć consent gate per-prompt: `BEZ PYTANIA: ...`

### Opt-out per prompt (5 prefixów)

```
BEZ PYTANIA: ...        # skip universal consent gate (just do)
BEZ COUNCIL: ...        # skip vb-suggest (no skill suggestion)
BEZ DEVTOOLS: ...       # skip devtools-suggest (use WebFetch)
USE WEBFETCH: ...       # alternative dla devtools-suggest
BEZ COWORK: ...         # skip cowork-suggest (stay in main session)
SINGLE SESSION: ...     # alternative dla cowork-suggest
BEZ ROUTE: ...          # skip model-route (no tier suggestion)
```

### Disable globalnie

Hooki są auto-loaded z `hooks/hooks.json` wewnątrz pluginu (od v0.6.10). Żeby je wyłączyć:

- **Wyłącz cały plugin:** `/plugin uninstall heart-vb` (znikają hooki + skille)
- **Wyłącz konkretny hook:** edytuj `${CLAUDE_PLUGIN_ROOT}/hooks/hooks.json` (zlokalizuj przez `find ~/.claude/plugins ~/Library/Application\ Support/Claude -name "hooks.json" -path "*heart-vb*"`) i usuń wybrane wpisy
- **Per-prompt opt-out:** użyj prefiksu (np. `BEZ COUNCIL:`) — patrz tabela wyżej

Legacy hooki z wersji ≤0.6.9 (w `~/.claude/settings.json` + `~/.claude/hooks/heart-*.sh`) są automatycznie wyczyszczone przez install.sh przy upgrade.

## Self-improving agent (si:*)

Po install masz dostęp do `/si:` commands które pozwalają agentowi uczyć się z każdej sesji:

| Command | Co robi |
|---------|---------|
| `/si:remember <wiedza>` | Explicitly save do auto-memory |
| `/si:review` | Analizuje MEMORY.md — promotion candidates, stale entries |
| `/si:promote` | Graduate pattern z MEMORY.md → CLAUDE.md / rules |
| `/si:extract` | Turn pattern → standalone skill |
| `/si:status` | Memory health dashboard |

Pełna referencja: [skills/self-improving/self-improving-agent/SKILL.md](skills/self-improving/self-improving-agent/SKILL.md)

## Heart-custom skills

4 sector-specific contexty reflektujące **aktualny focus Heart 2026**:

- **heart-healthtech-compliance** ⭐ — MDR, RODO art. 9, NFZ procurement, IRB approval. Use case: Wellnoted + new HealthTech ventures
- **heart-academic-spinouts** ⭐ — PAN/AGH/PW/PWr/UW/UJ/WUM, IP transfer z CTT, NCBR Szybka Ścieżka/LIDER/Bridge Alpha, NCN, FENG, IP Box. Use case: ventures budowane z polskimi uczelniami
- **heart-energy** ⭐ — Cała branża energetyczna: generation (OZE, nuclear/SMR, gas), T&D (PSE/DSO), storage (BESS, V2G), e-mobility (CPO/EMSP), wodór (H2), heat & buildings (heat pumps, district heating), energy services SaaS (forecasting, EMS, trading). Regulator stack: RED III, EU ETS, EU Battery Reg, EPBD, CSRD. Funding: NFOŚiGW, NCBR FENG, EU Innovation Fund
- **heart-fintech-compliance** — KNF, AMLD6, MIFID2, PSD2, RODO, DORA. Use case: VASBOX, Digital Gateways (legacy portfolio)

Loaderzy `--context` dla council + standalone reference podczas IC memo. **Dla sektorów spoza tej listy** (EdTech, Defense, AgriTech, etc.) — persona alone wystarczy (patrz Pattern E w heart-orchestrate).

## Diagnostyka

### Z poziomu Claude Code / Cowork (rekomendowane)

```
/heart-vb:status
```

Self-diagnostic skill — wykrywa environment (CLI vs Cowork), wersję pluginu, status hooków, dependencies (gemini-cli, codex, chrome-devtools-mcp), auth providers, gotowość Pattern E/F (Tier 1/2/3). Read-only, bez konsumpcji tokenów. **Pierwsze co odpalić gdy plugin "nie działa".**

### Z poziomu terminala (council binary only)

```bash
council doctor                                       # status providerów (CLI tylko)
council doctor --deep --provider gemini-cli          # live test (zużywa tokeny!)
council version
council config --show
```

> Uwaga: `council doctor` failuje z poziomu CC/Cowork session — uruchom **bezpośrednio w terminalu**.

## Update z poprzedniej wersji

```
# 1. Pull latest marketplace manifests
/plugin marketplace update

# 2. Upgrade heart-vb
/plugin update heart-vb

# 3. Restart Claude Code lub Cowork tab — hooks/hooks.json loaduje się przy starcie

# 4. (Tylko jeśli przechodzisz z ≤v0.6.9) — cleanup legacy hooks
bash <(curl -s https://raw.githubusercontent.com/The-Heart-Vibe/claude-code-marketplace/main/plugins/heart-vb/install.sh)

# 5. Verify
/heart-vb:status
# Spodziewaj się: 4/4 hooks auto-loaded, 0 legacy hooks, gemini ✅
```

> **Dlaczego krok 4 jest konieczny tylko z ≤v0.6.9:** wersje do v0.6.9 instalowały hooki ręcznie do `~/.claude/settings.json`. Od v0.6.10 są auto-loaded z `hooks/hooks.json` w pluginie. Bez kroku 4 oba mechanizmy są aktywne → każdy hook strzela 2× per prompt (dual-fire). Install.sh v0.6.10+ usuwa legacy entries z settings.json (z backupem).

## Reinstalacja (od zera)

```bash
which uv || curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv ~/tools/council-env
uv pip install 'the-llm-council[gemini]' --python ~/tools/council-env/bin/python
~/.local/bin/council doctor
```

Provider re-auth:
- `codex` → `codex login`
- `gemini-cli` → `gemini` (otworzy przeglądarkę → OAuth)

## Onboarding nowego teammate'a

→ [collections/onboarding-vb.md](../../collections/onboarding-vb.md) (30 min step-by-step)

---

<sub>Built with ☕ at The Heart by Wojtek Czuba · Każdy spawned agent w heart-orchestrate ma na imię Wojtek (small easter egg dla obserwujących).</sub>
