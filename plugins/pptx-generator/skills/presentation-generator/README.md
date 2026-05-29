# pptx-generator — Presentation Generator

> ⚠️ **Status: WIP — not ready for production**
>
> Core logic is working but the plugin requires manual setup (templates must be downloaded separately) and the layout-to-slide mappings for both templates need refinement. Use at your own risk.

Generates branded `.pptx` presentations from a topic or brief using The Heart / UZ Venture Studio templates.

```
/plugin marketplace add The-Heart-Vibe/claude-code-marketplace
/plugin install pptx-generator@the-heart-vibe
```

## What it does

Claude acts as creative director — you give a topic or brief, it plans the narrative, proposes a slide outline for approval, then calls `generate.py` to produce a `.pptx` file using the correct branded template.

## Setup required before first use

1. Open [The Heart blank presentation](https://docs.google.com/presentation/d/1WM2yqL2LUVq_tKyBwpwA5yVgUt3ioyCO_KNN_JNBH3g) → File → Download → Microsoft PowerPoint → save as `skills/presentation-generator/templates/blank.pptx`
2. Open [Pitch Deck Toolkit](https://docs.google.com/presentation/d/1h0VwTbQNLZ-hXFEPY_cvJShJZVrtxpj4cYvVFnvuHXs) → File → Download → Microsoft PowerPoint → save as `skills/presentation-generator/templates/pitchdeck-toolkit.pptx`

## Available templates

| Template | Use for |
|----------|---------|
| `blank.pptx` | Internal decks, one-pagers, status updates |
| `pitchdeck-toolkit.pptx` | External pitches, client proposals, investor materials |

## Known issues / what needs fixing before production

- [ ] **Template layout mappings** (`template_map.yaml`) — slide indices for both templates need verification against the actual downloaded PPTX files. The pitchdeck-toolkit has paired instruction+example slides; mappings must point to the clean "example" slides, not instruction slides.
- [ ] **brand.yaml** — colors and fonts are placeholders; need to be confirmed from the official brand guidelines embedded in the Core template Google Slides.
- [ ] **Templates excluded from repo** — too large for git; each user must download manually (see setup above).
- [ ] **generate.py** — OPC package cloning is implemented and tested; the within-package slide duplication approach works. Needs re-testing after correct templates are in place.

## Architecture

```
skills/presentation-generator/
  SKILL.md              — Claude behaviour: planning, copy rules, outline format
  generate.py           — Python engine: reads spec JSON, clones slides, fills content
  brand.yaml            — Brand config: colors, fonts, layout margins
  template_map.yaml     — Maps layout names (cover, content, ...) to slide indices per template
  icons/                — Lucide icon PNGs rendered at 64px
  templates/            — PPTX template files (download manually, see README)
```
