---
name: heart-status
description: "Self-diagnostic dla heart-vb — wykrywa środowisko (Claude Code CLI vs Cowork), wersję pluginu, status hooków, dependencies (gemini-cli, codex, Desktop Commander MCP, chrome-devtools-mcp, council CLI, Notion MCP), auth providers, gotowość Pattern E/F. Od v0.7.1 z opcjonalnym **milestone progress detection** — jeśli Notion MCP connector aktywny i user poda link do Project Card, skill czyta X/12 progress z linked database Streams/Milestones (Warstwa 2 DD by Heart). Use gdy plugin nie działa, przed demo/onboardingiem, lub gdy chcesz sprawdzić \"gdzie stoimy z projektem\". Trigger przez `/heart-status` lub fraza \"sprawdź czy plugin działa\", \"milestone progress\", \"ile zostało do fundraisingu\"."
---

> 🔒 **heart-vb CORE — zawsze, niezależnie od załadowanego skilla:**
> (1) output = prosty polski, zero żargonu (pass/Voices/Pattern-F-internal) · (2) fakty do VC (TAM/multiple/exit/CAC-LTV/regulacje) → zaproponuj cross-check Pattern F zanim trafią do decka · (3) nowy milestone → **załaduj jego skill** (`/heart-vb:X`), nie improwizuj · (4) KROK -1 consent przed kosztownym spawnem · (5) taguj [Guessing] na niepewnych liczbach, nie udawaj cross-checku na jednym modelu.

# Heart-vb Status — Self-Diagnostic

Sprawdza wszystkie komponenty pluginu, środowisko wykonawcze i gotowość workflow'ów. Output: jeden zwięzły raport z verdict per komponent.

## Po co

Plugin często nie działa z powodu który trudno zdiagnozować bez wglądu w środowisko:
- Środowisko nie wspiera plugins (claude.ai web → never)
- Plugin nie zainstalowany w aktualnej sesji
- Hooki nie auto-loadują się (stara wersja Claude Code <v2.1)
- Dependencies missing (gemini, codex, chrome-devtools-mcp)
- Provider nie zalogowany (gemini wymaga OAuth, codex wymaga ChatGPT Plus)

Skill agreguje to wszystko w jeden raport.

## Flow

Uruchom Bash diagnostyczne komendy **równolegle** gdzie to możliwe. Zbierz output, zaprezentuj w formacie poniżej. Nie pytaj o consent — to read-only diagnostic, nic nie modyfikuje.

### Krok 1 — Environment detection

```bash
# Czy jesteśmy w Claude Code CLI czy Cowork (Desktop)?
if [ -n "${CLAUDE_DESKTOP_VERSION:-}" ] || echo "${PWD:-}" | grep -q "local-agent-mode-sessions"; then
  ENV="Cowork (Claude Desktop)"
elif [ -n "${CLAUDECODE:-}" ] || command -v claude >/dev/null 2>&1; then
  ENV="Claude Code (CLI/IDE)"
else
  ENV="Unknown"
fi
echo "Environment: $ENV"
```

### Krok 2 — Plugin version + auto-load mechanism

```bash
# Znajdź plugin.json w environment-aware location
PLUGIN_JSON=""
for candidate in \
  ~/.claude/plugins/cache/*/heart-vb/*/.claude-plugin/plugin.json \
  ~/.claude/plugins/cache/*/heart-vb/.claude-plugin/plugin.json \
  ~/Library/Application\ Support/Claude/local-agent-mode-sessions/skills-plugin/*/*/heart-vb/.claude-plugin/plugin.json \
  "${CLAUDE_PLUGIN_ROOT:-}/.claude-plugin/plugin.json"
do
  if [ -f "$candidate" ]; then PLUGIN_JSON="$candidate"; break; fi
done
[ -n "$PLUGIN_JSON" ] && python3 -c "import json; d=json.load(open('$PLUGIN_JSON')); print(f\"Plugin: {d['name']} v{d['version']} ({len(d.get('skills',[]))} skilli)\")" || echo "Plugin: NIE WYKRYTY w cache"
```

### Krok 3 — Hooks loaded (auto-load + legacy detection)

