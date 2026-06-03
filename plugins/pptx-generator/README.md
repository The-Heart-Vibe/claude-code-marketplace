# pptx-generator

> **Status: stable (v1.0.0)** — production-ready, templates bundled, brand tokens auto-applied.

Two-mode plugin for The Heart brand. One source of truth (`brand.yaml` + Python widgets) drives both outputs.

```
/plugin marketplace add The-Heart-Vibe/claude-code-marketplace
/plugin install pptx-generator@the-heart-marketplace
```

---

## Mode 1 — PPTX deck generator

Claude acts as creative director. You give a topic or brief; it plans the narrative, proposes a slide outline for approval, then calls `generate.py` to produce a branded `.pptx` file using the correct template.

```bash
python3 generate.py --spec spec.json --output deck.pptx
```

### Coverage

- **33 generic layouts** (cover, content, two_column, three_column, stat_pair, table_grid, big_number, chart, traction, roadmap, comparison_matrix, value_prop, customer_journey, founder_story, partnership_model, gtm_strategy, okr, risk_matrix, swot, weekly_status, retro, decision_log, gantt, big_quote, testimonial, before_after, agenda, faq, image_grid, …)
- **13 pitch sections** with consultant checklists (cover, purpose, problem, solution, why_now, market_size, competition, product, business_model, financials, team, investment, contact)
- **10 pre-built narratives** (`investor_pitch`, `short_pitch`, `product_overview`, `internal_update`, `status_report`, `board_update`, `retro_review`, `project_kickoff`, `quarterly_planning`, `workshop_deck`)
- **9 chart types** (bar, horizontal_bar, stacked_bar, line, pie, donut, waterfall, funnel)
- **9 brand-chrome variants** auto-applied per slide (cover_minimal/split/statement, section, section_filled, content, content_minimal, closing, data_heavy)

### Templates (bundled)

| Template | Use for |
|---|---|
| `blank.pptx` | Internal decks, status reports, OKR reviews, workshops |
| `pitchdeck-toolkit.pptx` | Investor pitches, client proposals, external materials |

Both templates are stripped to Slide Master only; brand chrome (Raleway font, red footer bar, logo, page numbers, section eyebrow, decorative corners) is applied programmatically per slide so the output stays consistent across templates.

---

## Mode 2 — Design system exporter

Same brand tokens + widget definitions, exported as a Claude-Design-importable React + Tailwind repo.

```bash
python3 export_design_system.py --output ./dist/design-system
```

Produces a git-ready repo containing:

- **`tokens.json`** — W3C Design Tokens (DTCG format)
- **`tokens.css`** — 23 CSS custom properties (`--th-*`)
- **`tailwind.preset.cjs`** — Tailwind theme extending brand tokens
- **14 React components** — Arrow, Badge, BigStat, BrandFooter, BulletList (4 variants), ComparisonRow, DecorativeCorner, Divider, KPITile, PersonCard, SectionLabel, StatusPill, Symbol, TimelineEvent
- **12 slide patterns** — Cover, Problem3Col, OKRBoard, SWOTGrid, Roadmap, CompetitiveMatrix, BigQuote, BeforeAfter, ValueProp, CustomerJourney, WeeklyStatus, SlideShell
- **41 Lucide icons** — typed `<Icon name="…"/>` with brand tinting + alias manifest
- **Showcase page** — replica of the brand guideline slide (Wytyczne) + full pattern catalogue

Paste the resulting repo URL into Claude Design (`Setup → design-system → repo URL`).

---

## Architecture

```
skills/presentation-generator/
  SKILL.md                  Intent-driven instructions for Claude
  brand.yaml                Authoritative brand tokens (colours, typography, sizing)
  template_map.yaml         Master-layout-index map per template (Pitch + Blank)
  generate.py               PPTX deck engine
  export_design_system.py   Design-system exporter CLI
  layouts/
    base.py                 Placeholder + autofit helpers
    brand_chrome.py         9 chrome variants (cover/section/content/closing/...)
    colors.py               Semantic colour helpers (status, trend, accent palette)
    widgets.py              Composable atoms (KPI tile, person card, badges, ...)
    generic/                33 layout builders
    pitch/                  13 semantic pitch section builders
  narrative/
    pitchdeck.yaml          22 sections + 3 narratives for investor decks
    general.yaml            20 sections + 10 narratives for internal decks
  design_system/             Exporter modules
    tokens.py               DTCG / CSS / Tailwind generators
    components.py           React widget templates
    patterns.py             React slide-pattern templates
    icons.py                Icon library exporter
    scaffold.py             Vite + Tailwind + tsconfig scaffolding
    exporter.py             Orchestrator
  brand_assets/             th-horizontal.png, th-vertical.png, th-icon.png
  icons/svgs/               41 Lucide SVGs
  icons/icon_manifest.json  Alias → canonical + categories
  templates/
    blank.pptx              ~3 MB (Slide Master only)
    pitchdeck-toolkit.pptx  ~13 MB (Slide Master only)
```

---

## Brand rules baked in

- **Primary red `#E61B25`** dominates the visual.
- **Blue `#0056A4`** is "accent if needed" — never used for status pills (an "in progress" pill is **black**, not blue).
- **Raleway** + Raleway SemiBold + Raleway Light, with Arial as the documented fallback.
- **Min font size 10pt**, step of 2pt between hierarchy levels, prefer even sizes (per slide-10 guideline of blank.pptx).
- **Logo aspect ratios** measured from PNG sources (`th-horizontal` = 2.86:1, `th-vertical` = 1.244:1, `th-icon` = 0.66:1) — no stretching.
- **Status palette**: `done`/`on_track` → green, `in_progress`/`active` → black, `at_risk` → red-light, `blocked` → red, `planned` → gray.
