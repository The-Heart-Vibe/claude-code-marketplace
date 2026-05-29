"""agenda — numbered list with optional time column.

Spec:
  { "layout": "agenda",
    "title": "Agenda",
    "items": [
      { "label": "Welcome",          "time": "10:00" },
      { "label": "Quarterly review", "time": "10:15" },
      { "label": "Q&A",              "time": "11:30" }
    ]
  }
  # `time` is optional; omit it for a plain numbered agenda.
"""
from ..base import add_slide, set_notes
from ..widgets import text_box, divider


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)

    text_box(slide, prs, 0.05, 0.04, 0.90, 0.08,
             text=spec.get("title", "Agenda"), size_pt=22, bold=True,
             color=brand["colors"]["black"])

    items = spec.get("items", [])[:8]
    if not items:
        set_notes(slide, spec.get("notes"))
        return slide

    has_times = any(i.get("time") for i in items)
    num_w = 0.06
    time_w = 0.10 if has_times else 0
    label_l = 0.05 + num_w + time_w + 0.02
    label_w = 1 - 2 * 0.05 - num_w - time_w - 0.02

    row_top = 0.18
    row_h = min(0.085, (0.94 - row_top) / max(1, len(items)))

    for i, item in enumerate(items):
        ry = row_top + i * row_h
        text_box(slide, prs, 0.05, ry, num_w, row_h,
                 text=f"{i+1:02}", size_pt=22, bold=True,
                 color=brand["colors"]["primary"], anchor="middle")
        if has_times:
            text_box(slide, prs, 0.05 + num_w, ry, time_w, row_h,
                     text=item.get("time", ""), size_pt=12, bold=True,
                     color=brand["colors"]["gray_1"], anchor="middle")
        text_box(slide, prs, label_l, ry, label_w, row_h,
                 text=item.get("label", ""), size_pt=16,
                 color=brand["colors"]["black"], anchor="middle")
        if i < len(items) - 1:
            divider(slide, prs, 0.05, ry + row_h - 0.001, 0.90,
                    color=brand["colors"]["gray_2"], thickness=0.001)

    set_notes(slide, spec.get("notes"))
    return slide
