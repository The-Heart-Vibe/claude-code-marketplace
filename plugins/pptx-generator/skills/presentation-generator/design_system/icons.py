"""icons — copy the 41 Lucide SVGs into the design system and wire them
into a typed React `<Icon name="..."/>` component.

The plugin's icons/ directory contains:
  * svgs/<name>.svg       — currentColor-tinted SVG strings
  * icon_manifest.json    — alias → canonical-name + categories

We export:
  * src/icons/svgs/*.svg              — every SVG, copied verbatim
  * src/icons/icon-manifest.json      — same manifest the plugin uses
  * src/icons/IconName.ts             — exhaustive union of icon names
  * src/icons/Icon.tsx                — component that reads SVG + tints
  * src/icons/index.ts                — barrel exports
"""
from __future__ import annotations

import json
import shutil
from pathlib import Path


def write_icons(plugin_root: Path, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)

    src_svgs = plugin_root / "icons" / "svgs"
    dst_svgs = out_dir / "svgs"
    dst_svgs.mkdir(exist_ok=True)

    icon_names = []
    for svg in sorted(src_svgs.glob("*.svg")):
        shutil.copy2(svg, dst_svgs / svg.name)
        icon_names.append(svg.stem)

    # Copy manifest verbatim so both Python + React share a single map.
    manifest_src = plugin_root / "icons" / "icon_manifest.json"
    if manifest_src.exists():
        shutil.copy2(manifest_src, out_dir / "icon-manifest.json")

    # Emit a TypeScript union of canonical names.
    sorted_names = sorted(set(icon_names))
    union = " | ".join(f'"{n}"' for n in sorted_names)
    (out_dir / "IconName.ts").write_text(
        "// Auto-generated from icons/svgs/. Do not edit by hand.\n"
        f"export type IconName =\n  {union};\n\n"
        "export const ICON_NAMES = [\n"
        + "".join(f'  "{n}",\n' for n in sorted_names)
        + "] as const;\n"
    )

    # Emit the Icon component (Vite/CRA both support `?raw` SVG imports).
    (out_dir / "Icon.tsx").write_text(_icon_tsx())
    (out_dir / "icon-svgs.ts").write_text(_icon_svgs_ts(sorted_names))
    (out_dir / "index.ts").write_text(_barrel())


def _icon_tsx() -> str:
    return '''import { IconName } from "./IconName";
import { ICON_SVGS } from "./icon-svgs";
import manifest from "./icon-manifest.json";

/**
 * Brand-tinted icon. Renders one of the bundled Lucide SVGs and overrides
 * `currentColor` so the stroke matches the requested colour.
 *
 *   <Icon name="building-2" />                        // brand primary
 *   <Icon name="shield"     color="var(--th-color-black)" size={32} />
 *
 * `name` accepts either a canonical icon name (`building-2`) or any alias
 * declared in `icon-manifest.json` (`bank`, `organization`, ...).
 */
export interface IconProps {
  name:   IconName | string;
  size?:  number;
  color?: string;
  strokeWidth?: number;
  className?: string;
}

type IconManifest = { aliases: Record<string, string>; categories?: Record<string, string[]> };

export function Icon({
  name,
  size = 24,
  color = "var(--th-color-primary)",
  strokeWidth,
  className,
}: IconProps) {
  const canonical = resolveName(name, manifest as IconManifest);
  const raw = ICON_SVGS[canonical];
  if (!raw) {
    return <span aria-hidden style={{ display: "inline-block", width: size, height: size }} />;
  }
  let svg = raw
    .replace(/stroke="currentColor"/g, `stroke="${color}"`)
    .replace(/stroke:currentColor/g,   `stroke:${color}`)
    .replace(/width="[^"]*"/,   `width="${size}"`)
    .replace(/height="[^"]*"/,  `height="${size}"`);
  if (strokeWidth !== undefined) {
    svg = svg.replace(/stroke-width="[^"]*"/, `stroke-width="${strokeWidth}"`);
  }
  return (
    <span
      aria-hidden
      className={className}
      style={{ display: "inline-flex", width: size, height: size }}
      // eslint-disable-next-line react/no-danger
      dangerouslySetInnerHTML={{ __html: svg }}
    />
  );
}

function resolveName(name: string, manifest: IconManifest): string {
  if (name in manifest.aliases) return manifest.aliases[name];
  return name;
}
'''


def _icon_svgs_ts(names: list[str]) -> str:
    # Build a static map of name → raw SVG via Vite-friendly imports.
    # Using inline imports with `?raw` so this works with Vite out of the box.
    lines = [
        "// Auto-generated from icons/svgs/. Do not edit by hand.",
        "// `?raw` imports return the SVG file contents as a string — Vite, Webpack 5,",
        "// and Turbopack all support this pattern. The map below means a single",
        "// `Icon` render does not trigger a per-name dynamic import.",
        "",
    ]
    for n in names:
        var = "icon_" + n.replace("-", "_")
        lines.append(f'import {var} from "./svgs/{n}.svg?raw";')
    lines.append("")
    lines.append("export const ICON_SVGS: Record<string, string> = {")
    for n in names:
        var = "icon_" + n.replace("-", "_")
        lines.append(f'  "{n}": {var},')
    lines.append("};")
    lines.append("")
    return "\n".join(lines)


def _barrel() -> str:
    return (
        'export { Icon } from "./Icon";\n'
        'export type { IconProps } from "./Icon";\n'
        'export type { IconName } from "./IconName";\n'
        'export { ICON_NAMES } from "./IconName";\n'
    )
