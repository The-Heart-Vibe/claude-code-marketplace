"""quote — strong customer quote or bold claim on the MAIN_POINT layout.

Spec:
  {
    "layout": "quote",
    "quote":       "Banks spend 14 months building what we ship in 4 weeks.",
    "attribution": "Head of Innovation, Top 5 EU bank"   # optional
  }
"""
from ..base import add_slide, placeholder, set_text, set_notes


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)
    text = spec.get("quote") or spec.get("title", "")
    attribution = spec.get("attribution")

    rendered = f'"{text}"' if text else ""
    if attribution:
        rendered += f"\n— {attribution}"
    set_text(placeholder(slide, layout_cfg, "title"), rendered)

    set_notes(slide, spec.get("notes"))
    return slide
