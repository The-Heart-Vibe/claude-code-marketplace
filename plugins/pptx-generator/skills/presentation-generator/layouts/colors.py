"""colors — semantic colour resolution for layouts.

Every layout needs to make colour choices: "this stat went up so it's green",
"this row is blocked so its accent is red", "this is the third option so it
gets the third accent in the palette". Centralising those decisions here
means layouts stay short and the brand stays consistent.
"""
from __future__ import annotations

from typing import Any, Optional


# ── Status colours ────────────────────────────────────────────────────────

STATUS_COLOURS = {
    "done":         "#13A538",   # brand green
    "completed":    "#13A538",
    "ok":           "#13A538",
    "green":        "#13A538",
    "on_track":     "#13A538",

    # Brand rule: blue is "accent if needed" — must not dominate status pills
    # on every internal deck. Use black for active/in-progress so the user's
    # eye treats it as "currently happening" without competing with the red
    # primary or the green done state.
    "in_progress": "#000000",   # active = bold black
    "progress":    "#000000",
    "wip":         "#000000",
    "active":      "#000000",
    "blue":        "#0056A4",   # explicit opt-in for the accent

    "at_risk":     "#E9787E",   # brand red-light
    "warning":     "#E9787E",
    "amber":       "#E9787E",
    "yellow":      "#E9787E",
    "watch":       "#E9787E",

    "blocked":     "#E61B25",   # brand red
    "off_track":   "#E61B25",
    "critical":    "#E61B25",
    "red":         "#E61B25",
    "fail":        "#E61B25",

    "neutral":     "#969696",   # gray
    "planned":     "#969696",
    "tbd":         "#969696",
    "gray":        "#969696",
}


def status(value: Optional[str], default: str = "#969696") -> str:
    if not value:
        return default
    return STATUS_COLOURS.get(str(value).lower().strip().replace(" ", "_"), default)


# ── Trend arrow + colour ──────────────────────────────────────────────────

def trend(delta: Any) -> tuple[str, str]:
    """Return (arrow, hex) for a numeric delta.

    Positive → up green; negative → down red; zero → neutral gray.
    """
    try:
        d = float(str(delta).replace("%", "").replace("+", "").strip())
    except (TypeError, ValueError):
        return ("→", "#969696")
    if d > 0:
        return ("↑", "#13A538")
    if d < 0:
        return ("↓", "#E61B25")
    return ("→", "#969696")


# ── Accent palette ────────────────────────────────────────────────────────

# Use this when you have N items and want each one to have a distinguishable
# accent. Cycles through brand colours in a deliberate order.
ACCENT_PALETTE = [
    "#E61B25",   # primary red — main brand accent
    "#000000",   # black — second accent, never competes with red
    "#13A538",   # green — positive signals
    "#E9787E",   # red-light — softer accent
    "#969696",   # gray — supporting
    "#0056A4",   # blue — accent if needed (last in cycle on purpose)
]


def accent(index: int) -> str:
    return ACCENT_PALETTE[index % len(ACCENT_PALETTE)]


# ── Brand colour resolver (string keys → hex) ────────────────────────────

def resolve(brand: dict, key: str, fallback: str = "#000000") -> str:
    """Look up `colors.{key}` in brand.yaml, fall back to `fallback`."""
    if key.startswith("#"):
        return key
    return brand.get("colors", {}).get(key, fallback)
