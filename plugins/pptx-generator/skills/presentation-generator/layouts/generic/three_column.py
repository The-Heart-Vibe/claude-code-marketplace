"""three_column — title + 3 stat cells, each (heading + body).

Mirrors the toolkit's `CUSTOM_1_1_1_1_2_2` layout used on the ScanPay problem
slide (3 statistics with supporting context). Ideal for:
  - Problem framed as 3 root causes
  - Solution as 3 value props
  - Why-now as 3 converging trends

Spec:
  {
    "layout": "three_column",
    "title":     "...",
    "subtitle":  "..."        # optional one-liner under title
    "columns": [
      { "heading": "68%",    "body": "customers prefer self-service" },
      { "heading": "97%",    "body": "restaurants cite rising costs" },
      { "heading": "45%",    "body": "operators understaffed" }
    ]
  }
"""
from ..base import add_slide, placeholder, set_text, set_notes


def build(prs, layout_cfg, spec, brand, ctx):
    slide = add_slide(prs, layout_cfg)

    set_text(placeholder(slide, layout_cfg, "title"),    spec.get("title", ""))
    set_text(placeholder(slide, layout_cfg, "subtitle"), spec.get("subtitle", ""))

    cols = _normalize_columns(spec)
    placeholders = layout_cfg.get("placeholders") or {}
    has_split = "col1_heading" in placeholders
    has_flat  = "col1" in placeholders

    for i, col in enumerate(cols[:3], start=1):
        heading = col.get("heading", "")
        body    = col.get("body", "")
        if has_split:
            set_text(placeholder(slide, layout_cfg, f"col{i}_heading"), heading)
            set_text(placeholder(slide, layout_cfg, f"col{i}_body"),    body)
        elif has_flat:
            merged = "\n\n".join(p for p in (heading, body) if p)
            set_text(placeholder(slide, layout_cfg, f"col{i}"), merged)

    set_notes(slide, spec.get("notes"))
    return slide


def _normalize_columns(spec: dict) -> list:
    """Accept either {columns: [{heading, body}, ...]} or {col1, col2, col3}.

    Both forms appear in real specs depending on the template; this lets the
    same builder work across templates without forcing the caller to know
    which layout style is in use.
    """
    if "columns" in spec:
        return list(spec["columns"])
    cols = []
    for key in ("col1", "col2", "col3"):
        val = spec.get(key)
        if val is None:
            continue
        if isinstance(val, dict):
            cols.append(val)
        else:
            text = str(val)
            head, _, body = text.partition("\n")
            cols.append({"heading": head, "body": body})
    return cols
