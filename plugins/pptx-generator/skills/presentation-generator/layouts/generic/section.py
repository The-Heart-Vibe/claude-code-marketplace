"""section — narrative divider slide (master: SECTION_HEADER).

Spec:
  { "layout": "section", "title": "..." }
"""
from ..base import add_slide, placeholder, set_text, set_notes


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)
    set_text(placeholder(slide, layout_cfg, "title"), spec.get("title", ""))
    set_notes(slide, spec.get("notes"))
    return slide
