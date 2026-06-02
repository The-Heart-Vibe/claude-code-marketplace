---
name: "theheart-frontend"
description: "Build on-brand frontends and UI for The Heart. Use whenever generating React/Tailwind components, pages, or visual artifacts for The Heart products. Loads brand tokens, the canonical component library, and copy/colour/typography rules from the theheart-design-system repo so the output is always on-brand without guessing."
---

# The Heart — Frontend Companion

You are building UI for **The Heart**. The brand is opinionated; every
output must match its tokens, components, and rules verbatim.

The source of truth is a published design system. Treat it as a hard
contract — never invent colour, font, spacing, or pattern values.

---

## Source of truth

Two repos, two roles:

| Repo | Role |
|---|---|
| **theheart-design-system** — https://github.com/wojtekczuba/theheart-design-system | The canonical React + Tailwind design system. `tokens.json`, `tailwind.preset.cjs`, `src/tokens/tokens.css`, `src/components/`, `src/patterns/`, `src/icons/`, `src/logos/`. Pull from here. |
| **The-Heart-Vibe/claude-code-marketplace** (`plugins/pptx-generator`) | Source plugin that *generates* the design system. Edit `brand.yaml` and widgets here, then re-export. |

The instructional brand toolkit (Pitch Deck Toolkit) is the
human-readable spec. It is distributed as a **PDF** (the original
`.pptx` exceeds Claude Design's 20 MB upload limit, so it is flattened
to PDF — same content, same page order, page N in the PDF = slide N
in the deck). Page 11 carries the canonical guideline (Wytyczne).
If code is ambiguous, defer to the PDF's intent.

---

## Setup — bring the design system into the project

Three integration modes, pick the one that fits.

### A) As an npm dependency (preferred for new projects)

```bash
npm install github:wojtekczuba/theheart-design-system
```

Then in `tailwind.config.cjs`:

```js
module.exports = {
  presets: [require("@the-heart-vibe/design-system/tailwind.preset.cjs")],
  content: ["./src/**/*.{ts,tsx}"],
};
```

In `src/main.tsx`:

```ts
import "@the-heart-vibe/design-system/src/tokens/tokens.css";
```

### B) Copy-paste tokens + a single component

If the consumer can't add a dependency, copy:
1. `src/tokens/tokens.css` → into the project's global CSS
2. `tailwind.preset.cjs` → into the project's Tailwind config
3. The specific components you need from `src/components/` /
   `src/patterns/` — they have no implicit dependencies beyond Tailwind
   + Lucide-style SVGs.

### C) For Claude Design / Figma generation

Point the design tool at the design-system repo URL. Paste the
"Other notes" prompt from `prompts/claude-design-other-notes.md` in
the design-system repo, and attach the brand toolkit PDF in the
project's assets (the original `.pptx` is too large to upload — use
the PDF export, page numbering matches the deck 1:1).

---

## Hard brand rules — break these and the output is wrong

### Colour palette

| Token | Hex | Role |
|---|---|---|
| `--th-color-primary` | `#E61B25` | Main brand red. Dominant accent. Headlines, primary CTAs, key bars, status pills. |
| `--th-color-black` | `#000000` | Primary text + dominant heavy accents. |
| `--th-color-green` | `#13A538` | Positive / done state. |
| `--th-color-blue` | `#0056A4` | **"Accent if needed" — use sparingly.** Never the status colour for "in progress". |
| `--th-color-red-light` | `#E9787E` | Soft accent / "at risk" state. |
| `--th-color-gray-1` | `#969696` | Secondary text, captions. |
| `--th-color-gray-2` | `#E6E6E6` | Borders, dividers. |
| `--th-color-gray-3` | `#F0F0F0` | Subtle surfaces. |

### Status palette (fixed and intentional)

```
done / on_track     → green   (#13A538)
in_progress / active → BLACK   (#000000)   ← NEVER blue
at_risk / warning   → red_light (#E9787E)
blocked / off_track → red     (#E61B25)
planned / tbd       → gray    (#969696)
```

The "in progress" pill is **black** on purpose. Blue is reserved as an
opt-in accent (e.g. SWOT "Opportunities" quadrant) — using blue for an
in-progress badge breaks the guideline.

### Typography

- **Raleway** (regular / SemiBold / Light). Arial is the documented
  fallback only — never the default choice.
- Size hierarchy lives in `--th-text-*`: `title 36 · h1 28 · h2 20 ·
  section 12 · body 14 · supporting 12 · caption 10`.
- Min font size is **10pt**. Steps between hierarchy levels are
  **≥ 2pt**, prefer even sizes.
- Captions / 10pt are reserved for *reporting* slides — don't use them
  for normal UI body.
- Use Tailwind utilities: `text-th-h1`, `font-heading`, `font-body`,
  `font-light`. Never hardcode `text-2xl` or `text-[28px]`.

### Punctuation in copy

- Em-dash `—` is **banned**. Use a period or comma.
- En-dash `–` is allowed **only** in numeric ranges (`2–4 weeks`).
- Ellipsis `…` is banned.
- No tricolons ("Fast. Simple. Reliable.").
- No rhetorical questions in headlines.

---

## Component library — what to use, when

### Atomic widgets (`src/components/`)

