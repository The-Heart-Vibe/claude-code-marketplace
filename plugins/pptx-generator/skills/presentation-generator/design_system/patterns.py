"""patterns — emit page-level React components mirroring layouts/generic/*.

Each pattern is a presentational React component that takes typed props and
composes widgets. These map 1:1 to the rich slide layouts in the plugin so
designers can preview and adapt them in Claude Design.
"""
from __future__ import annotations


PATTERNS = {

    # ── SlideShell — chrome wrapper with red footer + page number ─────────
    "SlideShell.tsx": '''import { ReactNode } from "react";

import { BrandFooter } from "../components/BrandFooter";
import { DecorativeCorner } from "../components/DecorativeCorner";

export interface SlideShellProps {
  children: ReactNode;
  pageNumber?:    number;
  totalPages?:    number;
  sectionLabel?:  string;
  copyright?:     string;
  decorations?:   boolean;     // toggle the abstract corner artwork
}

/** Standard content-slide chrome:
 *  - thin vertical red bar on the left
 *  - section label eyebrow top-left
 *  - decorative grey corner top-right
 *  - red icon corner badge
 *  - bottom red accent bar + brand footer with copyright + page number
 *
 *  Mirrors slide 11 of blank.pptx (the canonical guideline slide).
 */
export function SlideShell({
  children,
  pageNumber,
  totalPages,
  sectionLabel,
  copyright,
  decorations = true,
}: SlideShellProps) {
  return (
    <div className="relative aspect-[16/9] w-full overflow-hidden bg-white p-12 font-body text-th-black">
      {/* Left vertical red bar */}
      <div className="absolute left-0 top-0 bottom-0 w-1.5 bg-th-primary" />

      {sectionLabel && (
        <div className="absolute left-12 top-6 text-th-caption font-heading font-semibold uppercase tracking-wide text-th-primary">
          {sectionLabel}
        </div>
      )}

      {decorations && <DecorativeCorner position="top-right" size={260} opacity={0.35} />}

      <div className="relative h-full pt-6">{children}</div>

      <div className="absolute inset-x-0 bottom-0 h-1.5 bg-th-primary" />
      <BrandFooter copyright={copyright} pageNumber={pageNumber} totalPages={totalPages} />
    </div>
  );
}
''',

    # ── Cover ──────────────────────────────────────────────────────────────
    "Cover.tsx": '''export interface CoverProps {
  title: string;
  subtitle?: string;
}

export function Cover({ title, subtitle }: CoverProps) {
  return (
    <div className="relative aspect-[16/9] w-full overflow-hidden bg-white p-16 font-body">
      <h1 className="text-th-title font-heading font-bold text-th-black max-w-[70%]">
        {title}
      </h1>
      {subtitle && (
        <p className="mt-6 text-th-h2 font-light text-th-gray-1 max-w-[70%]">{subtitle}</p>
      )}
      {/* signature red triangle bottom-right */}
      <div className="absolute bottom-0 right-0 h-1/3 w-1/3 bg-th-primary"
           style={{ clipPath: "polygon(100% 0, 100% 100%, 0 100%)" }} />
    </div>
  );
}
''',

    # ── Problem (3-stat) ───────────────────────────────────────────────────
    "Problem3Col.tsx": '''import { SlideShell } from "./SlideShell";

export interface Problem3ColProps {
  title: string;
  subtitle?: string;
  columns: { heading: string; body: string }[];
  pageNumber?: number;
  totalPages?: number;
}

export function Problem3Col({ title, subtitle, columns, pageNumber, totalPages }: Problem3ColProps) {
  return (
    <SlideShell pageNumber={pageNumber} totalPages={totalPages} sectionLabel="Problem">
      <h2 className="text-th-h1 font-heading font-bold text-th-black">{title}</h2>
      {subtitle && <p className="mt-2 text-th-supporting text-th-gray-1">{subtitle}</p>}
      <div className="mt-8 grid grid-cols-3 gap-6">
        {columns.slice(0, 3).map((c, i) => (
          <div key={i} className="flex flex-col gap-2">
            <div className="text-th-title font-heading font-bold text-th-primary">{c.heading}</div>
            <p className="text-th-supporting text-th-black">{c.body}</p>
          </div>
        ))}
      </div>
    </SlideShell>
  );
}
''',

    # ── OKR board ──────────────────────────────────────────────────────────
    "OKRBoard.tsx": '''import { SlideShell } from "./SlideShell";
import { StatusPill } from "../components/StatusPill";
import type { StatusKey } from "../components/types";

export interface KeyResult {
  label:   string;
  current: string;
  target:  string;
  status:  StatusKey;
}

export interface OKRBoardProps {
  title:     string;
  objective: string;
  keyResults: KeyResult[];
  pageNumber?: number;
  totalPages?: number;
}

export function OKRBoard({ title, objective, keyResults, pageNumber, totalPages }: OKRBoardProps) {
  return (
    <SlideShell pageNumber={pageNumber} totalPages={totalPages} sectionLabel="OKR">
      <h2 className="text-th-h1 font-heading font-bold text-th-black">{title}</h2>
      <div className="mt-4">
        <div className="text-th-caption font-heading font-semibold uppercase text-th-primary">Objective</div>
        <p className="mt-1 text-th-h2 font-heading font-semibold text-th-black">{objective}</p>
      </div>
      <div className="mt-8 grid grid-cols-3 gap-6">
        {keyResults.slice(0, 3).map((kr, i) => (
          <div key={i} className="rounded-md border border-th-gray-2 bg-white p-5 flex flex-col gap-3">
            <div className="text-th-caption font-heading font-semibold text-th-gray-1">KR {i + 1}</div>
            <div className="text-th-supporting font-heading font-semibold text-th-black">{kr.label}</div>
            <div className="text-th-h1 font-heading font-bold text-th-primary">
              {kr.current} <span className="text-th-gray-1 font-light">/</span> {kr.target}
            </div>
            <div className="text-th-caption text-th-gray-1">current / target</div>
            <StatusPill status={kr.status} />
          </div>
        ))}
      </div>
    </SlideShell>
  );
}
''',

    # ── SWOT grid ──────────────────────────────────────────────────────────
    "SWOTGrid.tsx": '''import { SlideShell } from "./SlideShell";

export interface SWOTGridProps {
  title: string;
  strengths:     string[];
  weaknesses:    string[];
  opportunities: string[];
  threats:       string[];
  pageNumber?: number;
  totalPages?: number;
}

const QUAD = [
  { key: "strengths",     label: "Strengths",     bg: "bg-th-green",     text: "text-white" },
  { key: "weaknesses",    label: "Weaknesses",    bg: "bg-th-red-light", text: "text-white" },
  { key: "opportunities", label: "Opportunities", bg: "bg-th-blue",      text: "text-white" },
  { key: "threats",       label: "Threats",       bg: "bg-th-primary",   text: "text-white" },
] as const;

export function SWOTGrid(props: SWOTGridProps) {
  const { title, pageNumber, totalPages, ...sections } = props;
  return (
    <SlideShell pageNumber={pageNumber} totalPages={totalPages} sectionLabel="SWOT">
      <h2 className="text-th-h1 font-heading font-bold text-th-black">{title}</h2>
      <div className="mt-6 grid grid-cols-2 gap-4 h-[80%]">
        {QUAD.map(q => (
          <div key={q.key} className="overflow-hidden rounded-md border border-th-gray-2 flex flex-col">
            <div className={`px-4 py-2 text-th-supporting font-heading font-semibold uppercase tracking-wide ${q.bg} ${q.text}`}>
              {q.label}
            </div>
            <ul className="flex-1 p-4 space-y-2 text-th-supporting text-th-black">
              {((sections as Record<string, string[]>)[q.key] ?? []).map((item, i) => (
                <li key={i}>• {item}</li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </SlideShell>
  );
}
''',

    # ── Roadmap ────────────────────────────────────────────────────────────
    "Roadmap.tsx": '''import { SlideShell } from "./SlideShell";
import { TimelineEvent } from "../components/TimelineEvent";
import type { StatusKey } from "../components/types";

export interface RoadmapMilestone {
  date:   string;
  label:  string;
  status?: StatusKey;
}

export interface RoadmapProps {
  title: string;
  milestones: RoadmapMilestone[];
  pageNumber?: number;
  totalPages?: number;
}

export function Roadmap({ title, milestones, pageNumber, totalPages }: RoadmapProps) {
  return (
    <SlideShell pageNumber={pageNumber} totalPages={totalPages} sectionLabel="Roadmap">
      <h2 className="text-th-h1 font-heading font-bold text-th-black">{title}</h2>
      <div className="mt-12 relative">
        <div className="absolute left-0 right-0 top-2 h-px bg-th-gray-2" />
        <div className="relative flex justify-between">
          {milestones.slice(0, 6).map((m, i) => (
            <TimelineEvent key={i} date={m.date} label={m.label} status={m.status} />
          ))}
        </div>
      </div>
    </SlideShell>
  );
}
''',

    # ── Competitive matrix ─────────────────────────────────────────────────
    "CompetitiveMatrix.tsx": '''import { SlideShell } from "./SlideShell";
import { ComparisonRow } from "../components/ComparisonRow";

export interface CompetitiveMatrixProps {
  title: string;
  columns: string[];                                  // first column = our product
  rows: { label: string; values: (boolean | string)[] }[];
  pageNumber?: number;
  totalPages?: number;
}

export function CompetitiveMatrix({ title, columns, rows, pageNumber, totalPages }: CompetitiveMatrixProps) {
  return (
    <SlideShell pageNumber={pageNumber} totalPages={totalPages} sectionLabel="Competition">
      <h2 className="text-th-h1 font-heading font-bold text-th-black">{title}</h2>
      <div className="mt-6">
        <div
          className="grid items-center pb-2"
          style={{ gridTemplateColumns: `200px repeat(${columns.length}, 1fr)` }}
        >
          <div />
          {columns.map((c, i) => (
            <div
              key={i}
              className={`text-center text-th-supporting font-heading font-semibold uppercase tracking-wide py-2 ${
                i === 0 ? "bg-th-primary text-white rounded-sm" : "text-th-black"
              }`}
            >
              {c}
            </div>
          ))}
        </div>
        {rows.map((row, i) => (
          <ComparisonRow key={i} label={row.label} values={row.values} />
        ))}
      </div>
    </SlideShell>
  );
}
''',

    # ── BigQuote ───────────────────────────────────────────────────────────
    "BigQuote.tsx": '''export interface BigQuoteProps {
  quote: string;
  attribution?: string;
}

export function BigQuote({ quote, attribution }: BigQuoteProps) {
  return (
    <div className="relative aspect-[16/9] w-full overflow-hidden bg-th-primary p-16 text-white font-body">
      <div className="text-[160px] leading-none font-heading font-bold opacity-30 -mb-8">"</div>
      <blockquote className="text-th-title font-heading font-semibold max-w-[80%]">
        {quote}
      </blockquote>
      {attribution && (
        <div className="mt-10 text-th-h2 font-light opacity-80">— {attribution}</div>
      )}
    </div>
  );
}
''',

    # ── Before / after ─────────────────────────────────────────────────────
    "BeforeAfter.tsx": '''import { SlideShell } from "./SlideShell";

export interface BeforeAfterProps {
  title: string;
  before: { heading: string; bullets: string[] };
  after:  { heading: string; bullets: string[] };
  pageNumber?: number;
  totalPages?: number;
}

export function BeforeAfter({ title, before, after, pageNumber, totalPages }: BeforeAfterProps) {
  return (
    <SlideShell pageNumber={pageNumber} totalPages={totalPages} sectionLabel="Before / After">
      <h2 className="text-th-h1 font-heading font-bold text-th-black">{title}</h2>
      <div className="mt-8 grid grid-cols-[1fr_60px_1fr] gap-4 items-stretch">
        <div className="rounded-md border border-th-gray-2 p-6 flex flex-col gap-3">
          <div className="text-th-supporting font-heading font-semibold text-th-gray-1">{before.heading}</div>
          <ul className="space-y-2 text-th-supporting">
            {before.bullets.map((b, i) => <li key={i}>• {b}</li>)}
          </ul>
        </div>
        <div className="flex items-center justify-center text-5xl font-bold text-th-primary">→</div>
        <div className="rounded-md border border-th-primary p-6 flex flex-col gap-3">
          <div className="text-th-supporting font-heading font-semibold text-th-primary">{after.heading}</div>
          <ul className="space-y-2 text-th-supporting">
            {after.bullets.map((b, i) => <li key={i}>• {b}</li>)}
          </ul>
        </div>
      </div>
    </SlideShell>
  );
}
''',

    # ── ValueProp ──────────────────────────────────────────────────────────
    "ValueProp.tsx": '''import { SlideShell } from "./SlideShell";

export interface Segment {
  name: string;
  pain: string;
  gain: string;
}

export interface ValuePropProps {
  title: string;
  segments: Segment[];
  pageNumber?: number;
  totalPages?: number;
}

export function ValueProp({ title, segments, pageNumber, totalPages }: ValuePropProps) {
  return (
    <SlideShell pageNumber={pageNumber} totalPages={totalPages} sectionLabel="Value proposition">
      <h2 className="text-th-h1 font-heading font-bold text-th-black">{title}</h2>
      <div className="mt-6 grid gap-4" style={{ gridTemplateColumns: `repeat(${segments.length}, 1fr)` }}>
        {segments.map((s, i) => (
          <div key={i} className="rounded-md border border-th-gray-2 bg-white overflow-hidden flex flex-col">
            <div className="bg-th-primary text-white text-center py-3 text-th-h2 font-heading font-semibold">
              {s.name}
            </div>
            <div className="p-5 flex flex-col gap-4 flex-1">
              <div>
                <div className="text-th-caption font-heading font-semibold text-th-gray-1">PAIN</div>
                <div className="text-th-supporting text-th-black">{s.pain}</div>
              </div>
              <div>
                <div className="text-th-caption font-heading font-semibold text-th-green">GAIN</div>
                <div className="text-th-supporting text-th-black">{s.gain}</div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </SlideShell>
  );
}
''',

    # ── Customer journey ───────────────────────────────────────────────────
    "CustomerJourney.tsx": '''import { SlideShell } from "./SlideShell";

export interface JourneyStep {
  label: string;
  body:  string;
}

export interface CustomerJourneyProps {
  title: string;
  steps: JourneyStep[];
  pageNumber?: number;
  totalPages?: number;
}

export function CustomerJourney({ title, steps, pageNumber, totalPages }: CustomerJourneyProps) {
  return (
    <SlideShell pageNumber={pageNumber} totalPages={totalPages} sectionLabel="Customer journey">
      <h2 className="text-th-h1 font-heading font-bold text-th-black">{title}</h2>
      <div className="relative mt-12 grid gap-6" style={{ gridTemplateColumns: `repeat(${steps.length}, 1fr)` }}>
        <div className="absolute left-0 right-0 top-6 h-px bg-th-gray-2" />
        {steps.map((s, i) => (
          <div key={i} className="relative flex flex-col items-center text-center gap-3">
            <div className="w-12 h-12 rounded-full bg-th-primary text-white flex items-center justify-center font-heading font-bold text-th-h2">
              {i + 1}
            </div>
            <div className="text-th-h2 font-heading font-semibold text-th-black">{s.label}</div>
            <p className="text-th-supporting text-th-gray-1">{s.body}</p>
          </div>
        ))}
      </div>
    </SlideShell>
  );
}
''',

    # ── Weekly status (RAG) ────────────────────────────────────────────────
    "WeeklyStatus.tsx": '''import { SlideShell } from "./SlideShell";
import { StatusPill } from "../components/StatusPill";
import type { StatusKey } from "../components/types";

export interface Stream {
  name:    string;
  status:  StatusKey;
  summary: string;
}

export interface WeeklyStatusProps {
  title: string;
  streams: Stream[];
  pageNumber?: number;
  totalPages?: number;
}

export function WeeklyStatus({ title, streams, pageNumber, totalPages }: WeeklyStatusProps) {
  return (
    <SlideShell pageNumber={pageNumber} totalPages={totalPages} sectionLabel="Workstream RAG">
      <h2 className="text-th-h1 font-heading font-bold text-th-black">{title}</h2>
      <div className="mt-6 divide-y divide-th-gray-2">
        {streams.map((s, i) => (
          <div key={i} className="py-4 grid items-center gap-4" style={{ gridTemplateColumns: "200px 120px 1fr" }}>
            <div className="text-th-h2 font-heading font-semibold text-th-black">{s.name}</div>
            <StatusPill status={s.status} />
            <div className="text-th-supporting text-th-black">{s.summary}</div>
          </div>
        ))}
      </div>
    </SlideShell>
  );
}
''',
}


def write_patterns(out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    for filename, source in PATTERNS.items():
        (out_dir / filename).write_text(source)

    barrel_lines = []
    for filename in PATTERNS:
        stem = filename.rsplit(".", 1)[0]
        barrel_lines.append(f'export {{ {stem} }} from "./{stem}";')
    (out_dir / "index.ts").write_text("\n".join(barrel_lines) + "\n")
