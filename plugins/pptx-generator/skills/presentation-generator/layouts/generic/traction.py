"""traction — pitch slide showing growth metrics with KPI tiles.

Spec:
  { "layout": "traction",
    "title":   "...",
    "main_statement": "...",                   # optional headline
    "kpis": [
       { "value": "127k", "label": "MAU",       "trend": "+18%" },
       { "value": "94%",  "label": "Retention", "trend": "+2pp" },
       { "value": "12d",  "label": "TTV",       "trend": "-3d"  }
    ],
    "supporting": "Optional context paragraph below the tiles."
  }
"""
from ..base import add_slide, set_notes
from ..widgets import text_box, kpi_tile


MARGIN_X = 0.05
MARGIN_TOP = 0.12


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)

    text_box(slide, prs, MARGIN_X, 0.04, 1 - 2 * MARGIN_X, 0.08,
             text=spec.get("title", ""), size_pt=22, bold=True,
             color=brand["colors"]["black"])

    main = spec.get("main_statement", "")
    if main:
        text_box(slide, prs, MARGIN_X, 0.14, 1 - 2 * MARGIN_X, 0.10,
                 text=main, size_pt=14,
                 color=brand["colors"]["gray_1"])

    grid_top = 0.26 if main else 0.18
    kpis = spec.get("kpis", [])[:4]
    if kpis:
        n = len(kpis)
        gutter = 0.02
        tile_w = (1 - 2 * MARGIN_X - (n - 1) * gutter) / n
        tile_h = 0.30
        for i, k in enumerate(kpis):
            left = MARGIN_X + i * (tile_w + gutter)
            kpi_tile(slide, prs, left, grid_top, tile_w, tile_h,
                     value=k.get("value", ""), label=k.get("label", ""),
                     trend_delta=k.get("trend"), brand=brand)

    supp = spec.get("supporting", "")
    if supp:
        text_box(slide, prs, MARGIN_X, grid_top + 0.34,
                 1 - 2 * MARGIN_X, 0.20,
                 text=supp, size_pt=12,
                 color=brand["colors"]["black"])

    set_notes(slide, spec.get("notes"))
    return slide