```bash
# Sprawdź hooks.json (v0.6.10+ auto-load)
HOOKS_JSON=""
for candidate in \
  ~/.claude/plugins/cache/*/heart-vb/*/hooks/hooks.json \
  ~/Library/Application\ Support/Claude/local-agent-mode-sessions/skills-plugin/*/*/heart-vb/hooks/hooks.json
do
  if [ -f "$candidate" ]; then HOOKS_JSON="$candidate"; break; fi
done
if [ -n "$HOOKS_JSON" ]; then
  COUNT=$(python3 -c "import json; print(len(json.load(open('$HOOKS_JSON'))['hooks']['UserPromptSubmit']))" 2>/dev/null)
  echo "Hooks (auto-load): $COUNT z hooks.json"
else
  echo "Hooks (auto-load): BRAK hooks.json (pewnie ≤v0.6.9)"
fi

# Legacy detection — zostawione w settings.json
LEGACY=$(python3 -c "
import json, os
try:
    cfg = json.load(open(os.path.expanduser('~/.claude/settings.json')))
    hooks = cfg.get('hooks', {}).get('UserPromptSubmit', [])
    markers = ['council-vb-suggest.sh', 'heart-devtools-suggest.sh', 'heart-cowork-suggest.sh', 'heart-model-route.sh']
    cnt = sum(1 for e in hooks for h in e.get('hooks',[]) if any(m in h.get('command','') for m in markers))
    print(cnt)
except: print(0)
")
[ "$LEGACY" -gt 0 ] && echo "Legacy hooks (settings.json): $LEGACY — uruchom install.sh aby wyczyścić" || true
```

### Krok 4 — Dependencies

```bash
echo "--- Dependencies ---"
# gemini-cli (wymagany dla Pattern E persona-driven i Pattern F)
if command -v gemini >/dev/null 2>&1; then
  echo "gemini-cli: ✅ $(gemini --version 2>/dev/null | head -1 || echo 'installed')"
else
  echo "gemini-cli: ❌ brak — install: npm install -g @google/gemini-cli"
fi

# codex (opcjonalny — daje 3-voice Pattern F)
if command -v codex >/dev/null 2>&1; then
  echo "codex: ✅ $(codex --version 2>/dev/null | head -1 || echo 'installed')"
else
  echo "codex: ⚠️ brak — Pattern F będzie 2-voice (Sonnet + Gemini); install opcjonalny"
fi

# chrome-devtools-mcp (dla devtools-suggest hook)
if claude mcp list 2>/dev/null | grep -qi chrome-devtools; then
  echo "chrome-devtools-mcp: ✅ registered"
else
  # Fallback grep w configach
  if grep -qli chrome-devtools ~/.claude.json ~/.claude/mcp.json ~/.config/claude/mcp.json 2>/dev/null; then
    echo "chrome-devtools-mcp: ✅ in config"
  else
    echo "chrome-devtools-mcp: ⚠️ brak — install: claude mcp add chrome-devtools npx chrome-devtools-mcp@latest"
  fi
fi

# council CLI (terminal-only, NIE działa z poziomu CC/Cowork)
if [ -x ~/.local/bin/council ]; then
  echo "council CLI: ✅ installed (TYLKO TERMINAL — w CC/Cowork użyj Pattern F)"
else
  echo "council CLI: ⚠️ brak — opcjonalny (Pattern F to alternatywa)"
fi

# Desktop Commander MCP — KLUCZOWE dla Pattern F w Cowork (bridge gemini/codex do hosta)
if claude mcp list 2>/dev/null | grep -qiE "desktop.?commander"; then
  echo "Desktop Commander MCP: ✅ — Pattern F działa w Cowork (gemini/codex na hoście przez DC)"
elif grep -qliE "desktop.?commander" ~/.claude.json ~/Library/Application\ Support/Claude/*.json 2>/dev/null; then
  echo "Desktop Commander MCP: ✅ in config"
else
  echo "Desktop Commander MCP: ⚠️ brak — bez niego Pattern F w Cowork niedostępny (CLI nadal działa przez Bash)"
fi
```

### Krok 5 — Auth status (tylko jeśli council jest)

```bash
if [ -x ~/.local/bin/council ]; then
  echo "--- Auth providers (z council doctor) ---"
  ~/.local/bin/council doctor 2>/dev/null | grep -E "claude|codex|gemini" | head -5 || echo "  doctor failed (Cowork? z terminal odpal: council doctor)"
fi
```

### Krok 6 — Pattern E/F readiness tier

Po zebraniu danych powyżej, **oceń tier gotowości**:

| Tier | Wymaga | Co działa |
|---|---|---|
| **Tier 1 (Min)** | Sonnet only | Pattern E z all-Sonnet personas (fallback, działa zawsze) |
| **Tier 2 (Standard)** | + gemini-cli OK | Pattern E z prawdziwym multi-LLM divergence (3 personas × Gemini) |
| **Tier 3 (Full)** | + codex zalogowany | Pattern F 3-voice (Sonnet + Gemini + Codex) — najlepsza hallucination detection |

### Krok 6b — Notion connector + milestone progress (DD by Heart)

Plugin nie ma własnego dostępu do Notion ale **wykrywa czy Notion MCP connector jest aktywny** w sesji. Jeśli tak — może czytać Project Card i raportować milestone progress (X/12).

