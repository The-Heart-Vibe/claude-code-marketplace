"""closing — last slide. Renders contact-style left/right block.

Spec:
  {
    "layout":  "closing",
    "title":   "Let's talk",
    "left":    { "heading": "Jan Andrzejczuk",  "bullets": ["j.andrzejczuk@x.com", "+48 696 756 889"] },
    "right":   { "heading": "Tomasz Czapliński", "bullets": ["tomek@x.com",        "+48 602 536 076"] }
  }
"""
from . import two_column as _native_two_column
from . import free_canvas as _free_canvas


def build(prs, layout_cfg, spec, brand, ctx):
    # Closing is two-column intent — route through free canvas when the
    # template's native two-column geometry isn't usable (blank.pptx case).
    spec = dict(spec)
    spec.setdefault("title", spec.get("cta_headline", "Let's talk"))
    if layout_cfg.get("free_canvas"):
        return _free_canvas.two_column(prs, layout_cfg, spec, brand, ctx)
    return _native_two_column.build(prs, layout_cfg, spec, brand, ctx)
