This design system is the source of truth for The Heart brand. Use it
verbatim — every token, component, and pattern below has a reason.

REPO: https://github.com/wojtekczuba/theheart-design-system

ATTACHED INSTRUCTIONAL DOCUMENT

A PDF export of the brand-guideline toolkit is attached in this
project's assets (the original .pptx exceeded the 20 MB upload limit
so it was flattened to PDF — same content, same page order, same
slide numbering, no editable layers needed for reference).

It is the human-readable source the design system was derived from.
When the code is ambiguous, defer to the PDF.

Key pages to consult (1-based — PDF page = original slide number):

  • Pages 1–7   — workflow rules: how to start a new deck, how to copy
                  slides safely, how to manage decorative triangles via
                  the Slide Master.
  • Pages 9–10  — typography: Raleway weights, size hierarchy
                  (10/12/14/16), "min 2pt step between levels, prefer
                  even sizes", "smaller sizes only for reporting slides".
  • Page 11     — THE canonical guideline. Fonts + Icons + Bullets +
                  Arrows + Symbols + Main vs Accent colour split. The
                  Showcase page in this repo replicates this page 1:1.
  • Pages 12–20 — example layouts (cover, section dividers, content)
                  showing the live brand on real slides.
  • Pages 41–45 — Logo + icon usage rules.

Reference these pages when a code component does not show a particular
edge case. The PDF is authoritative on intent; the code is authoritative
on implementation.

CONVENTIONS

• Everything is namespaced `th-`. Use CSS vars `--th-color-*` /
  `--th-font-*` / `--th-text-*` from `src/tokens/tokens.css`, or the
  matching Tailwind utilities (`bg-th-primary`, `text-th-h1`,
  `font-heading`, etc.) from `tailwind.preset.cjs`. Never hardcode hex.

• Font is Raleway (regular / SemiBold / Light). Arial is the documented
  fallback only — do not promote it to a real font choice.

COLOUR RULES — these break easily

• `#E61B25` (brand red) is the dominant accent. Use it for headlines,
  primary CTAs, decorative bars, key triangles, important pills.

• `#0056A4` (brand blue) is labelled "Accent if needed" in the guideline.
  Use it RARELY, only when red would be wrong (e.g. "Opportunities"
  quadrant in a SWOT). NEVER use blue for status colours.

• Status palette is fixed and intentional:
    done / on_track     → green   (#13A538)
    in_progress / active → BLACK   (#000000)   ← not blue
    at_risk / warning   → red_light (#E9787E)
    blocked / off_track → red     (#E61B25)
    planned / tbd       → gray    (#969696)

COMPONENT USAGE

• Slide patterns (`src/patterns/`) wrap content in `<SlideShell>`, which
  auto-applies the red footer bar, page number, section eyebrow, vertical
  red bar on the left, and a decorative top-right corner. Don't duplicate
  that chrome inside the pattern body.

• `<Logo variant="horizontal"|"vertical"|"icon" theme="color"|"white"|"black"
  height={N}/>` — pass ONE of width/height; the other is computed from
  the real PNG aspect ratio. Never set both.

• `<Icon name="building-2" />` — accepts any canonical name OR alias from
  `icon-manifest.json` (e.g. "bank" → "building-2"). Defaults to brand red.

• `<BulletList kind="filled-circle"|"filled-square"|"numbered"|"plain" />`
  — matches the four bullet styles from the brand guideline. Nested
  items render with the secondary marker automatically.

• `<Symbol kind="check"|"cross"|"dot" />` — standalone glyphs in green /
  red / amber. Use inline where a StatusPill would be too heavy.

REFERENCE

`src/examples/Showcase.tsx` is the canonical reference. The first
section replicates page 11 of the brand guideline PDF (Wytyczne); the
rest is a full catalogue of widgets, patterns, and the 9 Logo
combinations. When in doubt: code in Showcase + intent in attached PDF.
