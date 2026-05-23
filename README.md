# The Heart Vibe — Claude Code Marketplace

Wewnętrzny marketplace pluginów Claude Code dla zespołu The Heart Vibe.

## Jak dodać marketplace

W Claude Code:

```
/plugin marketplace add The-Heart-Vibe/claude-code-marketplace
```

Następnie zainstaluj wybrany plugin:

```
/plugin install council@the-heart-vibe
```

## Dostępne pluginy

| Plugin | Opis | Status |
|--------|------|--------|
| [`council`](plugins/council) | Multi-LLM debate (Claude + Codex + Gemini) z routingiem domain × tier dla decyzji tech i non-tech | ✅ stable |

## Kolekcje (kuratorskie zestawy per rola)

Kolekcje to **dokumentacja** — grupują polecane skille z różnych źródeł per faza pracy. Nie są bundle pluginami; każdy skill instalujesz osobno.

| Kolekcja | Dla kogo | Skille |
|----------|----------|--------|
| [Venture Builder](collections/venture-builder.md) | Analitycy + konsultanci VB | 18 skilli pogrupowanych w 6 faz: discovery, validation, strategy, modeling, build prep, IC/pitch |

Więcej kolekcji w [`collections/`](collections/).

## Dodawanie nowego pluginu

1. Stwórz katalog `plugins/<nazwa>/` z:
   - `.claude-plugin/plugin.json` — metadata
   - `skills/<nazwa>/SKILL.md` — body skilla
   - `README.md` — instrukcje setup i użycia
   - `install.sh` (opcjonalnie) — automatyzacja instalacji zależności
2. Dodaj wpis do `.claude-plugin/marketplace.json`
3. PR z opisem do czego ten plugin służy i jak był testowany
4. Po merge teammate'y robią `/plugin update council@the-heart-vibe` żeby pociągnąć zmiany

## Konwencje

- **Język:** polski w treści, angielski w `description` (dla skanowania przez Claude)
- **Paths:** używaj `$HOME` lub env-overridable zmiennych, nie hardcoded `/Users/...`
- **Provider keys:** unikaj wymuszania API keys jeśli da się przez CLI auth (jak w `council`)
- **Sekrety:** nigdy do repo. `.example.yaml` zamiast prawdziwych configów

## Licencja

MIT — wewnętrzne narzędzia, ale otwarte na opensourceing jeśli zdecydujemy.
