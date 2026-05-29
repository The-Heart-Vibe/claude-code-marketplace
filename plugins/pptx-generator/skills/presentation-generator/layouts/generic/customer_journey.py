"""customer_journey — N-step process or user flow.

Spec:
  { "layout": "customer_journey",
    "title": "...",
    "steps": [
      { "label": "Discover", "body": "User finds restaurant on Google Maps." },
      { "label": "Order",    "body": "Scans QR; browses menu in 30s." },
      { "label": "Pay",      "body": "Splits with friends; tips digitally." },
      { "label": "Return",   "body": "Loyalty points trigger repeat visit." }
    ]
  }
"""
from ..base import add_slide, set_notes
from ..widgets import text_box, circle, filled_rect


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)

    text_box(slide, prs, 0.05, 0.04, 0.90, 0.08,
             text=spec.get("title", ""), size_pt=22, bold=True,
             color=brand["colors"]["black"])

    steps = spec.get("steps", [])[:5]
    if not steps:
        set_notes(slide, spec.get("notes"))
        return slide

    n = len(steps)
    gutter = 0.02
    col_w = (1 - 2 * 0.05 - (n - 1) * gutter) / n
    block_top = 0.25
    block_h = 0.60

    # Connecting line between circles
    filled_rect(slide, prs, 0.05 + col_w / 2, block_top + 0.04,
                1 - 2 * 0.05 - col_w, 0.002,
                fill_color=brand["colors"]["gray_2"])

    for i, step in enumerate(steps):
        left = 0.05 + i * (col_w + gutter)
        cx = left + col_w / 2 - 0.02

        # Step number circle
        circle(slide, prs, cx, block_top, 0.05,
               fill_color=brand["colors"]["primary"])
        text_box(slide, prs, cx, block_top, 0.05, 0.05,
                 text=str(i + 1), size_pt=18, bold=True,
                 color="#FFFFFF", align="center", anchor="middle")

        # Label below circle
        text_box(slide, prs, left, block_top + 0.10,
                 col_w, 0.06,
                 text=step.get("label", ""), size_pt=14, bold=True,
                 color=brand["colors"]["black"],
                 align="center", anchor="middle")

        # Body below label
        text_box(slide, prs, left, block_top + 0.18,
                 col_w, block_h - 0.18,
                 text=step.get("body", ""), size_pt=11,
                 color=brand["colors"]["gray_1"],
                 align="center")

    set_notes(slide, spec.get("notes"))
    return slide
