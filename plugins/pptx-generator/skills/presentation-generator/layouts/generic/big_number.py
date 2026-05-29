"""big_number — one statistic gets the whole slide.

Spec:
  {
    "layout": "big_number",
    "number":  "€4.2B",
    "caption": "uncaptured loyalty revenue in CEE alone"
  }
"""
from ..base import add_slide, placeholder, set_text, set_notes


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)
    set_text(placeholder(slide, layout_cfg, "number"),  spec.get("number", ""))
    set_text(placeholder(slide, layout_cfg, "caption"), spec.get("caption", ""))
    set_notes(slide, spec.get("notes"))
    return slide
