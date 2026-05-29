"""testimonial — quote + person + role + company.

Spec:
  { "layout": "testimonial",
    "title":       "What our clients say",                # optional
    "quote":       "ScanPay cut our checkout time by 70%.",
    "name":        "Anna Nowak",
    "role":        "Operations Director",
    "company":     "Café Chain",
    "company_logo": "/path/to/logo.png"     # optional
  }
"""
from ..base import add_slide, set_notes
from ..widgets import text_box, rounded_rect, filled_rect


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)

    title = spec.get("title", "")
    if title:
        text_box(slide, prs, 0.05, 0.04, 0.90, 0.08,
                 text=title, size_pt=22, bold=True,
                 color=brand["colors"]["black"])

    quote_top = 0.18 if title else 0.10

    text_box(slide, prs, 0.08, quote_top, 0.84, 0.45,
             text=f"“{spec.get('quote', '')}”", size_pt=24, bold=True,
             color=brand["colors"]["black"],
             align="left", anchor="middle")

    # Accent divider before attribution
    attr_top = quote_top + 0.50
    filled_rect(slide, prs, 0.08, attr_top, 0.04, 0.005,
                fill_color=brand["colors"]["primary"])

    text_box(slide, prs, 0.08, attr_top + 0.015, 0.84, 0.06,
             text=spec.get("name", ""), size_pt=14, bold=True,
             color=brand["colors"]["black"])
    role_company = spec.get("role", "")
    if spec.get("company"):
        role_company = f"{role_company} · {spec['company']}" if role_company else spec["company"]
    text_box(slide, prs, 0.08, attr_top + 0.08, 0.84, 0.05,
             text=role_company, size_pt=12,
             color=brand["colors"]["gray_1"])

    set_notes(slide, spec.get("notes"))
    return slide