```bash
echo "--- Notion connector (DD by Heart milestone tracking) ---"
NOTION_AVAILABLE="no"
# Method A: claude mcp list
if claude mcp list 2>/dev/null | grep -qi notion; then
  NOTION_AVAILABLE="yes"
  NOTION_SOURCE="claude mcp list"
fi
# Method B: grep w configach MCP
if [ "$NOTION_AVAILABLE" = "no" ]; then
  for cfg in ~/.claude.json ~/.claude/mcp.json ~/.config/claude/mcp.json \
             ~/Library/Application\ Support/Claude/*.json; do
    if [ -f "$cfg" ] && grep -qi '"notion"' "$cfg" 2>/dev/null; then
      NOTION_AVAILABLE="yes"
      NOTION_SOURCE="$cfg"
      break
    fi
  done
fi

if [ "$NOTION_AVAILABLE" = "yes" ]; then
  echo "Notion MCP: ✅ available (source: $NOTION_SOURCE)"
  echo "→ Możesz podać link do Project Card w Notion żebym sprawdził milestone progress (X/12)."
else
  echo "Notion MCP: ⚠️ brak — milestone progress nie do auto-pull"
  echo "→ Install: w Cowork UI: Settings → Connectors → Notion (OAuth)"
  echo "→ Lub CLI: claude mcp add notion <npm package z https://github.com/makenotion/notion-mcp-server>"
  echo "→ Bez Notion: opowiedz mi ręcznie który milestone jest w jakim stanie i wykonam assessment z Twoich danych"
fi
```

#### Milestone progress detection flow (jeśli Notion available)

Po wykryciu Notion connector, **NIE pobieraj automatycznie**. Spytaj user'a:

> *"Wykryłem Notion MCP. Mogę sprawdzić milestone progress (X/12) dla konkretnego projektu — daj link do Project Card lub nazwę projektu. Albo zostań przy diagnostyce środowiskowej."*

Jeśli user dał link / nazwę projektu, **przez Notion MCP tools** (`notion-search`, `notion-fetch`):

1. Search Project Card po nazwie projektu lub fetch po URL
2. Read property `Faza` (Discovery / Creation / Validation / Fundraising)
3. Iteruj przez linked database Streams/Milestones (Warstwa 2 z dokumentu firmy):
   - 12 streamów, każdy ze statusem (Backlog / In Progress / Done)
   - Per stream: Objective, Key Results, Deliverable link
4. Count: X done, Y in progress, Z backlog → progress X/12
5. Identyfikuj **next milestone** (najbliższy in-progress lub backlog w aktualnej fazie)
6. Wykryj **anomalie**:
   - >3 streamy in progress jednocześnie (dokument firmy: max 2-3)
   - Milestone w fazie późniejszej done, gdy wcześniejsza missing (np. M11 done ale M6 brak)
   - Streamy bez Deliverable linka (placeholder, nie real progress)

#### Output rozszerzenie dla milestone progress

Gdy Notion data dostępne, dodaj sekcję do raportu:

```
DD by Heart milestone progress:
  Project: <nazwa>
  Faza: <Discovery/Creation/Validation/Fundraising>
  Progress: X/12 ✓ · Y/12 ◐ (in progress) · Z/12 ☐ (backlog)
  
  Per faza:
    Discovery (M1-M5):  X/5 ✓
    Creation (M6-M8):   X/3 ✓
    Validation (M9-M10): X/2 ✓
    Fundraising (M11-M12): X/2 ✓
  
  Next critical milestone: M<N> <name> (status: ◐, ETA: <data>)
  
  Anomalie wykryte:
    - <konkret, np. "5 streamów in progress — przekroczone 2-3 z dokumentu firmy">
    - <konkret>
  
  Fundraising readiness (heurystyka):
    Pre-seed: <gotowi/wymaga X/Y> (must-haves M5, M7, M11, M12)
    Seed: <gotowi/wymaga X/Y> (must-haves wszystkie z above + M4, M8, M9, M6)
  
  → Pełen check: /heart-vb-process fundraising-readiness skill
```

## Krok 7 — Action items (CRITICAL — concrete fix commands)

Po zebraniu danych ZAWSZE generuj sekcję **Action items** jeśli wykryjesz problemy. Każdy item musi mieć konkretną komendę do skopiowania, nie ogólnik.

