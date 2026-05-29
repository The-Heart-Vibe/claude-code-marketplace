"""big_quote — full-screen quote, no chrome competing with it.

Spec:
  { "layout": "big_quote",
    "quote":       "Banks spend 14 months building what we ship in 4 weeks.",
    "attribution": "Head of Innovation, Top 5 EU bank"
  }
"""
from ..base import add_slide, set_notes
from ..widgets import text_box, filled_rect


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)

    quote = spec.get("quote") or spec.get("title", "")
    attribution = spec.get("attribution", "")

    # Big quote marks accent
    text_box(slide, prs, 0.06, 0.10, 0.08, 0.20,
             text="“", size_pt=120, bold=True,
             color=brand["colors"]["primary"], anchor="top")

    text_box(slide, prs, 0.10, 0.25, 0.80, 0.40,
             text=quote, size_pt=32, bold=True,
             color=brand["colors"]["black"],
             align="left", anchor="middle")

    if attribution:
        filled_rect(slide, prs, 0.10, 0.70, 0.05, 0.005,
                    fill_color=brand["colors"]["primary"])
        text_box(slide, prs, 0.10, 0.72, 0.80, 0.08,
                 text=attribution, size_pt=14,
                 color=brand["colors"]["gray_1"])

    set_notes(slide, spec.get("notes"))
    return slide
