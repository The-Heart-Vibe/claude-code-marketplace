"""gtm_strategy — go-to-market plan as ordered phases.

Spec:
  { "layout": "gtm_strategy",
    "title": "...",
    "phases": [
      { "label": "Phase 1: Warsaw pilot",   "timeframe": "Q1 2026", "targets": ["10 restaurants", "200 daily orders"] },
      { "label": "Phase 2: Poland rollout", "timeframe": "Q2–Q3",   "targets": ["100 restaurants", "5 cities"]   },
      { "label": "Phase 3: CEE expansion",  "timeframe": "Q4 2026", "targets": ["3 countries", "500 restaurants"] }
    ]
  }
"""
from ..base import add_slide, set_notes
from ..widgets import text_box, rounded_rect, badge


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)

    text_box(slide, prs, 0.05, 0.04, 0.90, 0.08,
             text=spec.get("title", ""), size_pt=22, bold=True,
             color=brand["colors"]["black"])

    phases = spec.get("phases", [])[:4]
    if not phases:
        set_notes(slide, spec.get("notes"))
        return slide

    n = len(phases)
    gutter = 0.02
    col_w = (1 - 2 * 0.05 - (n - 1) * gutter) / n
    block_top = 0.18
    block_h = 0.74

    for i, ph in enumerate(phases):
        left = 0.05 + i * (col_w + gutter)
        rounded_rect(slide, prs, left, block_top, col_w, block_h,
                     fill_color="#FFFFFF",
                     line_color=brand["colors"]["gray_2"])
        # Timeframe badge
        badge(slide, prs, left + 0.01, block_top + 0.02,
              col_w - 0.02, 0.05,
              text=ph.get("timeframe", ""),
              color=brand["colors"]["primary"], text_color="#FFFFFF")
        # Label
        text_box(slide, prs, left + 0.01, block_top + 0.09,
                 col_w - 0.02, 0.10,
                 text=ph.get("label", ""), size_pt=14, bold=True,
                 color=brand["colors"]["black"])
        # Targets list
        targets = ph.get("targets", [])
        target_text = "\n".join(f"• {t}" for t in targets)
        text_box(slide, prs, left + 0.01, block_top + 0.22,
                 col_w - 0.02, block_h - 0.24,
                 text=target_text, size_pt=11,
                 color=brand["colors"]["gray_1"])

    set_notes(slide, spec.get("notes"))
    return slide
