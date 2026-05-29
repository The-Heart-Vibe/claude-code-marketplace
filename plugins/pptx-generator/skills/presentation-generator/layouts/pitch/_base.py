"""
pitch/_base.py — Shared helper for pitch section modules.

Each section module declares its preferred generic layout and forwards the
spec there. The wrapper lets the caller override the layout per spec entry
(e.g. force `three_column` when there are exactly 3 stats).
"""
from ..generic import (
    cover, section, content, two_column, three_column,
    main_point, big_number, stat_pair, table_grid, chart, quote, closing,
)


GENERIC_BY_NAME = {
    "cover":        cover,
    "section":      section,
    "content":      content,
    "two_column":   two_column,
    "three_column": three_column,
    "main_point":   main_point,
    "big_number":   big_number,
    "stat_pair":    stat_pair,
    "table_grid":   table_grid,
    "chart":        chart,
    "quote":        quote,
    "closing":      closing,
}


def dispatch(default_layout: str):
    """Return a section builder that delegates to a generic layout.

    The returned builder honours `spec['layout_override']` so a user can
    override the section's default layout without leaving the semantic API.
    """
    def _build(prs, layout_cfg, spec, brand, ctx):
        layout_name = spec.get("layout_override", default_layout)
        target = GENERIC_BY_NAME[layout_name]
        # The caller (generate.py) already resolved layout_cfg for the section
        # alias; if an override changes the layout, re-resolve via ctx.
        if layout_name != default_layout and ctx.get("resolve_layout"):
            layout_cfg = ctx["resolve_layout"](layout_name)
        return target.build(prs, layout_cfg, spec, brand, ctx)
    return _build
