# council — multi-LLM debate plugin

Wrapper na `the-llm-council` z routingiem **domain × tier** dla decyzji technicznych i biznesowych. Trzy providerzy bez API keys: Claude Code, Codex (ChatGPT Plus), Gemini CLI (Google Workspace OAuth).

## Instalacja

Po `/plugin install council@the-heart-vibe` zostanie odpalony `install.sh`, który:

1. Sprawdza/instaluje `uv` (Python package manager)
2. Sprawdza Node.js (wymagany dla Gemini CLI)
3. Instaluje globalnie `@google/gemini-cli` jeśli brak
4. Tworzy izolowany venv w `~/tools/council-env`
5. Instaluje `the-llm-council[gemini]>=0.7.16`
6. Tworzy wrapper w `~/.local/bin/council`
7. Kopiuje config template do `~/.config/llm-council/config.yaml`
8. Odpala `council doctor` i pokazuje status providerów

### Ręczna instalacja

```bash
bash <(curl -s https://raw.githubusercontent.com/The-Heart-Vibe/claude-code-marketplace/main/plugins/council/install.sh)
```

### Override paths

```bash
COUNCIL_VENV=/custom/path/venv \
COUNCIL_WRAPPER_DIR=/custom/bin \
bash install.sh
```

## Auth providerów

Po instalacji odpal `council doctor`. Jeśli któryś provider `FAIL`:

| Provider | Jak zalogować | Skąd tokeny |
|----------|---------------|-------------|
| `claude` | Już zalogowany jeśli używasz Claude Code | ❌ **NIE DZIAŁA z poziomu aktywnej Claude Code session** (self-invocation block) — używaj tylko z terminala |
| `codex` | `codex login` | ChatGPT Plus/Pro |
| `gemini-cli` | `gemini` (otworzy przeglądarkę → OAuth) | Google Workspace |

## Użycie w Claude Code

Po zainstalowaniu skill, w sesji:

```
/council Pricing: $19/49 vs $29/79 dla SMB SaaS, target ARR $1M/12mc
```

Claude:
1. Klasyfikuje **domain** (tech vs non-tech) — tu: non-tech (pricing)
2. Klasyfikuje **tier** (S/M/L/XL) — tu: L (decyzja z kontekstem)
3. Dobiera subagent (`planner --mode assess`), providerów (`gemini-cli,codex`), personę (`pricing analyst`)
4. Buduje komendę z `--context "<persona>"` i `--json`
5. Parsuje wynik i prezentuje **streszczenie ~15 linii** (decyzja, confidence, warunki, top alternatywy)

## Tier × Domain matrix

| Tier | TECH | NON-TECH |
|------|------|----------|
| **S** quick fix / quick copy | `drafter --mode impl` solo gemini-cli | `critic --mode review` solo gemini-cli + persona |
| **M** implementacja / copy review | `drafter` lub `critic review` + 2 providerzy | `critic review` lub `researcher` + 2 providerzy + persona |
| **L** feature / pricing | `drafter --mode arch` lub `planner` + 2 providerzy | `planner --mode assess/plan` + 2 providerzy + persona |
| **XL** architektura / strategia | `drafter --mode arch` lub `critic --mode security` | `planner --mode plan` + persona VP/C-level |

## Bezpośrednie użycie z terminala

```bash
# TECH — Tier L
council run drafter --mode arch "Cache layer: Redis vs in-memory" \
  --providers gemini-cli,codex --json

# NON-TECH — Tier L (mandatory --context!)
council run planner --mode assess \
  "Pricing $19 vs $29 dla SMB SaaS, target ARR $1M/12mc" \
  --providers gemini-cli,codex \
  --context "Jesteś senior pricing analyst. Pomiń tech. 
             Skup się na unit economics, conversion, ARPU, churn." \
  --json
```

## Konfiguracja

`~/.config/llm-council/config.yaml`:

```yaml
defaults:
  providers:
    - gemini-cli   # nie 'claude' — self-invocation block w Claude Code
    - codex
  timeout: 180
```

## Diagnostyka

```bash
council doctor                          # status providerów
council doctor --deep --provider gemini-cli   # live test (zużywa tokeny)
council version
council config --show
```

## Reinstalacja

```bash
rm -rf ~/tools/council-env
bash <(curl -s https://raw.githubusercontent.com/The-Heart-Vibe/claude-code-marketplace/main/plugins/council/install.sh)
```

## Co to nie jest

- **Nie zastępuje normalnej sesji Claude Code** — to drugie zdanie dla decyzji gdzie warto mieć 2-3 perspektywy
- **Nie generuje kodu produkcyjnego** — adversarial drafty + ranking, nie production-ready output
- **Nie zastępuje code review** — jest komplementarne (możesz puścić council critic review obok normalnego PR review)

## Powiązane

- Upstream: [`sherifkozman/the-llm-council`](https://github.com/sherifkozman/the-llm-council)
- Playbook entry: TODO link gdy doda się sekcję AI Tooling w `playbook`