| Wykryty problem | Action item (paste-able command) |
|---|---|
| `Plugin: NIE WYKRYTY` | **CLI/IDE:** `/plugin marketplace add The-Heart-Vibe/the-heart-marketplace` → `/plugin install heart-vb@the-heart-marketplace`. **Cowork:** Customize → Personal plugins → "+" → Create plugin → Add marketplace → install (GUI, brak slash-komend). Potem restart sesji |
| `Hooks: 0/4` mimo plugin OK | Restart Claude Code / Cowork tab — hooks/hooks.json loaduje się przy starcie |
| `Legacy hooks (settings.json): >0` | Pobierz → przejrzyj → uruchom (NIE pipe-to-bash na ślepo): `curl -fsSL -o /tmp/hv-install.sh https://raw.githubusercontent.com/The-Heart-Vibe/the-heart-marketplace/main/plugins/heart-vb/install.sh && less /tmp/hv-install.sh && bash /tmp/hv-install.sh` — usuwa legacy z backupem. **WAŻNE: bez tego hooki strzelają 2× per prompt (dual-fire)** |
| `gemini-cli: ❌` | `npm install -g @google/gemini-cli` (wymaga Node.js) → `gemini` (OAuth w przeglądarce) |
| `codex: ⚠️` (Pattern F będzie 2-voice) | Opcjonalne — Codex CLI install + `codex login` (wymaga ChatGPT Plus). Bez Codex pełny Pattern F nadal działa jako 2-voice fallback. |
| `chrome-devtools-mcp: ⚠️` | `claude mcp add chrome-devtools npx chrome-devtools-mcp@latest` → restart sesji |
| `council CLI: ⚠️` | Opcjonalne — działa TYLKO z terminala. W CC/Cowork użyj Pattern F (heart-orchestrate skill) jako workaround |
| `Notion MCP: ⚠️` | Opcjonalne ale **silnie rekomendowane dla milestone tracking** — bez Notion connector plugin nie ma jak czytać X/12 progress. Setup: w Cowork → Settings → Connectors → Notion (OAuth). Lub CLI: `claude mcp add notion <package>`. Po dodaniu — restart sesji i podaj plugin link do Project Card |

## Output format (przedstaw user'owi)

```
🩺 Heart-vb Status Report

Environment: <CLI/Cowork/Unknown>
Plugin: heart-vb v<X.Y.Z> (<N> skilli)
Hooks: <N>/4 auto-loaded ✅ | ❌ <issue>
Legacy hooks: <N> w settings.json — ⚠️ DUAL-FIRE RISK jeśli >0

Dependencies:
  gemini-cli      ✅/❌ <version/issue>
  codex           ✅/⚠️ <version/optional>
  Desktop Cmder   ✅/⚠️ <Pattern F bridge w Cowork>
  chrome-devtools ✅/⚠️ <registered/install command>
  council CLI     ✅/⚠️ <terminal-only note>
  Notion MCP      ✅/⚠️ <connector dla milestone tracking>

Pattern readiness:
  Tier 1 (Min)      ✅ <always>
  Tier 2 (Standard) ✅/❌ <reason>
  Tier 3 (Full)     ✅/⚠️ <reason>

DD by Heart milestone tracking:
  Notion connector  ✅/⚠️
  [Jeśli Notion ✅ + user dał project link, wstaw sekcję milestone progress
   z Kroku 6b: X/12 ✓, per-faza breakdown, next critical, anomalie]
  [Jeśli ⚠️ lub brak link: "Podaj Notion link lub opowiedz ręcznie który milestone w jakim stanie"]

Verdict: <one sentence — ready to use / fix X first / requires Notion for milestone tracking>

[Action items jeśli są — jak dokończyć setup]
```

## Edge cases

- **Brak `claude` w PATH**: w Cowork pewnie nie ma — fallback na inne sygnały (CLAUDE_PLUGIN_ROOT env)
- **Council doctor failuje w Cowork**: spodziewane — note że terminal-only, nie blocker dla Pattern F
- **Plugin nie wykryty**: nie zainstalowany w aktualnym environment. **CLI/IDE:** `/plugin marketplace add The-Heart-Vibe/the-heart-marketplace` + `/plugin install heart-vb@the-heart-marketplace`. **Cowork:** Customize → Personal plugins → "+" → Create plugin → Add marketplace → install (GUI, Cowork nie ma slash-komend `/plugin`)
- **Legacy hooks present**: backup + clean przez install.sh — pobierz i przejrzyj przed uruchomieniem: `curl -fsSL -o /tmp/hv-install.sh https://raw.githubusercontent.com/The-Heart-Vibe/the-heart-marketplace/main/plugins/heart-vb/install.sh && less /tmp/hv-install.sh && COUNCIL_INSTALL_HOOK=skip bash /tmp/hv-install.sh` (NIE curl|bash na ślepo)

## NIE rób

- Nie spawnuj cowork agents w trakcie diagnostyki — to ma być fast, read-only
- Nie modyfikuj settings.json bez explicit user yes
- Nie odpalaj `council doctor --deep` (zużywa tokeny)
- Nie ask consent przed diagnostyką — to instrument, nie workflow
