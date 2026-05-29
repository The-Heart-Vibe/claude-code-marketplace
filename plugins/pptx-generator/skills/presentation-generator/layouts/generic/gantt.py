"""gantt — horizontal bars across a unit-less time axis.

Spec:
  { "layout": "gantt",
    "title": "...",
    "periods": ["Q1", "Q2", "Q3", "Q4"],     # column headers
    "tasks": [
      { "label": "Discovery",     "start": 0, "end": 1, "status": "done"        },
      { "label": "Build MVP",     "start": 1, "end": 3, "status": "in_progress" },
      { "label": "Launch + GTM",  "start": 3, "end": 4, "status": "planned"     }
    ]
  }
  # `start` and `end` are 0-based indices into `periods`. `end` is exclusive.
"""
from ..base import add_slide, set_notes
from ..widgets import text_box, filled_rect, divider
from .. import colors as c


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)

    text_box(slide, prs, 0.05, 0.04, 0.90, 0.08,
             text=spec.get("title", ""), size_pt=22, bold=True,
             color=brand["colors"]["black"])

    periods = spec.get("periods", [])
    tasks = spec.get("tasks", [])[:7]
    if not periods or not tasks:
        set_notes(slide, spec.get("notes"))
        return slide

    label_w = 0.22
    grid_left = 0.05 + label_w
    grid_w = 1 - 2 * 0.05 - label_w
    period_w = grid_w / len(periods)
    header_top = 0.16
    body_top = header_top + 0.05
    row_h = min(0.09, (0.92 - body_top) / max(1, len(tasks)))

    # Period headers
    for i, p in enumerate(periods):
        text_box(slide, prs, grid_left + i * period_w, header_top,
                 period_w, 0.05,
                 text=p, size_pt=11, bold=True,
                 color=brand["colors"]["gray_1"],
                 align="center", anchor="middle")
        # Vertical grid line
        filled_rect(slide, prs,
                    grid_left + i * period_w, body_top,
                    0.001, row_h * len(tasks),
                    fill_color=brand["colors"]["gray_2"])

    # Task rows
    for i, t in enumerate(tasks):
        ry = body_top + i * row_h
        text_box(slide, prs, 0.05, ry, label_w, row_h,
                 text=t.get("label", ""), size_pt=12,
                 color=brand["colors"]["black"], anchor="middle")
        start = max(0, int(t.get("start", 0)))
        end = min(len(periods), int(t.get("end", start + 1)))
        if end <= start:
            continue
        bar_left = grid_left + start * period_w + 0.005
        bar_w = (end - start) * period_w - 0.01
        bar_color = c.status(t.get("status"), default=brand["colors"]["primary"])
        filled_rect(slide, prs,
                    bar_left, ry + row_h * 0.30,
                    bar_w, row_h * 0.40,
                    fill_color=bar_color)
        divider(slide, prs, 0.05, ry + row_h - 0.001,
                1 - 2 * 0.05,
                color=brand["colors"]["gray_3"], thickness=0.001)

    set_notes(slide, spec.get("notes"))
    return slide
