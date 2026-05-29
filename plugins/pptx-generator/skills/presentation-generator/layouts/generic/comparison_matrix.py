"""comparison_matrix — feature vs competitor table.

Spec:
  { "layout": "comparison_matrix",
    "title": "...",
    "columns": ["ScanPay", "Competitor A", "Competitor B"],
    "rows": [
      { "label": "Digital menu",     "values": [true,  true,  false] },
      { "label": "Payment splitting","values": [true,  false, false] },
      { "label": "POS integration",  "values": [true,  true,  true ] }
    ]
  }
"""
from ..base import add_slide, set_notes
from ..widgets import text_box, comparison_row, divider, filled_rect


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)

    text_box(slide, prs, 0.05, 0.04, 0.90, 0.08,
             text=spec.get("title", ""), size_pt=22, bold=True,
             color=brand["colors"]["black"])

    cols = spec.get("columns", [])
    rows = spec.get("rows", [])
    if not cols or not rows:
        set_notes(slide, spec.get("notes"))
        return slide

    table_top = 0.16
    label_w = 0.28
    rest_w = 1 - 2 * 0.05 - label_w
    col_w = rest_w / max(1, len(cols))

    # Header row
    for i, c in enumerate(cols):
        cx = 0.05 + label_w + i * col_w
        # Highlight first column (own product) with a soft background
        if i == 0:
            filled_rect(slide, prs, cx, table_top - 0.005, col_w, 0.045,
                        fill_color=brand["colors"]["primary"])
            text_box(slide, prs, cx, table_top, col_w, 0.04,
                     text=c, size_pt=11, bold=True,
                     color="#FFFFFF", align="center", anchor="middle")
        else:
            text_box(slide, prs, cx, table_top, col_w, 0.04,
                     text=c, size_pt=11, bold=True,
                     color=brand["colors"]["black"], align="center", anchor="middle")

    # Data rows
    row_h = min(0.07, (0.95 - table_top - 0.06) / max(1, len(rows)))
    for ri, row in enumerate(rows):
        ry = table_top + 0.06 + ri * row_h
        comparison_row(
            slide, prs, 0.05, ry,
            1 - 2 * 0.05, row_h,
            label=row.get("label", ""),
            options=row.get("values", []),
            brand=brand, label_w=label_w,
        )
        divider(slide, prs, 0.05, ry + row_h - 0.001,
                1 - 2 * 0.05,
                color=brand["colors"]["gray_2"], thickness=0.001)

    set_notes(slide, spec.get("notes"))
    return slide
