"""
layouts/ — Per-layout slide builders.

Each module exports a `build(prs, layout_cfg, spec, brand, ctx)` function that
adds a single slide using the given Slide Master layout and fills it from the
spec.

Splitting per file:
  generic/  — primitive layouts that map 1:1 to a master layout
  pitch/    — semantic pitchdeck sections (problem, solution, ...) that pick
              the right generic layout based on content shape and apply the
              section-specific copy rules.

The dispatch table is built in layouts/__init__.py::resolve().
"""
from .generic import cover, section, content, two_column, three_column
from .generic import main_point, big_number, stat_pair, table_grid, closing
from .generic import chart as chart_layout, quote as quote_layout

# Rich pitch layouts
from .generic import (
    traction, roadmap, comparison_matrix,
    value_prop, customer_journey, founder_story,
    partnership_model, gtm_strategy,
)

# Internal-deck layouts
from .generic import (
    okr, risk_matrix, swot,
    weekly_status, retro, decision_log, gantt,
)

# General-purpose layouts
from .generic import (
    big_quote, testimonial, before_after, agenda, faq, image_grid,
)

from .pitch import (
    cover as pitch_cover,
    purpose, problem, solution, why_now, market_size, competition,
    product, business_model, financials, team, investment, contact,
)


GENERIC = {
    # Core primitives
    "cover":        cover,
    "section":      section,
    "content":      content,
    "two_column":   two_column,
    "three_column": three_column,
    "main_point":   main_point,
    "big_number":   big_number,
    "stat_pair":    stat_pair,
    "table_grid":   table_grid,
    "chart":        chart_layout,
    "quote":        quote_layout,
    "closing":      closing,

    # Rich pitch
    "traction":           traction,
    "roadmap":            roadmap,
    "comparison_matrix":  comparison_matrix,
    "value_prop":         value_prop,
    "customer_journey":   customer_journey,
    "founder_story":      founder_story,
    "partnership_model":  partnership_model,
    "gtm_strategy":       gtm_strategy,

    # Internal
    "okr":            okr,
    "risk_matrix":    risk_matrix,
    "swot":           swot,
    "weekly_status":  weekly_status,
    "retro":          retro,
    "decision_log":   decision_log,
    "gantt":          gantt,

    # General-purpose
    "big_quote":     big_quote,
    "testimonial":   testimonial,
    "before_after":  before_after,
    "agenda":        agenda,
    "faq":           faq,
    "image_grid":    image_grid,
}

PITCH = {
    "cover":           pitch_cover,
    "purpose":         purpose,
    "problem":         problem,
    "solution":        solution,
    "why_now":         why_now,
    "market_size":     market_size,
    "competition":     competition,
    "product":         product,
    "business_model":  business_model,
    "financials":      financials,
    "team":            team,
    "investment":      investment,
    "contact":         contact,
}


def resolve(spec_entry: dict):
    """Return the builder function for a spec entry.

    A spec entry may declare either a generic `layout` or a semantic `section`.
    Pitch sections take precedence — they delegate to the appropriate generic
    layout internally, but apply per-section checklists and copy rules.
    """
    if "section" in spec_entry and spec_entry["section"] in PITCH:
        return PITCH[spec_entry["section"]]
    layout = spec_entry.get("layout", "content")
    if layout in GENERIC:
        return GENERIC[layout]
    raise KeyError(f"Unknown layout/section: {spec_entry}")
