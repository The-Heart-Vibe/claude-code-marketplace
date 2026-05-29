"""
design_system — Export the plugin's brand + widgets as a Claude-Design-ready
git repository.

We already keep authoritative design data in three places:
  * brand.yaml          → colours, typography, spacing
  * layouts/widgets.py  → atomic widgets (KPI tile, person card, badge, ...)
  * layouts/generic/*   → slide patterns built from widgets

The exporter walks those three sources and emits a self-contained
TypeScript + Tailwind + React project that:
  * declares brand tokens in W3C DTCG format (`tokens.json`)
  * exposes them as CSS custom properties (`tokens.css`)
  * provides a Tailwind preset wiring those tokens into utility classes
  * implements every widget + pattern as a TypeScript React component
  * includes an `examples` page that renders one of each

The output directory is a valid git repository that Claude Design accepts
as `setup=design-system → repo URL`.
"""
from .exporter import export_design_system  # noqa: F401
