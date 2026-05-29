"""tokens — convert brand.yaml into design tokens in three formats.

Formats produced:
  1. W3C Design Tokens (DTCG)  — tokens.json
  2. CSS custom properties      — tokens.css
  3. Tailwind preset            — tailwind.preset.cjs

DTCG spec: https://design-tokens.github.io/community-group/format/
"""
from __future__ import annotations

import json
from typing import Any


# ── W3C DTCG ──────────────────────────────────────────────────────────────

def to_dtcg(brand: dict) -> dict:
    """Return a W3C DTCG `tokens.json` payload from brand.yaml."""
    colors = brand.get("colors", {})
    typo = brand.get("typography", {})
    layout = brand.get("layout", {})

    def color_token(value: str, description: str = "") -> dict:
        return {"$type": "color", "$value": value,
                **({"$description": description} if description else {})}

    def fontfamily_token(value: str, description: str = "") -> dict:
        return {"$type": "fontFamily", "$value": [value],
                **({"$description": description} if description else {})}

    def number_token(value: int) -> dict:
        return {"$type": "number", "$value": value}

    return {
        "$schema": "https://design-tokens.org/schemas/2024-09-tokens.json",
        "color": {
            "brand": {
                "primary":    color_token(colors.get("primary",  "#E61B25"),
                                          "The Heart signature red."),
                "black":      color_token(colors.get("black",    "#000000"),
                                          "Primary text colour."),
                "green":      color_token(colors.get("green",    "#13A538"),
                                          "Positive / done signals."),
                "background": color_token(colors.get("background","#FFFFFF")),
            },
            "accent": {
                "blue":      color_token(colors.get("blue",       "#0056A4"),
                                          "Use sparingly — accent if needed."),
                "red_light": color_token(colors.get("red_light",  "#E9787E")),
            },
            "neutral": {
                "gray_1": color_token(colors.get("gray_1", "#969696"),
                                       "Secondary text, captions."),
                "gray_2": color_token(colors.get("gray_2", "#E6E6E6"),
                                       "Borders, dividers."),
                "gray_3": color_token(colors.get("gray_3", "#F0F0F0"),
                                       "Subtle surfaces, hover states."),
            },
            "status": {
                "done":        color_token(colors.get("green",  "#13A538")),
                "in_progress": color_token(colors.get("black",  "#000000"),
                                            "Status pill for active items — uses black "
                                            "instead of blue per brand rule (blue is "
                                            "an opt-in accent)."),
                "at_risk":     color_token(colors.get("red_light", "#E9787E")),
                "blocked":     color_token(colors.get("primary", "#E61B25")),
                "planned":     color_token(colors.get("gray_1",  "#969696")),
            },
        },
        "font": {
            "family": {
                "heading":  fontfamily_token(typo.get("heading_font",  "Raleway SemiBold")),
                "body":     fontfamily_token(typo.get("body_font",     "Raleway")),
                "emphasis": fontfamily_token(typo.get("emphasis_font", "Raleway SemiBold")),
                "light":    fontfamily_token(typo.get("light_font",    "Raleway Light")),
                "fallback": fontfamily_token(typo.get("fallback_font", "Arial")),
            },
            "size": {
                "title":     number_token(typo.get("size_title", 36)),
                "h1":        number_token(typo.get("size_h1", 28)),
                "h2":        number_token(typo.get("size_h2", 20)),
                "section":   number_token(typo.get("size_section_title", 12)),
                "body":      number_token(typo.get("size_body", 14)),
                "supporting":number_token(typo.get("size_supporting", 12)),
                "caption":   number_token(typo.get("size_caption", 10)),
            },
        },
        "spacing": {
            "margin_h_pct": number_token(int((layout.get("margin_h", 0.08)) * 100)),
            "margin_v_pct": number_token(int((layout.get("margin_v", 0.08)) * 100)),
        },
    }


# ── CSS custom properties ─────────────────────────────────────────────────

