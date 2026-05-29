"""roadmap — horizontal timeline of milestones.

Spec:
  { "layout": "roadmap",
    "title": "...",
    "milestones": [
      { "date": "Q1 2026", "label": "Beta launch",      "status": "done"        },
      { "date": "Q2 2026", "label": "10 paying clients", "status": "in_progress" },
      { "date": "Q3 2026", "label": "Series A",         "status": "planned"     }
    ]
  }
"""
from ..base import add_slide, set_notes
from ..widgets import text_box, timeline_event, divider


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)

    text_box(slide, prs, 0.05, 0.04, 0.90, 0.08,
             text=spec.get("title", ""), size_pt=22, bold=True,
             color=brand["colors"]["black"])

    milestones = spec.get("milestones", [])[:6]
    if not milestones:
        set_notes(slide, spec.get("notes"))
        return slide

    # Horizontal line through middle
    line_y = 0.45
    divider(slide, prs, 0.05, line_y, 0.90,
            color=brand["colors"]["gray_2"], thickness=0.003)

    # Events distributed along the line
    n = len(milestones)
    span = 0.84
    step = span / max(n - 1, 1)
    for i, m in enumerate(milestones):
        cx = 0.08 + i * step
        timeline_event(
            slide, prs,
            cx - 0.06, line_y - 0.10,
            0.12, 0.20,
            date=m.get("date", ""),
            label=m.get("label", ""),
            status_key=m.get("status"),
            brand=brand,
        )

    set_notes(slide, spec.get("notes"))
    return slide
