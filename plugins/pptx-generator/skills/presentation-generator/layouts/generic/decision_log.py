"""decision_log — table of date / decision / owner / status rows.

Spec:
  { "layout": "decision_log",
    "title": "...",
    "decisions": [
      { "date": "2026-02-12", "decision": "Adopt FastAPI for the platform API",
        "owner": "Wojciech", "status": "done" },
      { "date": "2026-02-15", "decision": "Defer mobile launch to Q3",
        "owner": "Board",    "status": "blocked" }
    ]
  }
"""
from ..base import add_slide, set_notes
from ..widgets import text_box, divider, status_pill, filled_rect


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)

    text_box(slide, prs, 0.05, 0.04, 0.90, 0.08,
             text=spec.get("title", ""), size_pt=22, bold=True,
             color=brand["colors"]["black"])

    rows = spec.get("decisions", [])[:8]
    if not rows:
        set_notes(slide, spec.get("notes"))
        return slide

    col_dates = 0.12
    col_dec   = 0.50
    col_owner = 0.14
    col_status = 0.14

    header_top = 0.16
    # Header row
    filled_rect(slide, prs, 0.05, header_top, 0.90, 0.05,
                fill_color=brand["colors"]["gray_3"])
    headers = [
        ("Date",     0.05, col_dates),
        ("Decision", 0.05 + col_dates, col_dec),
        ("Owner",    0.05 + col_dates + col_dec, col_owner),
        ("Status",   0.05 + col_dates + col_dec + col_owner, col_status),
    ]
    for name, lx, lw in headers:
        text_box(slide, prs, lx + 0.005, header_top, lw - 0.01, 0.05,
                 text=name, size_pt=11, bold=True,
                 color=brand["colors"]["gray_1"], anchor="middle")

    body_top = header_top + 0.05
    row_h = min(0.085, (0.94 - body_top) / max(1, len(rows)))
    for i, r in enumerate(rows):
        ry = body_top + i * row_h
        text_box(slide, prs, 0.05 + 0.005, ry,
                 col_dates - 0.01, row_h,
                 text=r.get("date", ""), size_pt=10,
                 color=brand["colors"]["gray_1"], anchor="middle")
        text_box(slide, prs, 0.05 + col_dates + 0.005, ry,
                 col_dec - 0.01, row_h,
                 text=r.get("decision", ""), size_pt=12,
                 color=brand["colors"]["black"], anchor="middle")
        text_box(slide, prs, 0.05 + col_dates + col_dec + 0.005, ry,
                 col_owner - 0.01, row_h,
                 text=r.get("owner", ""), size_pt=11,
                 color=brand["colors"]["black"], anchor="middle")
        status_pill(slide, prs,
                    0.05 + col_dates + col_dec + col_owner + 0.005,
                    ry + row_h * 0.30,
                    col_status - 0.01, row_h * 0.40,
                    status_key=r.get("status", "neutral"), brand=brand)
        divider(slide, prs, 0.05, ry + row_h - 0.001, 0.90,
                color=brand["colors"]["gray_2"], thickness=0.001)

    set_notes(slide, spec.get("notes"))
    return slide