| Component | Use for |
|---|---|
| `KPITile` | Single metric with optional trend arrow and status colour. |
| `PersonCard` | Team member: name + role + 1-sentence bio. |
| `BigStat` | One huge number with caption — for hero / cover moments. |
| `StatusPill` | Status badge (`done`/`in_progress`/`at_risk`/`blocked`/`planned`). |
| `Badge` | Generic filled pill — `primary`/`black`/`gray`/`outline`. |
| `BulletList` | 4 variants from guideline: `filled-circle`, `filled-square`, `numbered`, `plain`. Nested children render with the secondary marker automatically. |
| `Arrow` | Solid / dotted arrow in any direction. Black by default. |
| `Symbol` | Standalone glyphs: `check` (green), `cross` (red), `dot` (amber). |
| `TimelineEvent` | Dot + date + label, optionally coloured by status. |
| `ComparisonRow` | Row in a competitor matrix: label + booleans/strings per column. |
| `Divider` | Thin horizontal line. |
| `SectionLabel` | Small uppercase red eyebrow for section headers. |
| `BrandFooter` | "The Heart. All rights reserved." + page number. Wired into `SlideShell`. |
| `DecorativeCorner` | Abstract grey triangles + dotted lines for slide corners. |

### Slide patterns (`src/patterns/`)

Wrap content. Most use `SlideShell` automatically — don't duplicate
chrome inside the body.

| Pattern | Use for |
|---|---|
| `SlideShell` | Standard chrome: vertical red bar left, eyebrow, decorative corner, footer + page number. |
| `Cover` | First slide. Signature red triangle bottom-right. |
| `Problem3Col` | Problem framed as 3 stats with supporting text. |
| `OKRBoard` | Single objective + up to 3 KRs with current/target + status pill. |
| `SWOTGrid` | 4-quadrant SWOT analysis. |
| `Roadmap` | Horizontal timeline of milestones. |
| `CompetitiveMatrix` | Feature × competitor table. Own column highlighted red. |
| `BigQuote` | Full-screen quote on red background. |
| `BeforeAfter` | A → B comparison with arrow between. |
| `ValueProp` | Per-segment value proposition (pain / gain). |
| `CustomerJourney` | Numbered steps connected by a horizontal line. |
| `WeeklyStatus` | RAG status by workstream. |

### Logos (`src/logos/`)

```tsx
<Logo variant="horizontal" height={32} />
<Logo variant="vertical"   theme="white" height={96} />
<Logo variant="icon"       theme="black" height={64} />
```

- **3 variants**: `horizontal` (2.86:1), `vertical` (1.24:1), `icon` (0.66:1).
  Ratios extracted from real PNGs — pass **one** of `width`/`height`,
  never both.
- **3 themes**: `color` (default brand red) / `white` (for dark
  surfaces) / `black` (monochrome for photo overlays).

### Icons (`src/icons/`)

```tsx
<Icon name="building-2" size={36} />
<Icon name="bank" />              {/* alias resolves to building-2 */}
<Icon name="shield" color="var(--th-color-black)" />
```

41 Lucide icons bundled. Defaults to brand red. `name` accepts canonical
names or any alias from `icon-manifest.json`.

---

## Decision tree — which pattern fits the brief?

| Brief | Pattern |
|---|---|
| First slide, title + tagline | `Cover` |
| State a single bold claim | `BigQuote` |
| Three stats / 3 root causes | `Problem3Col` |
| Quarterly OKR review | `OKRBoard` |
| SWOT analysis | `SWOTGrid` |
| Show a timeline of milestones | `Roadmap` |
| Compare us vs N competitors | `CompetitiveMatrix` |
| Show how a user flows through the product | `CustomerJourney` |
| Per-segment value prop | `ValueProp` |
| Project status per workstream (RAG) | `WeeklyStatus` |
| Before / after change | `BeforeAfter` |

For non-slide UI (dashboards, forms, settings): compose from atomic
widgets. `KPITile` grids and `StatusPill` rows cover most cases.

---

## Showcase as living spec

`src/examples/Showcase.tsx` in the design-system repo is the canonical
visual reference. It contains:

1. A **Wytyczne** section replicating slide 11 of the brand toolkit
   (Fonts / Icons / Bullets / Arrows / Symbols + Main vs Accent palette).
2. A **Logotypes** section: 3 variants × 3 themes = 9 lock-ups.
3. A full catalogue of every widget and every slide pattern with
   realistic data.

When in doubt, mirror what Showcase does for a similar shape.

---

## What to do when the brief asks for something not in the system

1. **First, compose.** Almost everything reduces to atomic widgets + a
   `SlideShell` or plain Tailwind container.
2. **Reach for free tokens, never raw colours.** Even when extending,
   use `var(--th-color-*)` / `bg-th-*` so the result tracks future
   brand updates.
3. **Don't introduce new fonts, new accent colours, or new bullet
   styles.** Those are guideline-level decisions — flag the gap to the
   user rather than improvising.
4. **If you need a new pattern**, propose it as an addition to the
   plugin (`layouts/generic/*.py` and `design_system/patterns.py`).

---

## Quick checks before declaring a UI done

- [ ] Every colour comes from a `--th-color-*` token or Tailwind `th-*`
      utility — no hardcoded hex.
- [ ] Every text element uses Raleway via `font-heading` / `font-body`
      or `font-light`.
- [ ] No blue in headings or status colours.
- [ ] No em-dashes in copy, no ellipses, no tricolons.
- [ ] If a status appears, it uses one of the five fixed values.
- [ ] Logo is rendered via `<Logo/>`, not as a free `<img>`.
- [ ] If the screen mirrors a slide pattern, it wraps in `SlideShell`.
