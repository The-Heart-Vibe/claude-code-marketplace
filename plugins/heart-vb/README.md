# heart-vb — The Heart Venture Builder toolkit

**Jedna instalacja, kompletny VB stack.** 30 skilli w 8 kategoriach pod jednym pluginem.

```
/plugin marketplace add The-Heart-Vibe/claude-code-marketplace
/plugin install heart-vb@the-heart-vibe
```

I masz wszystko. Bez dodawania innych marketplaces.

## Co dostajesz

| Kategoria | Skille | Source |
|-----------|--------|--------|
| **council** ⭐ | Multi-LLM debate z routingiem domain × tier (Claude Code + Codex + Gemini CLI) | The Heart Vibe |
| **self-improving** | si:* commands (`remember`, `review`, `extract`, `promote`, `status`) — agent auto-uczy się z MEMORY.md | alirezarezvani (MIT) |
| **vb-research** | deep-research, market-research, exa-search | affaan-m (MIT) |
| **vb-product** | product-discovery, competitive-teardown, experiment-designer, ux-researcher-designer, product-strategist | alirezarezvani (MIT) |
| **vb-finance** | financial-analyst, saas-metrics-coach (unit economics, P&L, KPIs) | alirezarezvani (MIT) |
| **vb-commercial** | pricing-strategist, deal-desk, commercial-forecaster, channel-economics | alirezarezvani (MIT) |
| **vb-comms** | board-prep (IC memo), stress-test, hard-call, investor-materials, investor-outreach | mixed (MIT) |
| **heart-custom** | heart-fintech-compliance (KNF/AMLD), heart-healthtech-compliance (MDR/RODO art. 9), heart-realestate-context (polski RE market), heart-martech-ecosystem (Shopify/WooCommerce/Allegro) | The Heart Vibe |

**Total: 30 skilli.** Pełna lista [w plugin.json](.claude-plugin/plugin.json). Atrybucja w [skills/ATTRIBUTION.md](skills/ATTRIBUTION.md).

## Co robi install.sh

Skille SKILL.md są auto-loaded przez Claude Code po `/plugin install`. Ale council CLI wymaga setup'u systemowego — install.sh tym się zajmuje:

1. Sprawdza/instaluje `uv` (Python package manager)
2. Sprawdza Node.js (wymagany dla Gemini CLI)
3. Instaluje globalnie `@google/gemini-cli` jeśli brak
4. Tworzy izolowany venv w `~/tools/council-env`
5. Instaluje `the-llm-council[gemini]>=0.7.16`
6. Tworzy wrapper w `~/.local/bin/council`
7. Kopiuje config template do `~/.config/llm-council/config.yaml`
8. **Pyta czy zainstalować Venture Builder hook** (rekomendowane: y)
9. Odpala `council doctor` i pokazuje status providerów

### Ręczne uruchomienie installer

```bash
bash <(curl -s https://raw.githubusercontent.com/The-Heart-Vibe/claude-code-marketplace/main/plugins/heart-vb/install.sh)
```

### Non-interactive install

```bash
COUNCIL_INSTALL_HOOK=yes bash install.sh   # auto-yes na hook
COUNCIL_INSTALL_HOOK=no bash install.sh    # auto-no
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

Hook klasyfikuje 6 intentów i sugeruje właściwy skill:

| Intent | Trigger keywords | Suggested skill |
|--------|------------------|------------------|
| **decision** | "vs", "co wybrać", "build-vs-buy" | council Tier L |
| **research** | "TAM", "konkurenci", "research" | deep-research, market-research, exa-search |
| **modeling** | "CAC", "LTV", "DCF", "unit econ" | financial-analyst, saas-metrics-coach |
| **writing** | "IC memo", "pitch deck", "term sheet" | board-prep, investor-materials |
| **validation** | "JTBD", "interview", "fake door" | product-discovery, experiment-designer |
| **screening** | "founder fit", "patent", "spin-out" | deal-desk, board-prep |
| **+sector** | FinTech / HealthTech / RealEstate / MarTech | adds compliance reminder z heart-custom |

### Opt-out per prompt (4 prefixy)

```
BEZ COUNCIL: ...        # skip vb-suggest (no skill suggestion)
BEZ DEVTOOLS: ...       # skip devtools-suggest (use WebFetch)
USE WEBFETCH: ...       # alternative dla devtools-suggest
BEZ COWORK: ...         # skip cowork-suggest (stay in main session)
SINGLE SESSION: ...     # alternative dla cowork-suggest
BEZ ROUTE: ...          # skip model-route (no tier suggestion)
```

### Disable globalnie

Usuń wpisy z `~/.claude/settings.json` hooks.UserPromptSubmit, lub usuń pliki:
- `~/.claude/hooks/council-vb-suggest.sh` (vb-suggest)
- `~/.claude/hooks/heart-devtools-suggest.sh` (devtools-suggest)
- `~/.claude/hooks/heart-cowork-suggest.sh` (cowork-suggest)
- `~/.claude/hooks/heart-model-route.sh` (model-route)

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

4 sector-specific contexty pisane pod portfolio The Heart:

- **heart-fintech-compliance** — KNF, AMLD6, MIFID2, PSD2, RODO. Use case: VASBOX, Digital Gateways
- **heart-healthtech-compliance** — MDR, RODO art. 9, NFZ procurement, IRB approval. Use case: Wellnoted
- **heart-realestate-context** — polski rynek RE (OtoDom/Morizon, regionalność, brokerzy). Use case: Flatte, HomeAlert
- **heart-martech-ecosystem** — Shopify/WooCommerce/Allegro, polski SME e-commerce. Use case: UniPerks

Loaderzy `--context` dla council + standalone reference podczas IC memo.

## Diagnostyka

```bash
council doctor                                       # status providerów
council doctor --deep --provider gemini-cli          # live test (zużywa tokeny!)
council version
council config --show
```

## Reinstalacja

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
