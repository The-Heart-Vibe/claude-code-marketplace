"""weekly_status — RAG status across N workstreams.

Spec:
  { "layout": "weekly_status",
    "title": "...",
    "streams": [
      { "name": "Product",     "status": "on_track", "summary": "Beta shipped to 12 design partners." },
      { "name": "Sales",       "status": "at_risk",  "summary": "Two of four enterprise deals slipped to Q2." },
      { "name": "Engineering", "status": "done",     "summary": "Migration to new infra complete." }
    ]
  }
"""
from ..base import add_slide, set_notes
from ..widgets import text_box, status_pill, divider


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)

    text_box(slide, prs, 0.05, 0.04, 0.90, 0.08,
             text=spec.get("title", ""), size_pt=22, bold=True,
             color=brand["colors"]["black"])

    streams = spec.get("streams", [])[:6]
    if not streams:
        set_notes(slide, spec.get("notes"))
        return slide

    row_top = 0.18
    row_h = min(0.12, (0.94 - row_top) / max(1, len(streams)))
    name_w = 0.20
    pill_w = 0.12
    summary_w = 0.90 - name_w - pill_w - 0.04

    for i, s in enumerate(streams):
        ry = row_top + i * row_h
        text_box(slide, prs, 0.05, ry, name_w, row_h,
                 text=s.get("name", ""), size_pt=15, bold=True,
                 color=brand["colors"]["black"], anchor="middle")
        status_pill(slide, prs, 0.05 + name_w, ry + row_h * 0.30,
                    pill_w, row_h * 0.40,
                    status_key=s.get("status", "neutral"), brand=brand)
        text_box(slide, prs, 0.05 + name_w + pill_w + 0.02, ry,
                 summary_w, row_h,
                 text=s.get("summary", ""), size_pt=12,
                 color=brand["colors"]["black"], anchor="middle")
        if i < len(streams) - 1:
            divider(slide, prs, 0.05, ry + row_h - 0.002, 0.90,
                    color=brand["colors"]["gray_2"], thickness=0.001)

    set_notes(slide, spec.get("notes"))
    return slide
