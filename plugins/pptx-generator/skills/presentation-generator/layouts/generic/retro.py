"""retro — Start / Stop / Continue 3-column.

Spec:
  { "layout": "retro",
    "title": "...",
    "start":    ["...", "..."],
    "stop":     ["...", "..."],
    "continue": ["...", "..."]
  }
"""
from ..base import add_slide, set_notes
from ..widgets import text_box, filled_rect


COLS = [
    ("start",    "Start",    "#13A538"),
    ("stop",     "Stop",     "#E61B25"),
    ("continue", "Continue", "#0056A4"),
]


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)

    text_box(slide, prs, 0.05, 0.04, 0.90, 0.08,
             text=spec.get("title", ""), size_pt=22, bold=True,
             color=brand["colors"]["black"])

    gutter = 0.02
    col_w = (1 - 2 * 0.05 - 2 * gutter) / 3
    block_top = 0.18
    block_h = 0.74

    for i, (key, title, color) in enumerate(COLS):
        left = 0.05 + i * (col_w + gutter)
        # Coloured header
        filled_rect(slide, prs, left, block_top, col_w, 0.07,
                    fill_color=color)
        text_box(slide, prs, left, block_top, col_w, 0.07,
                 text=title.upper(), size_pt=14, bold=True,
                 color="#FFFFFF", align="center", anchor="middle")
        # Body
        items = spec.get(key, [])
        body = "\n".join(f"• {x}" for x in items)
        text_box(slide, prs, left + 0.01, block_top + 0.09,
                 col_w - 0.02, block_h - 0.10,
                 text=body, size_pt=13,
                 color=brand["colors"]["black"])

    set_notes(slide, spec.get("notes"))
    return slide
