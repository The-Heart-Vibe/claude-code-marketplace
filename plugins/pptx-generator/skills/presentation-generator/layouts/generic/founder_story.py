"""founder_story — single founder profile with big quote.

Spec:
  { "layout": "founder_story",
    "title": "...",
    "name":  "Jan Andrzejczuk",
    "role":  "CEO and founder",
    "bio":   "7 years in venture building. Built Digital Gateways and AIS Gateway.",
    "quote": "We started ScanPay because restaurants don't need another POS — they need a 30-second checkout."
  }
"""
from ..base import add_slide, set_notes
from ..widgets import text_box, filled_rect


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)

    text_box(slide, prs, 0.05, 0.04, 0.90, 0.08,
             text=spec.get("title", ""), size_pt=22, bold=True,
             color=brand["colors"]["black"])

    # Left column: name + role + bio (35%)
    text_box(slide, prs, 0.05, 0.18, 0.32, 0.10,
             text=spec.get("name", ""), size_pt=24, bold=True,
             color=brand["colors"]["black"])
    text_box(slide, prs, 0.05, 0.30, 0.32, 0.06,
             text=spec.get("role", ""), size_pt=14, bold=True,
             color=brand["colors"]["primary"])
    text_box(slide, prs, 0.05, 0.38, 0.32, 0.50,
             text=spec.get("bio", ""), size_pt=12,
             color=brand["colors"]["gray_1"])

    # Right column: quote with accent (60%)
    quote = spec.get("quote", "")
    if quote:
        filled_rect(slide, prs, 0.40, 0.25, 0.005, 0.50,
                    fill_color=brand["colors"]["primary"])
        text_box(slide, prs, 0.43, 0.25, 0.52, 0.50,
                 text=f"“{quote}”", size_pt=20,
                 color=brand["colors"]["black"], anchor="middle")

    set_notes(slide, spec.get("notes"))
    return slide
