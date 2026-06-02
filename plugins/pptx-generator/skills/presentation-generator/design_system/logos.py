"""logos — copy The Heart brand logo assets into the design system and
expose a typed `<Logo/>` component.

Source files (`brand_assets/`):
  th-horizontal.png   7088×2482   ratio 2.856   wide banner / headers
  th-vertical.png     2363×1900   ratio 1.244   portrait / split covers
  th-icon.png          905×1371   ratio 0.660   favicon / monogram

Real (W/H) ratios are emitted as TypeScript constants so the `<Logo/>` size
prop always preserves aspect ratio — no stretched logos.

Output structure:
  src/logos/
    assets/
      th-horizontal.png
      th-vertical.png
      th-icon.png
    Logo.tsx          — typed React component
    aspect-ratios.ts  — width/height constants
    index.ts          — barrel
"""
from __future__ import annotations

import shutil
from pathlib import Path

from PIL import Image


LOGO_FILES = ("th-horizontal.png", "th-vertical.png", "th-icon.png")


def write_logos(plugin_root: Path, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    assets = out_dir / "assets"
    assets.mkdir(exist_ok=True)

    ratios: dict[str, float] = {}
    src_dir = plugin_root / "brand_assets"

    for name in LOGO_FILES:
        src = src_dir / name
        if not src.exists():
            continue
        shutil.copy2(src, assets / name)
        with Image.open(src) as img:
            w, h = img.size
            ratios[name] = round(w / h, 4)

    (out_dir / "aspect-ratios.ts").write_text(_aspect_ratios_ts(ratios))
    (out_dir / "Logo.tsx").write_text(_logo_tsx())
    (out_dir / "index.ts").write_text(_barrel())


# ── TypeScript output ─────────────────────────────────────────────────────

def _aspect_ratios_ts(ratios: dict[str, float]) -> str:
    horizontal = ratios.get("th-horizontal.png", 2.856)
    vertical   = ratios.get("th-vertical.png",   1.244)
    icon       = ratios.get("th-icon.png",       0.660)
    return (
        "// Auto-generated from brand_assets/. Real PNG aspect ratios (W / H).\n"
        "// Imported by Logo.tsx so size props never stretch the logo.\n"
        "\n"
        "export const LOGO_RATIOS = {\n"
        f"  horizontal: {horizontal:.4f},\n"
        f"  vertical:   {vertical:.4f},\n"
        f"  icon:       {icon:.4f},\n"
        "} as const;\n"
    )


def _logo_tsx() -> str:
    return '''import horizontalSrc from "./assets/th-horizontal.png";
import verticalSrc   from "./assets/th-vertical.png";
import iconSrc       from "./assets/th-icon.png";
import { LOGO_RATIOS } from "./aspect-ratios";

/**
 * The Heart logo.
 *
 *   <Logo variant="horizontal" height={32} />
 *   <Logo variant="vertical"   width={180}  theme="white" />
 *   <Logo variant="icon"       height={64} />
 *
 * - `variant` picks the asset (horizontal banner, vertical lock-up, or icon).
 * - `theme` re-tints the logo for dark backgrounds:
 *     - "color" (default) — uses the source asset as-is (brand red)
 *     - "white" — inverts brightness for use on dark surfaces
 *     - "black" — converts to monochrome black (use on top of light photos)
 * - Provide ONE dimension (`width` OR `height`) — the other is computed from
 *   the real PNG aspect ratio so the logo is never stretched.
 */
export type LogoVariant = "horizontal" | "vertical" | "icon";
export type LogoTheme   = "color" | "white" | "black";

export interface LogoProps {
  variant?: LogoVariant;
  theme?:   LogoTheme;
  width?:   number;
  height?:  number;
  className?: string;
  title?:   string;
}

const SOURCES: Record<LogoVariant, string> = {
  horizontal: horizontalSrc,
  vertical:   verticalSrc,
  icon:       iconSrc,
};

const FILTERS: Record<LogoTheme, string | undefined> = {
  color: undefined,
  // brightness(0) + invert(1) → solid white silhouette that respects transparency
  white: "brightness(0) invert(1)",
  // brightness(0) → solid black silhouette that respects transparency
  black: "brightness(0)",
};

export function Logo({
  variant = "horizontal",
  theme   = "color",
  width,
  height,
  className,
  title = "The Heart",
}: LogoProps) {
  const ratio = LOGO_RATIOS[variant];

  // Derive the missing dimension from the real PNG ratio.
  let finalWidth  = width;
  let finalHeight = height;
  if (width === undefined && height === undefined) {
    finalHeight = 32;
  }
  if (finalWidth === undefined && finalHeight !== undefined) {
    finalWidth = finalHeight * ratio;
  }
  if (finalHeight === undefined && finalWidth !== undefined) {
    finalHeight = finalWidth / ratio;
  }

  return (
    <img
      src={SOURCES[variant]}
      alt={title}
      width={finalWidth}
      height={finalHeight}
      className={className}
      style={{
        filter: FILTERS[theme],
        display: "inline-block",
        objectFit: "contain",
      }}
    />
  );
}
'''


def _barrel() -> str:
    return (
        'export { Logo } from "./Logo";\n'
        'export type { LogoProps, LogoVariant, LogoTheme } from "./Logo";\n'
        'export { LOGO_RATIOS } from "./aspect-ratios";\n'
    )
