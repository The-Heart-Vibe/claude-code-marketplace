"""stat_pair — title + main statement + supporting stats.

Mirrors the toolkit's `CUSTOM_1_1_1_1_2_1` layout used heavily in the
HomeAlert examples (Solution, Why-now, Business model, Market sizing).

Spec:
  {
    "layout": "stat_pair",
    "title":           "Market sizing",
    "main_statement":  "5.25M single-family homes in Poland — the addressable base.",
    "supporting": [
      { "label": "€6.15B", "body": "European home inspection market"   },
      { "label": "€0.75B", "body": "Polish home inspection market"     },
      { "label": "12.7%",  "body": "CAGR 2024–2031, global software"   }
    ],
    "aux": "Sources: InsightCrafters Pro, Verified Market Research"   # optional
  }
"""
from ..base import add_slide, placeholder, set_text, set_notes


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)

    set_text(placeholder(slide, layout_cfg, "title"),          spec.get("title", ""))
    set_text(placeholder(slide, layout_cfg, "main_statement"), spec.get("main_statement", ""))

    supporting = spec.get("supporting", [])
    # The master layout exposes one labeled cell + one body cell;
    # surface up to 3 supporting items concatenated.
    if supporting:
        labels = "\n".join(item.get("label", "") for item in supporting)
        bodies = "\n\n".join(item.get("body", "")  for item in supporting)
        set_text(placeholder(slide, layout_cfg, "supporting_label"), labels)
        set_text(placeholder(slide, layout_cfg, "supporting_body"),  bodies)

    set_text(placeholder(slide, layout_cfg, "aux"), spec.get("aux", ""))

    set_notes(slide, spec.get("notes"))
    return slide
