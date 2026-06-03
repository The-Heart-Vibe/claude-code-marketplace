---
name: status
description: Self-diagnostic dla heart-vb — wykrywa środowisko (Claude Code CLI vs Cowork), wersję pluginu, status hooków, dependencies (gemini-cli, codex, chrome-devtools-mcp, council CLI), auth providers, gotowość Pattern E/F. Use gdy plugin nie działa lub przed demo/onboardingiem żeby zweryfikować że wszystko jest na miejscu. Trigger przez `/heart-vb:status` lub fraza "sprawdź czy plugin działa".
---

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

## Krok 7 — Action items (CRITICAL — concrete fix commands)

Po zebraniu danych ZAWSZE generuj sekcję **Action items** jeśli wykryjesz problemy. Każdy item musi mieć konkretną komendę do skopiowania, nie ogólnik.

| Wykryty problem | Action item (paste-able command) |
|---|---|
| `Plugin: NIE WYKRYTY` | `/plugin marketplace add The-Heart-Vibe/claude-code-marketplace` → `/plugin install heart-vb@the-heart-vibe` → restart sesji |
| `Hooks: 0/4` mimo plugin OK | Restart Claude Code / Cowork tab — hooks/hooks.json loaduje się przy starcie |
| `Legacy hooks (settings.json): >0` | `bash <(curl -s https://raw.githubusercontent.com/The-Heart-Vibe/claude-code-marketplace/main/plugins/heart-vb/install.sh)` — usuwa legacy z backupem. **WAŻNE: bez tego hooki strzelają 2× per prompt (dual-fire)** |
| `gemini-cli: ❌` | `npm install -g @google/gemini-cli` (wymaga Node.js) → `gemini` (OAuth w przeglądarce) |
| `codex: ⚠️` (Pattern F będzie 2-voice) | Opcjonalne — Codex CLI install + `codex login` (wymaga ChatGPT Plus). Bez Codex pełny Pattern F nadal działa jako 2-voice fallback. |
| `chrome-devtools-mcp: ⚠️` | `claude mcp add chrome-devtools npx chrome-devtools-mcp@latest` → restart sesji |
| `council CLI: ⚠️` | Opcjonalne — działa TYLKO z terminala. W CC/Cowork użyj Pattern F (heart-orchestrate skill) jako workaround |

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
  chrome-devtools ✅/⚠️ <registered/install command>
  council CLI     ✅/⚠️ <terminal-only note>

Pattern readiness:
  Tier 1 (Min)      ✅ <always>
  Tier 2 (Standard) ✅/❌ <reason>
  Tier 3 (Full)     ✅/⚠️ <reason>

Verdict: <one sentence — ready to use / fix X first>

[Action items jeśli są — jak dokończyć setup]
```

## Edge cases

- **Brak `claude` w PATH**: w Cowork pewnie nie ma — fallback na inne sygnały (CLAUDE_PLUGIN_ROOT env)
- **Council doctor failuje w Cowork**: spodziewane — note że terminal-only, nie blocker dla Pattern F
- **Plugin nie wykryty**: oznacza że `/plugin install heart-vb` nie został odpalony w aktualnym environment. Action: `/plugin marketplace add The-Heart-Vibe/claude-code-marketplace` + `/plugin install heart-vb@the-heart-vibe`
- **Legacy hooks present**: backup + clean przez install.sh (run `bash <(curl -s https://raw.githubusercontent.com/The-Heart-Vibe/claude-code-marketplace/main/plugins/heart-vb/install.sh)` z `COUNCIL_INSTALL_HOOK=skip`)

## NIE rób

- Nie spawnuj cowork agents w trakcie diagnostyki — to ma być fast, read-only
- Nie modyfikuj settings.json bez explicit user yes
- Nie odpalaj `council doctor --deep` (zużywa tokeny)
- Nie ask consent przed diagnostyką — to instrument, nie workflow
