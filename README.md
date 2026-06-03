# The Heart Vibe — Claude Code Marketplace

Wewnętrzny marketplace pluginów Claude Code dla zespołu The Heart Vibe.

**Zasada:** wszystko w jednym pluginie. **Bez dodawania innych marketplaces.**

## 🚀 Quick start

```
/plugin marketplace add The-Heart-Vibe/claude-code-marketplace
/plugin install heart-vb@the-heart-marketplace
```

I masz całą Venture Builder toolkit — 36 skilli w 8 kategoriach.

Installer (~3 min) zapyta o opt-in Venture Builder hook → **odpowiedz `y`**.

**Nowy w zespole?** → [**Onboarding VB**](collections/onboarding-vb.md) — step-by-step 30 min.

## Plugin

| Plugin | Co zawiera | Status |
|--------|------------|--------|
| [`heart-vb`](plugins/heart-vb) | **36 skilli** w 8 kategoriach: council (multi-LLM debate), self-improving (si:*), vb-research, vb-product, vb-finance, vb-commercial, vb-comms, heart-custom (sector contexts) | ✅ stable v0.5.0 |
| [`pptx-generator`](plugins/pptx-generator) | Generator prezentacji `.pptx` z branded templatek The Heart. Claude jako creative director — temat → outline → gotowy plik. Wymaga ręcznego pobrania templatek. | 🚧 WIP v0.1.0 |

Pełna lista skilli w [plugins/heart-vb/.claude-plugin/plugin.json](plugins/heart-vb/.claude-plugin/plugin.json). Atrybucja upstream'ów: [plugins/heart-vb/skills/ATTRIBUTION.md](plugins/heart-vb/skills/ATTRIBUTION.md).

## Kolekcje (dokumentacja użycia)

| Kolekcja | Dla kogo | Co zawiera |
|----------|----------|------------|
| [Venture Builder map](collections/venture-builder.md) | Analitycy + konsultanci VB | Mapa 36 skilli na 7 faz pracy (discovery → IC) + sector addenda + token-saving practices |
| [Onboarding VB](collections/onboarding-vb.md) | Nowy teammate | Setup w 30 min: install, providery, hook, 3 praktyczne zadania |

## Co odróżnia od poprzedniej wersji (v0.1.0)

Poprzednio: 1 mały plugin (council) + collection wskazująca na 5 zewnętrznych marketplaces.
Teraz: 1 mega-plugin (heart-vb) który **bundluje** wszystkie skille z atrybucją MIT — jedna instalacja, koniec.

## Skille z upstream sources (bundled)

Wszystkie z licencją MIT. Atrybucja w każdym SKILL.md i w [ATTRIBUTION.md](plugins/heart-vb/skills/ATTRIBUTION.md):

- [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) — product-team, finance, commercial, c-level-advisor, engineering-team subdirs
- [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) — research + investor skills
- Heart-custom — sektor-specific context dla HealthTech / Academic spinouts / Energy storage / FinTech (legacy) — reflecting current portfolio focus 2026

Nie auto-syncujemy z upstream — update wymaga ręcznego re-copy + diff review (PR mile widziane).

## Dodawanie nowego skilla do heart-vb

1. Skopiuj SKILL.md do właściwej kategorii pod `plugins/heart-vb/skills/<kategoria>/`
2. Dodaj wpis do `skills` array w `plugins/heart-vb/.claude-plugin/plugin.json`
3. Jeśli z upstream — dodaj wiersz do `ATTRIBUTION.md`
4. PR z opisem use case
5. Teammate'y robią `/plugin update heart-vb@the-heart-marketplace`

## Konwencje

- **Język:** polski w treści, angielski w `description` (dla skanowania przez Claude)
- **Paths:** używaj `$HOME` lub env-overridable zmiennych, nie hardcoded `/Users/...`
- **Provider keys:** unikaj wymuszania API keys jeśli da się przez CLI auth (jak w `council`)
- **Sekrety:** nigdy do repo. `.example.yaml` zamiast prawdziwych configów

## Licencja

- Nasze: MIT
- Upstream: MIT (zobacz [ATTRIBUTION.md](plugins/heart-vb/skills/ATTRIBUTION.md))

Wewnętrzne narzędzie, ale otwarte na opensourceing jeśli zdecydujemy.
