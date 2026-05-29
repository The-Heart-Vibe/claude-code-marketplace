"""main_point — single large centred statement.

Use for a punchy mission line, a single bold claim, or a strong quote.

Spec:
  { "layout": "main_point", "title": "..." }
"""
from ..base import add_slide, placeholder, set_text, set_notes


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)
    set_text(placeholder(slide, layout_cfg, "title"), spec.get("title", ""))
    set_notes(slide, spec.get("notes"))
    return slide
