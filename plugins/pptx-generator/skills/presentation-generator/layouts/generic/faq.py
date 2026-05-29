"""faq — list of Q/A pairs.

Spec:
  { "layout": "faq",
    "title": "...",
    "items": [
      { "q": "How long does integration take?", "a": "2–4 weeks." },
      { "q": "Who owns the data?",               "a": "The bank, exclusively. We see pseudonymised hashes only." }
    ]
  }
"""
from ..base import add_slide, set_notes
from ..widgets import text_box, divider


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)

    text_box(slide, prs, 0.05, 0.04, 0.90, 0.08,
             text=spec.get("title", "FAQ"), size_pt=22, bold=True,
             color=brand["colors"]["black"])

    items = spec.get("items", [])[:5]
    if not items:
        set_notes(slide, spec.get("notes"))
        return slide

    row_top = 0.16
    row_h = min(0.16, (0.94 - row_top) / max(1, len(items)))

    for i, item in enumerate(items):
        ry = row_top + i * row_h
        # Q
        text_box(slide, prs, 0.05, ry + 0.005, 0.04, 0.06,
                 text="Q", size_pt=14, bold=True,
                 color=brand["colors"]["primary"], align="center")
        text_box(slide, prs, 0.10, ry + 0.005, 0.85, 0.06,
                 text=item.get("q", ""), size_pt=14, bold=True,
                 color=brand["colors"]["black"])
        # A
        text_box(slide, prs, 0.05, ry + 0.07, 0.04, 0.06,
                 text="A", size_pt=12, bold=True,
                 color=brand["colors"]["gray_1"], align="center")
        text_box(slide, prs, 0.10, ry + 0.07, 0.85, row_h - 0.08,
                 text=item.get("a", ""), size_pt=12,
                 color=brand["colors"]["gray_1"])
        if i < len(items) - 1:
            divider(slide, prs, 0.05, ry + row_h - 0.005, 0.90,
                    color=brand["colors"]["gray_2"], thickness=0.001)

    set_notes(slide, spec.get("notes"))
    return slide
