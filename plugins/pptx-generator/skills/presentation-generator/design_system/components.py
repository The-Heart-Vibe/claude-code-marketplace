"""components — emit React + Tailwind components mirroring layouts/widgets.py.

Each widget in Python becomes a React component using brand tokens via the
generated Tailwind preset. Components are pure presentational TSX (no state),
which is the form Claude Design expects for design-system imports.
"""
from __future__ import annotations


# ── Shared types ─────────────────────────────────────────────────────────

TYPES = '''// Shared types for status-driven components.
export type StatusKey =
  | "done"
  | "in_progress"
  | "at_risk"
  | "blocked"
  | "planned"
  | "on_track"
  | "off_track";

export const statusToClass: Record<StatusKey, string> = {
  done:        "bg-th-status-done",
  on_track:    "bg-th-status-done",
  in_progress: "bg-th-status-in-progress",
  at_risk:     "bg-th-status-at-risk",
  blocked:     "bg-th-status-blocked",
  off_track:   "bg-th-status-blocked",
  planned:     "bg-th-status-planned",
};
'''


COMPONENTS = {

    # ── KPI tile ───────────────────────────────────────────────────────────
    "KPITile.tsx": '''import type { StatusKey } from "./types";

type TrendDirection = "up" | "down" | "flat";

export interface KPITileProps {
  value: string;
  label: string;
  trend?: string;               // e.g. "+12%" or "-3d"
  trendDirection?: TrendDirection;
  status?: StatusKey;
}

const trendArrow: Record<TrendDirection, string> = {
  up: "↑",
  down: "↓",
  flat: "→",
};

const trendClass: Record<TrendDirection, string> = {
  up:   "text-th-green",
  down: "text-th-primary",
  flat: "text-th-gray-1",
};

export function KPITile({ value, label, trend, trendDirection = "flat", status }: KPITileProps) {
  const valueClass = trend ? trendClass[trendDirection] : "text-th-primary";
  return (
    <div className="rounded-md border border-th-gray-2 bg-white p-4 flex flex-col gap-1">
      <div className={`text-th-h1 font-heading font-semibold ${valueClass}`}>
        {value}
        {trend && (
          <span className="ml-2 text-th-h2 font-body">
            {trendArrow[trendDirection]} {trend}
          </span>
        )}
      </div>
      <div className="text-th-supporting text-th-gray-1 font-body">{label}</div>
    </div>
  );
}
''',

    # ── Person card ────────────────────────────────────────────────────────
    "PersonCard.tsx": '''export interface PersonCardProps {
  name: string;
  role: string;
  bio: string;
  photoUrl?: string;
}

export function PersonCard({ name, role, bio, photoUrl }: PersonCardProps) {
  return (
    <div className="flex flex-col gap-2">
      {photoUrl && (
        <img src={photoUrl} alt={name} className="aspect-square w-24 rounded-full object-cover" />
      )}
      <div className="text-th-h2 font-heading font-semibold text-th-black">{name}</div>
      <div className="text-th-supporting font-heading font-semibold text-th-primary">{role}</div>
      <p className="text-th-supporting font-body text-th-gray-1">{bio}</p>
    </div>
  );
}
''',

    # ── Big stat ───────────────────────────────────────────────────────────
    "BigStat.tsx": '''export interface BigStatProps {
  value: string;
  caption: string;
  color?: string;     // CSS colour; defaults to brand primary
  align?: "left" | "center" | "right";
}

export function BigStat({ value, caption, color, align = "center" }: BigStatProps) {
  const alignClass = { left: "text-left", center: "text-center", right: "text-right" }[align];
  return (
    <div className={`${alignClass}`}>
      <div
        className="font-heading font-bold leading-none"
        style={{ fontSize: 80, color: color ?? "var(--th-color-primary)" }}
      >
        {value}
      </div>
      <div className="mt-3 text-th-supporting font-body text-th-gray-1">{caption}</div>
    </div>
  );
}
''',

    # ── Badge ──────────────────────────────────────────────────────────────
    "Badge.tsx": '''export interface BadgeProps {
  children: React.ReactNode;
  variant?: "primary" | "black" | "gray" | "outline";
}

const variantClass: Record<Required<BadgeProps>["variant"], string> = {
  primary: "bg-th-primary text-white",
  black:   "bg-th-black text-white",
  gray:    "bg-th-gray-3 text-th-black",
  outline: "border border-th-gray-2 text-th-black",
};

export function Badge({ children, variant = "primary" }: BadgeProps) {
  return (
    <span
      className={`inline-block rounded-full px-3 py-1 text-th-caption font-heading font-semibold uppercase tracking-wide ${variantClass[variant]}`}
    >
      {children}
    </span>
  );
}
''',

    # ── Status pill ────────────────────────────────────────────────────────
    "StatusPill.tsx": '''import { StatusKey, statusToClass } from "./types";

export interface StatusPillProps {
  status: StatusKey;
  label?: string;
}

const defaultLabels: Record<StatusKey, string> = {
  done:        "Done",
  on_track:    "On track",
  in_progress: "In progress",
  at_risk:     "At risk",
  blocked:     "Blocked",
  off_track:   "Off track",
  planned:     "Planned",
};

export function StatusPill({ status, label }: StatusPillProps) {
  return (
    <span
      className={`inline-block rounded-full px-3 py-1 text-th-caption font-heading font-semibold uppercase tracking-wide text-white ${statusToClass[status]}`}
    >
      {label ?? defaultLabels[status]}
    </span>
  );
}
''',

    # ── Timeline event ─────────────────────────────────────────────────────
    "TimelineEvent.tsx": '''import { StatusKey, statusToClass } from "./types";

export interface TimelineEventProps {
  date: string;
  label: string;
  status?: StatusKey;
}

export function TimelineEvent({ date, label, status = "planned" }: TimelineEventProps) {
  return (
    <div className="flex flex-col items-center text-center gap-2 max-w-[180px]">
      <span className={`block h-4 w-4 rounded-full ${statusToClass[status]}`} />
      <div className="text-th-caption font-heading font-semibold text-th-gray-1">{date}</div>
      <div className="text-th-supporting font-body text-th-black">{label}</div>
    </div>
  );
}
''',

    # ── Comparison row ─────────────────────────────────────────────────────
    "ComparisonRow.tsx": '''export interface ComparisonRowProps {
  label: string;
  values: (boolean | string)[];
}

export function ComparisonRow({ label, values }: ComparisonRowProps) {
  return (
    <div
      className="grid items-center border-b border-th-gray-2 py-3"
      style={{ gridTemplateColumns: `200px repeat(${values.length}, 1fr)` }}
    >
      <div className="text-th-supporting font-heading font-semibold text-th-black">{label}</div>
      {values.map((v, i) => (
        <div key={i} className="text-center text-th-supporting font-body">
          {typeof v === "boolean" ? (
            <span className={v ? "text-th-green" : "text-th-primary"} style={{ fontSize: 22 }}>
              {v ? "✔" : "✘"}
            </span>
          ) : (
            <span className="text-th-black">{v}</span>
          )}
        </div>
      ))}
    </div>
  );
}
''',

    # ── Divider ────────────────────────────────────────────────────────────
    "Divider.tsx": '''export interface DividerProps {
  color?: string;
  thickness?: number;
}

export function Divider({ color = "var(--th-color-gray-2)", thickness = 1 }: DividerProps) {
  return <div style={{ height: thickness, background: color, width: "100%" }} />;
}
''',

    # ── SectionLabel (eyebrow) ─────────────────────────────────────────────
    "SectionLabel.tsx": '''export interface SectionLabelProps {
  children: React.ReactNode;
}

export function SectionLabel({ children }: SectionLabelProps) {
  return (
    <span className="text-th-caption font-heading font-semibold uppercase tracking-wide text-th-primary">
      {children}
    </span>
  );
}
''',

    # ── BulletList — four guideline variants + nested children ─────────────
    "BulletList.tsx": '''import { ReactNode } from "react";

/* Brand guideline (slide 11 of blank.pptx) defines four bullet styles:
 *
 *   filled-circle   ● heading  → ○ child
 *   filled-square   ■ heading  → □ child
 *   numbered        1. heading → ● child
 *   plain           bullets without hierarchy
 *
 * Each `BulletItem` can carry nested `children` which are auto-rendered
 * with the matching secondary marker.
 */
export type BulletKind = "filled-circle" | "filled-square" | "numbered" | "plain";

export interface BulletItem {
  text:      ReactNode;
  children?: BulletItem[];
}

export interface BulletListProps {
  kind?:  BulletKind;
  items:  BulletItem[];
  depth?: number;   // internal — caller leaves it 0
}

const PRIMARY = {
  "filled-circle": "●",
  "filled-square": "■",
  "numbered":      null,  // rendered as "1.", "2." inline
  "plain":         "•",
} satisfies Record<BulletKind, string | null>;

const NESTED = {
  "filled-circle": "○",
  "filled-square": "□",
  "numbered":      "●",
  "plain":         "○",
} satisfies Record<BulletKind, string>;

export function BulletList({ kind = "filled-circle", items, depth = 0 }: BulletListProps) {
  return (
    <ul className="space-y-2">
      {items.map((item, i) => {
        const marker =
          kind === "numbered" && depth === 0
            ? `${i + 1}.`
            : depth === 0
              ? PRIMARY[kind]
              : NESTED[kind];
        return (
          <li key={i} className="flex items-start gap-2">
            <span
              aria-hidden
              className={`flex-none w-5 text-th-body font-heading font-semibold ${
                depth === 0 && (kind === "filled-circle" || kind === "filled-square")
                  ? "text-th-primary"
                  : "text-th-black"
              }`}
            >
              {marker}
            </span>
            <div className="flex-1 text-th-body text-th-black">
              <div>{item.text}</div>
              {item.children && item.children.length > 0 && (
                <div className="mt-2 ml-2">
                  <BulletList kind={kind} items={item.children} depth={depth + 1} />
                </div>
              )}
            </div>
          </li>
        );
      })}
    </ul>
  );
}
''',

    # ── Arrow — solid + dotted black arrows from the guideline ─────────────
    "Arrow.tsx": '''/* Brand guideline (slide 11) ships two arrow styles: solid and dotted.
 * Both render in black to keep the visual neutral; use the colour prop
 * sparingly when you really need an emphasis.
 */
export type ArrowStyle = "solid" | "dotted";
export type ArrowDirection = "right" | "left" | "up" | "down";

export interface ArrowProps {
  style?:     ArrowStyle;
  direction?: ArrowDirection;
  length?:    number;   // px
  color?:     string;
}

const ROTATION: Record<ArrowDirection, number> = {
  right: 0, down: 90, left: 180, up: 270,
};

export function Arrow({
  style = "solid",
  direction = "right",
  length = 120,
  color = "var(--th-color-black)",
}: ArrowProps) {
  const head = 12;
  const lineY = 10;
  const dash = style === "dotted" ? "3 5" : undefined;
  return (
    <svg
      width={length}
      height={20}
      viewBox={`0 0 ${length} 20`}
      style={{ transform: `rotate(${ROTATION[direction]}deg)` }}
    >
      <line
        x1={0} y1={lineY} x2={length - head} y2={lineY}
        stroke={color} strokeWidth={2}
        strokeDasharray={dash}
        strokeLinecap="round"
      />
      <polygon
        points={`${length - head},${lineY - 6} ${length},${lineY} ${length - head},${lineY + 6}`}
        fill={color}
      />
    </svg>
  );
}
''',

    # ── Symbol — standalone status markers from the guideline ──────────────
    "Symbol.tsx": '''/* Standalone symbols from the brand guideline (slide 11):
 *   ✔   green check
 *   ✘   red cross
 *   ⬤   amber (red-light) dot
 *
 * Use these inline (in body text) where a StatusPill would be too heavy.
 */
export type SymbolKind = "check" | "cross" | "dot";

export interface SymbolProps {
  kind:  SymbolKind;
  size?: number;
}

const GLYPH: Record<SymbolKind, string> = {
  check: "✔",
  cross: "✘",
  dot:   "⬤",
};

const COLOR: Record<SymbolKind, string> = {
  check: "var(--th-color-green)",
  cross: "var(--th-color-primary)",
  dot:   "var(--th-color-red-light)",
};

export function Symbol({ kind, size = 18 }: SymbolProps) {
  return (
    <span
      aria-hidden
      style={{
        fontSize: size,
        color: COLOR[kind],
        lineHeight: 1,
        display: "inline-block",
        verticalAlign: "middle",
      }}
    >
      {GLYPH[kind]}
    </span>
  );
}
''',

    # ── BrandFooter — copyright bar from every guideline slide ─────────────
    "BrandFooter.tsx": '''/* Replicates the footer that appears on every blank.pptx content slide:
 *
 *      The Heart. All rights reserved.            <page> / <total>
 *
 * Sits flush above the red accent bar drawn by SlideShell.
 */
export interface BrandFooterProps {
  copyright?:  string;
  pageNumber?: number;
  totalPages?: number;
}

export function BrandFooter({
  copyright = "The Heart. All rights reserved.",
  pageNumber,
  totalPages,
}: BrandFooterProps) {
  return (
    <div className="absolute inset-x-12 bottom-3 flex items-center justify-between text-th-caption text-th-gray-1">
      <span>{copyright}</span>
      {pageNumber !== undefined && (
        <span>
          {pageNumber}
          {totalPages ? ` / ${totalPages}` : ""}
        </span>
      )}
    </div>
  );
}
''',

    # ── DecorativeCorner — abstract triangles in the corners ───────────────
    "DecorativeCorner.tsx": '''/* Abstract grey triangles + line fragments anchored to a corner.
 * Mirrors the decorative element in the top-right of every blank.pptx
 * content slide. Pure SVG so it scales cleanly.
 */
export type DecorativeCornerPosition = "top-right" | "top-left" | "bottom-right" | "bottom-left";

export interface DecorativeCornerProps {
  position?: DecorativeCornerPosition;
  size?:     number;   // px square
  opacity?:  number;
}

const TRANSFORMS: Record<DecorativeCornerPosition, string> = {
  "top-right":    "translate(0, 0)",
  "top-left":     "translate(0, 0) scale(-1, 1)",
  "bottom-right": "translate(0, 0) scale(1, -1)",
  "bottom-left":  "translate(0, 0) scale(-1, -1)",
};

const POSITION_CLASS: Record<DecorativeCornerPosition, string> = {
  "top-right":    "absolute top-0 right-0",
  "top-left":     "absolute top-0 left-0",
  "bottom-right": "absolute bottom-0 right-0",
  "bottom-left":  "absolute bottom-0 left-0",
};

export function DecorativeCorner({
  position = "top-right",
  size = 240,
  opacity = 0.35,
}: DecorativeCornerProps) {
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 240 240"
      className={POSITION_CLASS[position]}
      style={{ opacity, pointerEvents: "none" }}
      aria-hidden
    >
      <g transform={TRANSFORMS[position]} fill="none" stroke="var(--th-color-gray-1)" strokeWidth={1}>
        {/* Stylised line fragments + triangles, mirroring the guideline corner */}
        <polyline points="240,30 170,80 220,140" />
        <polyline points="240,90 200,130 240,170" />
        <polygon  points="160,40 200,90 140,90"   />
        <polyline points="230,180 180,200 220,230" strokeDasharray="3 4" />
        <polygon  points="120,20 150,50 100,60"   />
      </g>
    </svg>
  );
}
''',
}


def write_components(out_dir):
    """Write every component plus a barrel `index.ts`."""
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "types.ts").write_text(TYPES)
    for filename, source in COMPONENTS.items():
        (out_dir / filename).write_text(source)

    barrel_lines = ['export * from "./types";']
    for filename in COMPONENTS:
        stem = filename.rsplit(".", 1)[0]
        barrel_lines.append(f'export {{ {stem} }} from "./{stem}";')
    (out_dir / "index.ts").write_text("\n".join(barrel_lines) + "\n")
