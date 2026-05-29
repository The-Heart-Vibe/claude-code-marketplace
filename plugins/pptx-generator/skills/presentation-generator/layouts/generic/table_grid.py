"""table_grid — title + up to 10 cells.

Mirrors `CUSTOM_1_1_1_1_2_1_1_1_2`. The toolkit uses this layout for
financials forecast (Y1–Y5 × KPI) and a 4–5 person team grid.

Spec — flat form:
  {
    "layout": "table_grid",
    "title":  "Team",
    "cells": [
      "Tomasz Czapliński\\nCo-founder\\nManaging Partner at SpeedUp VC",
      "Jan Andrzejczuk\\nVenture Architect\\n7y in venture building",
      ...
    ]
  }
"""
from ..base import add_slide, placeholder, set_text, set_notes


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)
    set_text(placeholder(slide, layout_cfg, "title"), spec.get("title", ""))

    cells = spec.get("cells", [])
    for i, value in enumerate(cells, start=1):
        if i > 10:
            break
        set_text(placeholder(slide, layout_cfg, f"cell_{i}"), value)

    set_notes(slide, spec.get("notes"))
    return slide
