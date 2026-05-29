"""risk_matrix — 2D probability × impact matrix with placed risks.

Spec:
  { "layout": "risk_matrix",
    "title": "...",
    "risks": [
      { "label": "Regulatory change",  "probability": "low",    "impact": "high"   },
      { "label": "Key partner churns", "probability": "medium", "impact": "high"   },
      { "label": "Team burnout",       "probability": "medium", "impact": "medium" }
    ]
  }
"""
from ..base import add_slide, set_notes
from ..widgets import text_box, filled_rect, circle


LEVELS = ["low", "medium", "high"]
LEVEL_IDX = {k: i for i, k in enumerate(LEVELS)}


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)

    text_box(slide, prs, 0.05, 0.04, 0.90, 0.08,
             text=spec.get("title", ""), size_pt=22, bold=True,
             color=brand["colors"]["black"])

    # Grid: 3×3 cells from (0.15, 0.20) to (0.85, 0.90)
    g_left, g_top, g_w, g_h = 0.18, 0.20, 0.60, 0.65
    cell_w = g_w / 3
    cell_h = g_h / 3

    # Cells with risk colour gradient
    palette = [
        ["#13A538", "#13A538", "#E9787E"],   # low impact row (top → bottom inversed)
        ["#13A538", "#E9787E", "#E61B25"],
        ["#E9787E", "#E61B25", "#E61B25"],
    ]
    for r in range(3):
        for c in range(3):
            color = palette[2 - r][c]
            filled_rect(slide, prs,
                        g_left + c * cell_w, g_top + r * cell_h,
                        cell_w, cell_h,
                        fill_color=color, line_color="#FFFFFF")

    # Axis labels
    text_box(slide, prs, g_left, g_top + g_h + 0.01,
             g_w, 0.04,
             text="Probability →", size_pt=10, bold=True,
             color=brand["colors"]["gray_1"], align="center")
    text_box(slide, prs, g_left - 0.14, g_top, 0.13, g_h,
             text="Impact →", size_pt=10, bold=True,
             color=brand["colors"]["gray_1"], align="right", anchor="middle")
    # X-axis tick labels
    for i, lvl in enumerate(LEVELS):
        text_box(slide, prs,
                 g_left + i * cell_w, g_top + g_h + 0.045,
                 cell_w, 0.03,
                 text=lvl, size_pt=9,
                 color=brand["colors"]["gray_1"], align="center")
    # Y-axis tick labels (top = high)
    for i, lvl in enumerate(reversed(LEVELS)):
        text_box(slide, prs, g_left - 0.06, g_top + i * cell_h,
                 0.05, cell_h,
                 text=lvl, size_pt=9,
                 color=brand["colors"]["gray_1"],
                 align="right", anchor="middle")

    # Risk dots
    for i, r in enumerate(spec.get("risks", [])):
        p_idx = LEVEL_IDX.get(r.get("probability", "low"), 0)
        i_idx = LEVEL_IDX.get(r.get("impact", "low"), 0)
        cx = g_left + p_idx * cell_w + cell_w / 2 - 0.015
        cy = g_top + (2 - i_idx) * cell_h + cell_h / 2 - 0.025
        circle(slide, prs, cx, cy, 0.03,
               fill_color=brand["colors"]["black"])
        text_box(slide, prs, cx, cy, 0.03, 0.03,
                 text=str(i + 1), size_pt=12, bold=True,
                 color="#FFFFFF", align="center", anchor="middle")

    # Legend right side
    legend_left = 0.82
    for i, r in enumerate(spec.get("risks", [])[:6]):
        ly = 0.20 + i * 0.10
        circle(slide, prs, legend_left, ly, 0.025,
               fill_color=brand["colors"]["black"])
        text_box(slide, prs, legend_left, ly, 0.025, 0.025,
                 text=str(i + 1), size_pt=10, bold=True,
                 color="#FFFFFF", align="center", anchor="middle")
        text_box(slide, prs, legend_left + 0.03, ly - 0.005, 0.15, 0.06,
                 text=r.get("label", ""), size_pt=10,
                 color=brand["colors"]["black"])

    set_notes(slide, spec.get("notes"))
    return slide
