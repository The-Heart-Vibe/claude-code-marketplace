"""value_prop — per-segment value proposition.

Spec:
  { "layout": "value_prop",
    "title": "...",
    "segments": [
      { "name": "For customers",   "pain": "Long wait times.",  "gain": "30s self-order." },
      { "name": "For restaurants", "pain": "Staff shortage.",   "gain": "Higher turnover." },
      { "name": "For waiters",     "pain": "Errors and stress", "gain": "Cashless tips."  }
    ]
  }
"""
from ..base import add_slide, set_notes
from ..widgets import text_box, rounded_rect


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)

    text_box(slide, prs, 0.05, 0.04, 0.90, 0.08,
             text=spec.get("title", ""), size_pt=22, bold=True,
             color=brand["colors"]["black"])

    segments = spec.get("segments", [])[:3]
    if not segments:
        set_notes(slide, spec.get("notes"))
        return slide

    n = len(segments)
    gutter = 0.02
    col_w = (1 - 2 * 0.05 - (n - 1) * gutter) / n
    col_h = 0.74

    for i, seg in enumerate(segments):
        left = 0.05 + i * (col_w + gutter)
        rounded_rect(slide, prs, left, 0.16, col_w, col_h,
                     fill_color="#FFFFFF",
                     line_color=brand["colors"]["gray_2"])
        # Name banner (red)
        text_box(slide, prs, left, 0.16, col_w, 0.06,
                 text=seg.get("name", ""), size_pt=14, bold=True,
                 color=brand["colors"]["primary"],
                 align="center", anchor="middle")
        # Pain
        text_box(slide, prs, left + 0.01, 0.24, col_w - 0.02, 0.04,
                 text="PAIN", size_pt=9, bold=True,
                 color=brand["colors"]["gray_1"])
        text_box(slide, prs, left + 0.01, 0.28, col_w - 0.02, 0.18,
                 text=seg.get("pain", ""), size_pt=12,
                 color=brand["colors"]["black"])
        # Gain
        text_box(slide, prs, left + 0.01, 0.50, col_w - 0.02, 0.04,
                 text="GAIN", size_pt=9, bold=True,
                 color=brand["colors"]["green"])
        text_box(slide, prs, left + 0.01, 0.54, col_w - 0.02, 0.30,
                 text=seg.get("gain", ""), size_pt=12,
                 color=brand["colors"]["black"])

    set_notes(slide, spec.get("notes"))
    return slide
