"""partnership_model — money flow + value flow between parties.

Spec:
  { "layout": "partnership_model",
    "title": "...",
    "parties": [
      { "name": "Customer",  "role": "pays full price",      "value": "100%" },
      { "name": "ScanPay",   "role": "platform fee",         "value": "10%"  },
      { "name": "Restaurant","role": "receives revenue",     "value": "90%"  }
    ]
  }
"""
from ..base import add_slide, set_notes
from ..widgets import text_box, rounded_rect, filled_rect


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)

    text_box(slide, prs, 0.05, 0.04, 0.90, 0.08,
             text=spec.get("title", ""), size_pt=22, bold=True,
             color=brand["colors"]["black"])

    parties = spec.get("parties", [])[:4]
    if not parties:
        set_notes(slide, spec.get("notes"))
        return slide

    n = len(parties)
    gutter = 0.04
    col_w = (1 - 2 * 0.05 - (n - 1) * gutter) / n
    block_top = 0.30
    block_h = 0.40

    # Arrows / connectors between parties
    arrow_y = block_top + block_h / 2
    filled_rect(slide, prs, 0.05 + col_w, arrow_y, 1 - 2 * 0.05 - col_w, 0.002,
                fill_color=brand["colors"]["gray_2"])

    for i, p in enumerate(parties):
        left = 0.05 + i * (col_w + gutter)
        rounded_rect(slide, prs, left, block_top, col_w, block_h,
                     fill_color="#FFFFFF",
                     line_color=brand["colors"]["primary"])
        # Value badge (red)
        text_box(slide, prs, left, block_top + 0.02,
                 col_w, 0.10,
                 text=p.get("value", ""), size_pt=28, bold=True,
                 color=brand["colors"]["primary"],
                 align="center", anchor="middle")
        # Name
        text_box(slide, prs, left, block_top + 0.14,
                 col_w, 0.08,
                 text=p.get("name", ""), size_pt=14, bold=True,
                 color=brand["colors"]["black"],
                 align="center", anchor="middle")
        # Role
        text_box(slide, prs, left + 0.005, block_top + 0.24,
                 col_w - 0.01, block_h - 0.26,
                 text=p.get("role", ""), size_pt=11,
                 color=brand["colors"]["gray_1"],
                 align="center")

    set_notes(slide, spec.get("notes"))
    return slide