def to_css(brand: dict) -> str:
    """Emit a `tokens.css` exposing every brand token as a CSS variable.

    Variables are namespaced as `--th-<group>-<name>` so they can be safely
    used alongside other token systems.
    """
    colors = brand.get("colors", {})
    typo = brand.get("typography", {})

    lines = [
        "/* Auto-generated from brand.yaml — DO NOT EDIT BY HAND. */",
        ":root {",
        "  /* Colour — main palette */",
        f"  --th-color-primary: {colors.get('primary', '#E61B25')};",
        f"  --th-color-black: {colors.get('black', '#000000')};",
        f"  --th-color-green: {colors.get('green', '#13A538')};",
        f"  --th-color-background: {colors.get('background', '#FFFFFF')};",
        "",
        "  /* Colour — accents (use sparingly) */",
        f"  --th-color-blue: {colors.get('blue', '#0056A4')};",
        f"  --th-color-red-light: {colors.get('red_light', '#E9787E')};",
        "",
        "  /* Colour — neutrals */",
        f"  --th-color-gray-1: {colors.get('gray_1', '#969696')};",
        f"  --th-color-gray-2: {colors.get('gray_2', '#E6E6E6')};",
        f"  --th-color-gray-3: {colors.get('gray_3', '#F0F0F0')};",
        "",
        "  /* Status colours */",
        f"  --th-color-status-done: {colors.get('green', '#13A538')};",
        f"  --th-color-status-in-progress: {colors.get('black', '#000000')};",
        f"  --th-color-status-at-risk: {colors.get('red_light', '#E9787E')};",
        f"  --th-color-status-blocked: {colors.get('primary', '#E61B25')};",
        f"  --th-color-status-planned: {colors.get('gray_1', '#969696')};",
        "",
        "  /* Typography */",
        f"  --th-font-heading: \"{typo.get('heading_font', 'Raleway SemiBold')}\", Arial, sans-serif;",
        f"  --th-font-body: \"{typo.get('body_font', 'Raleway')}\", Arial, sans-serif;",
        f"  --th-font-light: \"{typo.get('light_font', 'Raleway Light')}\", Arial, sans-serif;",
        "",
        "  /* Font sizes (px) */",
        f"  --th-text-title: {typo.get('size_title', 36)}px;",
        f"  --th-text-h1: {typo.get('size_h1', 28)}px;",
        f"  --th-text-h2: {typo.get('size_h2', 20)}px;",
        f"  --th-text-section: {typo.get('size_section_title', 12)}px;",
        f"  --th-text-body: {typo.get('size_body', 14)}px;",
        f"  --th-text-supporting: {typo.get('size_supporting', 12)}px;",
        f"  --th-text-caption: {typo.get('size_caption', 10)}px;",
        "",
        "  /* Spacing */",
        "  --th-radius-sm: 4px;",
        "  --th-radius-md: 8px;",
        "  --th-radius-lg: 12px;",
        "}",
        "",
        "body { font-family: var(--th-font-body); color: var(--th-color-black); }",
        "h1, h2, h3, h4, h5 { font-family: var(--th-font-heading); }",
    ]
    return "\n".join(lines) + "\n"


# ── Tailwind preset ───────────────────────────────────────────────────────

def to_tailwind_preset(brand: dict) -> str:
    """Emit `tailwind.preset.cjs` consumed by the consumer's tailwind.config."""
    colors = brand.get("colors", {})
    typo = brand.get("typography", {})

    preset: dict[str, Any] = {
        "theme": {
            "extend": {
                "colors": {
                    "th": {
                        "primary":    colors.get("primary", "#E61B25"),
                        "black":      colors.get("black", "#000000"),
                        "green":      colors.get("green", "#13A538"),
                        "blue":       colors.get("blue", "#0056A4"),
                        "red-light":  colors.get("red_light", "#E9787E"),
                        "gray-1":     colors.get("gray_1", "#969696"),
                        "gray-2":     colors.get("gray_2", "#E6E6E6"),
                        "gray-3":     colors.get("gray_3", "#F0F0F0"),
                        "background": colors.get("background", "#FFFFFF"),
                        "status": {
                            "done":        colors.get("green", "#13A538"),
                            "in-progress": colors.get("black", "#000000"),
                            "at-risk":     colors.get("red_light", "#E9787E"),
                            "blocked":     colors.get("primary", "#E61B25"),
                            "planned":     colors.get("gray_1", "#969696"),
                        },
                    },
                },
                "fontFamily": {
                    "heading":  [typo.get("heading_font", "Raleway SemiBold"), "Arial", "sans-serif"],
                    "body":     [typo.get("body_font", "Raleway"),             "Arial", "sans-serif"],
                    "light":    [typo.get("light_font", "Raleway Light"),      "Arial", "sans-serif"],
                },
                "fontSize": {
                    "th-title":      [f"{typo.get('size_title', 36)}px", {"lineHeight": "1.1"}],
                    "th-h1":         [f"{typo.get('size_h1', 28)}px",    {"lineHeight": "1.2"}],
                    "th-h2":         [f"{typo.get('size_h2', 20)}px",    {"lineHeight": "1.3"}],
                    "th-section":    [f"{typo.get('size_section_title', 12)}px", {"lineHeight": "1.4"}],
                    "th-body":       [f"{typo.get('size_body', 14)}px",  {"lineHeight": "1.5"}],
                    "th-supporting": [f"{typo.get('size_supporting', 12)}px", {"lineHeight": "1.5"}],
                    "th-caption":    [f"{typo.get('size_caption', 10)}px",   {"lineHeight": "1.4"}],
                },
            },
        },
    }
    body = json.dumps(preset, indent=2)
    return (
        "// Auto-generated from brand.yaml — DO NOT EDIT BY HAND.\n"
        "/** @type {import('tailwindcss').Config} */\n"
        f"module.exports = {body};\n"
    )
