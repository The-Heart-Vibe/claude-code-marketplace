"""before_after — left/right comparison with arrow.

Spec:
  { "layout": "before_after",
    "title": "...",
    "before": { "heading": "Before", "bullets": ["Wait 8 min for waiter", "Pay in cash"] },
    "after":  { "heading": "After",  "bullets": ["30s self-order",       "Cashless split"] }
  }
"""
from ..base import add_slide, set_notes
from ..widgets import text_box, rounded_rect


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)

    text_box(slide, prs, 0.05, 0.04, 0.90, 0.08,
             text=spec.get("title", ""), size_pt=22, bold=True,
             color=brand["colors"]["black"])

    block_top = 0.20
    block_h = 0.70

    # Before
    rounded_rect(slide, prs, 0.05, block_top, 0.42, block_h,
                 fill_color="#FFFFFF",
                 line_color=brand["colors"]["gray_2"])
    text_box(slide, prs, 0.06, block_top + 0.02, 0.40, 0.06,
             text=(spec.get("before") or {}).get("heading", "Before"),
             size_pt=14, bold=True, color=brand["colors"]["gray_1"])
    before_body = "\n".join(f"• {b}" for b in (spec.get("before") or {}).get("bullets", []))
    text_box(slide, prs, 0.06, block_top + 0.10, 0.40, block_h - 0.12,
             text=before_body, size_pt=13,
             color=brand["colors"]["black"])

    # Arrow centre
    text_box(slide, prs, 0.47, block_top + block_h / 2 - 0.05,
             0.06, 0.10,
             text="→", size_pt=44, bold=True,
             color=brand["colors"]["primary"],
             align="center", anchor="middle")

    # After
    rounded_rect(slide, prs, 0.53, block_top, 0.42, block_h,
                 fill_color="#FFFFFF",
                 line_color=brand["colors"]["primary"])
    text_box(slide, prs, 0.54, block_top + 0.02, 0.40, 0.06,
             text=(spec.get("after") or {}).get("heading", "After"),
             size_pt=14, bold=True, color=brand["colors"]["primary"])
    after_body = "\n".join(f"• {b}" for b in (spec.get("after") or {}).get("bullets", []))
    text_box(slide, prs, 0.54, block_top + 0.10, 0.40, block_h - 0.12,
             text=after_body, size_pt=13,
             color=brand["colors"]["black"])

    set_notes(slide, spec.get("notes"))
    return slide
