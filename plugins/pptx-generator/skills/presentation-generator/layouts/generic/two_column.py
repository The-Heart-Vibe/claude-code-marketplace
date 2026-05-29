"""two_column — title + left + right.

Useful for comparison, options A/B, before/after, pros/cons, and the
competition slide of a pitchdeck.

Spec:
  {
    "layout": "two_column",
    "title":  "...",
    "left":   { "heading": "Option A", "bullets": [...] },
    "right":  { "heading": "Option B", "bullets": [...] }
  }
"""
from ..base import add_slide, placeholder, set_text, set_notes


def _column_text(col_spec: dict) -> str:
    heading = col_spec.get("heading", "")
    bullets = col_spec.get("bullets", [])
    parts = []
    if heading:
        parts.append(heading)
    parts.extend(f"• {b}" for b in bullets)
    return "\n".join(parts)


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)
    set_text(placeholder(slide, layout_cfg, "title"), spec.get("title", ""))
    set_text(placeholder(slide, layout_cfg, "left"),  _column_text(spec.get("left", {})))
    set_text(placeholder(slide, layout_cfg, "right"), _column_text(spec.get("right", {})))
    set_notes(slide, spec.get("notes"))
    return slide
