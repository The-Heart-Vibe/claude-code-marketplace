"""swot — 4-quadrant SWOT analysis.

Spec:
  { "layout": "swot",
    "title": "...",
    "strengths":     ["...", "..."],
    "weaknesses":    ["...", "..."],
    "opportunities": ["...", "..."],
    "threats":       ["...", "..."]
  }
"""
from ..base import add_slide, set_notes
from ..widgets import text_box, filled_rect


QUADS = [
    ("strengths",     "Strengths",     "#13A538"),
    ("weaknesses",    "Weaknesses",    "#E9787E"),
    ("opportunities", "Opportunities", "#0056A4"),
    ("threats",       "Threats",       "#E61B25"),
]


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)

    text_box(slide, prs, 0.05, 0.04, 0.90, 0.08,
             text=spec.get("title", ""), size_pt=22, bold=True,
             color=brand["colors"]["black"])

    g_left, g_top, g_w, g_h = 0.06, 0.16, 0.88, 0.75
    cell_w = g_w / 2
    cell_h = g_h / 2

    for i, (key, title, color) in enumerate(QUADS):
        r = i // 2
        c = i % 2
        cx = g_left + c * cell_w
        cy = g_top + r * cell_h

        # Coloured header band
        filled_rect(slide, prs, cx, cy, cell_w, 0.06,
                    fill_color=color)
        text_box(slide, prs, cx, cy, cell_w, 0.06,
                 text=title.upper(), size_pt=12, bold=True,
                 color="#FFFFFF", align="center", anchor="middle")
        # Body
        items = spec.get(key, [])
        body = "\n".join(f"• {x}" for x in items)
        text_box(slide, prs, cx + 0.01, cy + 0.08,
                 cell_w - 0.02, cell_h - 0.10,
                 text=body, size_pt=12,
                 color=brand["colors"]["black"])

    set_notes(slide, spec.get("notes"))
    return slide
