"""cover — first slide of the deck.

Uses `cover_split` (master_idx=11) when available — the toolkit's split layout
with left-side title and right-side image area. Falls back to `cover_centered`
(master_idx=0, TITLE) if the alias isn't mapped.

Spec:
  {
    "layout": "cover",
    "title": "...",
    "subtitle": "..."           # optional
  }
"""
from datetime import date
from ..base import add_slide, placeholder, set_text, set_notes


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)

    set_text(placeholder(slide, layout_cfg, "title"), spec.get("title", ""))

    subtitle = spec.get("subtitle") or (
        f"{brand['identity']['company_name']}  ·  {date.today().strftime('%B %Y')}"
    )
    set_text(placeholder(slide, layout_cfg, "subtitle"), subtitle)

    # Some templates render the cover via free shapes (no placeholders).
    # In that case, fill the first two text shapes in document order.
    if (
        not layout_cfg.get("placeholders")
        and layout_cfg.get("free_shapes")
    ):
        text_shapes = [s for s in slide.shapes if s.has_text_frame]
        free = layout_cfg["free_shapes"]
        if "title" in free and len(text_shapes) > free["title"]:
            set_text(text_shapes[free["title"]], spec.get("title", ""))
        if "tagline" in free and len(text_shapes) > free["tagline"]:
            set_text(text_shapes[free["tagline"]], subtitle)

    set_notes(slide, spec.get("notes"))
    return slide
