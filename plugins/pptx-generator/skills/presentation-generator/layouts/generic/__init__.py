from . import cover, section, content, two_column, three_column
from . import main_point, big_number, stat_pair, table_grid
from . import chart, quote, closing, free_canvas

# Rich pitch layouts
from . import traction, roadmap, comparison_matrix
from . import value_prop, customer_journey, founder_story
from . import partnership_model, gtm_strategy

# Internal-deck layouts
from . import okr, risk_matrix, swot
from . import weekly_status, retro, decision_log, gantt

# General-purpose layouts
from . import big_quote, testimonial, before_after, agenda, faq, image_grid


# Wrap multi-column builders so they delegate to free_canvas when the
# template_map says the current template lacks native multi-column layouts.
# This keeps the dispatch table in layouts/__init__.py oblivious to which
# template is in use — the spec stays the same; rendering adapts.

def _wrap_with_canvas(native_module, canvas_fn):
    class _Dispatcher:
        @staticmethod
        def build(prs, layout_cfg, spec, brand, ctx):
            if layout_cfg.get("free_canvas"):
                return canvas_fn(prs, layout_cfg, spec, brand, ctx)
            return native_module.build(prs, layout_cfg, spec, brand, ctx)
    return _Dispatcher()


two_column   = _wrap_with_canvas(two_column,   free_canvas.two_column)
three_column = _wrap_with_canvas(three_column, free_canvas.three_column)
stat_pair    = _wrap_with_canvas(stat_pair,    free_canvas.stat_pair)
table_grid   = _wrap_with_canvas(table_grid,   free_canvas.table_grid)
