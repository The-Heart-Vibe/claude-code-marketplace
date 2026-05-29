"""okr — single Objective with 3 Key Results.

Spec:
  { "layout": "okr",
    "title": "...",
    "objective": "Become the default payment method for Polish QSRs by end of Q4.",
    "key_results": [
      { "label": "Active restaurants", "target": "200", "current": "117", "status": "on_track" },
      { "label": "MRR",                "target": "150k PLN", "current": "98k PLN", "status": "at_risk" },
      { "label": "NPS",                "target": ">50", "current": "62", "status": "done" }
    ]
  }
"""
from ..base import add_slide, set_notes
from ..widgets import text_box, rounded_rect, status_pill


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)

    text_box(slide, prs, 0.05, 0.04, 0.90, 0.08,
             text=spec.get("title", ""), size_pt=22, bold=True,
             color=brand["colors"]["black"])

    text_box(slide, prs, 0.05, 0.14, 0.07, 0.05,
             text="OBJECTIVE", size_pt=10, bold=True,
             color=brand["colors"]["primary"])
    text_box(slide, prs, 0.05, 0.19, 0.90, 0.14,
             text=spec.get("objective", ""), size_pt=18, bold=True,
             color=brand["colors"]["black"])

    krs = spec.get("key_results", [])[:3]
    if not krs:
        set_notes(slide, spec.get("notes"))
        return slide

    n = len(krs)
    gutter = 0.02
    col_w = (1 - 2 * 0.05 - (n - 1) * gutter) / n
    block_top = 0.40
    block_h = 0.50

    for i, kr in enumerate(krs):
        left = 0.05 + i * (col_w + gutter)
        rounded_rect(slide, prs, left, block_top, col_w, block_h,
                     fill_color="#FFFFFF",
                     line_color=brand["colors"]["gray_2"])
        # KR number
        text_box(slide, prs, left + 0.01, block_top + 0.02,
                 col_w - 0.02, 0.05,
                 text=f"KR {i+1}", size_pt=10, bold=True,
                 color=brand["colors"]["gray_1"])
        # Label
        text_box(slide, prs, left + 0.01, block_top + 0.07,
                 col_w - 0.02, 0.10,
                 text=kr.get("label", ""), size_pt=13, bold=True,
                 color=brand["colors"]["black"])
        # Current / target
        text_box(slide, prs, left + 0.01, block_top + 0.18,
                 col_w - 0.02, 0.10,
                 text=f"{kr.get('current', '?')}  /  {kr.get('target', '?')}",
                 size_pt=20, bold=True,
                 color=brand["colors"]["primary"])
        text_box(slide, prs, left + 0.01, block_top + 0.30,
                 col_w - 0.02, 0.04,
                 text="current / target", size_pt=9,
                 color=brand["colors"]["gray_1"])
        # Status pill
        status_pill(slide, prs, left + 0.01, block_top + 0.40,
                    col_w * 0.50, 0.06,
                    status_key=kr.get("status", "neutral"),
                    brand=brand)

    set_notes(slide, spec.get("notes"))
    return slide
