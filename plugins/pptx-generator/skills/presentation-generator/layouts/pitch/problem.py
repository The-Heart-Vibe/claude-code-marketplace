"""problem — Problem framing slide.

Toolkit question: "Jak dany problem jest obecnie rozwiązywany i dlaczego
należy to zmienić?"

Default layout: three_column (three stats land harder than prose). If the
spec has < 3 columns, use stat_pair instead.
"""
from ._base import dispatch, GENERIC_BY_NAME


def build(prs, layout_cfg, spec, brand, ctx):
    columns = spec.get("columns") or []
    layout_name = spec.get("layout_override")
    if not layout_name:
        layout_name = "three_column" if len(columns) >= 3 else "stat_pair"
    if "layout_override" not in spec and ctx.get("resolve_layout"):
        layout_cfg = ctx["resolve_layout"](layout_name)
    return GENERIC_BY_NAME[layout_name].build(prs, layout_cfg, spec, brand, ctx)
