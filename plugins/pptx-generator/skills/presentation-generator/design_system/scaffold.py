"""scaffold — project files that turn the generated tokens + components into
a Claude-Design-importable git repository.

Emits:
  README.md, package.json, tsconfig.json, vite.config.ts, tailwind.config.cjs,
  postcss.config.cjs, index.html, src/main.tsx, src/App.tsx,
  src/examples/Showcase.tsx, .gitignore.
"""
from __future__ import annotations

import json
from textwrap import dedent


def _pkg_json(brand: dict) -> str:
    name_slug = brand.get("identity", {}).get("company_name", "the-heart").lower().replace(" ", "-")
    return json.dumps({
        "name":    f"@{name_slug}/design-system",
        "version": "1.0.0",
        "private": True,
        "description": "The Heart brand design system — tokens, widgets, and slide patterns.",
        "type":    "module",
        "scripts": {
            "dev":     "vite",
            "build":   "tsc -b && vite build",
            "preview": "vite preview",
        },
        "dependencies": {
            "react":      "^18.3.1",
            "react-dom":  "^18.3.1",
        },
        "devDependencies": {
            "@types/react":      "^18.3.3",
            "@types/react-dom":  "^18.3.0",
            "@vitejs/plugin-react": "^4.3.1",
            "autoprefixer":      "^10.4.19",
            "postcss":           "^8.4.39",
            "tailwindcss":       "^3.4.4",
            "typescript":        "^5.4.5",
            "vite":              "^5.3.1",
        },
    }, indent=2)


def _tsconfig() -> str:
    return json.dumps({
        "compilerOptions": {
            "target":           "ES2022",
            "useDefineForClassFields": True,
            "lib":              ["ES2022", "DOM", "DOM.Iterable"],
            "module":           "ESNext",
            "skipLibCheck":     True,
            "moduleResolution": "Bundler",
            "allowImportingTsExtensions": True,
            "resolveJsonModule": True,
            "isolatedModules":  True,
            "noEmit":           True,
            "jsx":              "react-jsx",
            "strict":           True,
            "noUnusedLocals":   False,
            "noUnusedParameters": False,
            "noFallthroughCasesInSwitch": True,
        },
        "include": ["src"],
    }, indent=2)


def _vite_config() -> str:
    return dedent('''\
        import { defineConfig } from "vite";
        import react from "@vitejs/plugin-react";

        export default defineConfig({
          plugins: [react()],
        });
        ''')


def _tailwind_config() -> str:
    return dedent('''\
        /** @type {import('tailwindcss').Config} */
        module.exports = {
          content: ["./index.html", "./src/**/*.{ts,tsx}"],
          presets: [require("./tailwind.preset.cjs")],
          theme: { extend: {} },
          plugins: [],
        };
        ''')


def _postcss_config() -> str:
    return dedent('''\
        module.exports = {
          plugins: { tailwindcss: {}, autoprefixer: {} },
        };
        ''')


def _index_html(brand: dict) -> str:
    company = brand.get("identity", {}).get("company_name", "The Heart")
    return dedent(f'''\
        <!doctype html>
        <html lang="en">
        <head>
          <meta charset="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;600;700&display=swap" rel="stylesheet" />
          <title>{company} — Design System</title>
        </head>
        <body>
          <div id="root"></div>
          <script type="module" src="/src/main.tsx"></script>
        </body>
        </html>
        ''')


def _main_tsx() -> str:
    return dedent('''\
        import React from "react";
        import ReactDOM from "react-dom/client";
        import App from "./App";
        import "./tokens/tokens.css";

        ReactDOM.createRoot(document.getElementById("root")!).render(
          <React.StrictMode>
            <App />
          </React.StrictMode>,
        );
        ''')


def _app_tsx() -> str:
    return dedent('''\
        import { Showcase } from "./examples/Showcase";

        export default function App() {
          return <Showcase />;
        }
        ''')


def _showcase_tsx() -> str:
    return dedent('''\
        import {
          Cover, Problem3Col, OKRBoard, SWOTGrid, Roadmap,
          CompetitiveMatrix, BigQuote, BeforeAfter, ValueProp,
          CustomerJourney, WeeklyStatus, SlideShell,
        } from "../patterns";
        import {
          KPITile, PersonCard, BigStat, Badge, StatusPill,
          BulletList, Arrow, Symbol, BrandFooter, DecorativeCorner, SectionLabel,
        } from "../components";
        import { Icon } from "../icons";

        export function Showcase() {
          return (
            <div className="bg-th-gray-3 min-h-screen p-6 space-y-12">
              <header className="max-w-5xl mx-auto">
                <h1 className="text-th-title font-heading font-bold text-th-black">The Heart Design System</h1>
                <p className="mt-2 text-th-h2 font-light text-th-gray-1">
                  Tokens, widgets, and slide patterns generated from the deck-builder plugin.
                </p>
                <p className="mt-2 text-th-supporting text-th-gray-1">
                  Mirrors slide 11 of <code>blank.pptx</code> — Wytyczne: Rekomendowane czcionki, kształty i kolory.
                </p>
              </header>

              {/* ── Brand guideline section — replicates the canonical slide ─── */}
              <section className="max-w-5xl mx-auto bg-white rounded-md p-8 relative">
                <SectionLabel>Wytyczne</SectionLabel>
                <h2 className="mt-2 text-th-h1 font-heading font-bold text-th-black">
                  Rekomendowane czcionki, kształty i kolory
                </h2>

                <div className="mt-8 grid grid-cols-4 gap-6">
                  {/* Fonts */}
                  <div>
                    <h3 className="text-th-h2 font-heading font-semibold text-th-primary">Fonts</h3>
                    <p className="mt-1 text-th-caption text-th-gray-1">
                      Mniejsze czcionki jedynie w ostateczności — slajdy raportowe
                    </p>
                    <div className="mt-3 space-y-1 font-body">
                      <div style={{ fontSize: 10 }}>Raleway (10)</div>
                      <div style={{ fontSize: 12 }}>Raleway (12)</div>
                      <div style={{ fontSize: 14 }}>Raleway (14)</div>
                      <div style={{ fontSize: 16 }}>Raleway (16)</div>
                    </div>
                  </div>

                  {/* Icons */}
                  <div>
                    <h3 className="text-th-h2 font-heading font-semibold text-th-primary">Icons</h3>
                    <div className="mt-3 grid grid-cols-3 gap-3">
                      <Icon name="building-2" size={36} />
                      <Icon name="shield"     size={36} />
                      <Icon name="users"      size={36} />
                      <Icon name="trending-up" size={36} />
                      <Icon name="target"     size={36} />
                      <Icon name="rocket"     size={36} />
                    </div>
                    <p className="mt-2 text-th-caption text-th-gray-1">
                      41 icons available — see <code>icon-manifest.json</code>
                    </p>
                  </div>

                  {/* Bullets */}
                  <div>
                    <h3 className="text-th-h2 font-heading font-semibold text-th-primary">Bullets</h3>
                    <div className="mt-3 space-y-4">
                      <BulletList
                        kind="filled-circle"
                        items={[{ text: "The Heart", children: [{ text: "Lorem ipsum" }] }]}
                      />
                      <BulletList
                        kind="filled-square"
                        items={[{ text: "The Heart", children: [{ text: "Lorem ipsum" }] }]}
                      />
                      <BulletList
                        kind="numbered"
                        items={[
                          { text: "The Heart", children: [{ text: "Lorem ipsum" }] },
                          { text: "The Heart", children: [{ text: "Lorem ipsum" }] },
                        ]}
                      />
                    </div>
                  </div>

                  {/* Arrows + Symbols */}
                  <div>
                    <h3 className="text-th-h2 font-heading font-semibold text-th-primary">Arrows</h3>
                    <div className="mt-3 space-y-3">
                      <Arrow style="solid" length={140} />
                      <Arrow style="dotted" length={140} />
                    </div>
                    <h3 className="mt-6 text-th-h2 font-heading font-semibold text-th-black">Symbols</h3>
                    <div className="mt-3 flex gap-3 text-2xl">
                      <Symbol kind="check" size={26} />
                      <Symbol kind="cross" size={26} />
                      <Symbol kind="dot"   size={26} />
                    </div>
                  </div>
                </div>

                {/* Colour palette — matches the bottom half of the guideline slide */}
                <div className="mt-12">
                  <h3 className="sr-only">Colour palette</h3>
                  <div className="grid grid-cols-8 gap-4">
                    {[
                      ["Red",       "var(--th-color-primary)",   "#e61b25"],
                      ["Black",     "var(--th-color-black)",     "#000000"],
                      ["Gray 1",    "var(--th-color-gray-1)",    "#969696"],
                      ["Gray 2",    "var(--th-color-gray-2)",    "#e6e6e6"],
                      ["Green",     "var(--th-color-green)",     "#13a538"],
                      ["Red light", "var(--th-color-red-light)", "#e9787e"],
                      ["Blue",      "var(--th-color-blue)",      "#0056a4"],
                      ["Gray 3",    "var(--th-color-gray-3)",    "#f0f0f0"],
                    ].map(([name, css, hex]) => (
                      <div key={hex} className="flex flex-col items-center text-center gap-2">
                        <div
                          className="w-20 h-20 rounded-full border border-th-gray-2"
                          style={{ backgroundColor: css }}
                        />
                        <div className="text-th-supporting font-heading font-semibold text-th-black">{name}</div>
                        <div className="text-th-caption text-th-gray-1">{hex}</div>
                      </div>
                    ))}
                  </div>
                  <div className="mt-4 grid grid-cols-2 text-center text-th-supporting font-heading font-semibold">
                    <div className="text-th-primary">← Main colors →</div>
                    <div className="text-th-gray-1">← Accents if needed →</div>
                  </div>
                </div>
              </section>

              <header className="max-w-5xl mx-auto">
                <h2 className="text-th-h1 font-heading font-bold text-th-black">Component & pattern catalogue</h2>
                <p className="mt-1 text-th-supporting text-th-gray-1">
                  Every shape available to the deck-builder + Claude Design.
                </p>
              </header>

              <section className="max-w-5xl mx-auto">
                <h2 className="text-th-h1 font-heading font-semibold mb-4">Atomic widgets</h2>
                <div className="grid grid-cols-3 gap-6 bg-white p-6 rounded-md">
                  <KPITile value="127k" label="Monthly active users" trend="+18%" trendDirection="up" />
                  <KPITile value="94%"  label="Month-1 retention"     trend="+3pp" trendDirection="up" />
                  <KPITile value="12d"  label="Time to value"          trend="-3d"  trendDirection="down" />
                </div>
                <div className="mt-6 flex gap-3">
                  <StatusPill status="done" />
                  <StatusPill status="in_progress" />
                  <StatusPill status="at_risk" />
                  <StatusPill status="blocked" />
                  <StatusPill status="planned" />
                  <Badge>Custom badge</Badge>
                </div>
                <div className="mt-6 grid grid-cols-4 gap-6 bg-white p-6 rounded-md">
                  <PersonCard name="Jan Andrzejczuk" role="Venture Architect"
                    bio="7y in venture building at Digital Gateways, AIS Gateway." />
                  <PersonCard name="Tomasz Czapliński" role="Co-founder"
                    bio="Managing Partner at SpeedUp VC; investment and BD lead." />
                  <PersonCard name="Tomasz Wilczak" role="Product Owner"
                    bio="6y in product strategy across online banking and education." />
                  <PersonCard name="Bartosz Gembicki" role="COO"
                    bio="10y in operations management at Nomad Electric and Polenergia." />
                </div>
                <div className="mt-6 bg-white p-10 rounded-md">
                  <BigStat value="€4.2B" caption="uncaptured loyalty revenue in CEE" />
                </div>
              </section>

              <section className="max-w-5xl mx-auto space-y-6">
                <h2 className="text-th-h1 font-heading font-semibold">Slide patterns</h2>

                <Cover title="ScanPay" subtitle="Dining kiosk in your mobile" />

                <Problem3Col
                  title="Labor shortages push restaurants to digitise"
                  subtitle="Rising costs and changing expectations meet a tightening labour market"
                  columns={[
                    { heading: "68%", body: "of customers prefer self-service" },
                    { heading: "97%", body: "of restaurants cite rising costs"  },
                    { heading: "45%", body: "of operators understaffed"          },
                  ]}
                  pageNumber={3} totalPages={13}
                />

                <OKRBoard
                  title="Q4 OKR scorecard"
                  objective="Become the default payment method for Polish QSRs by end of Q4."
                  keyResults={[
                    { label: "Active restaurants",  current: "117",     target: "200",       status: "on_track" },
                    { label: "Monthly recurring revenue", current: "98k PLN", target: "150k PLN", status: "at_risk"  },
                    { label: "NPS",                 current: "62",      target: ">50",      status: "done"     },
                  ]}
                />

                <SWOTGrid
                  title="Where we win and where we are exposed"
                  strengths={["Self-checkout 4× faster than competition", "POS integrations cover 80% of market"]}
                  weaknesses={["Brand recognition still low", "Only 2 enterprise deals closed"]}
                  opportunities={["EU regulation forcing transparency in tips", "12% CAGR food service market"]}
                  threats={["Square entering CEE in 2027", "Rising payment processing fees"]}
                />

                <Roadmap
                  title="Roadmap to Series A"
                  milestones={[
                    { date: "Q2 2025", label: "Slovakia pilot",       status: "done" },
                    { date: "Q3 2025", label: "Czech expansion",      status: "in_progress" },
                    { date: "Q4 2025", label: "200 restaurants live", status: "in_progress" },
                    { date: "Q1 2026", label: "Series A close",       status: "planned" },
                  ]}
                />

                <CompetitiveMatrix
                  title="Where we beat the incumbents"
                  columns={["ScanPay", "SumUp", "Square", "Glovo Pay"]}
                  rows={[
                    { label: "Self-order menu",  values: [true, false, false, true] },
                    { label: "Bill splitting",   values: [true, false, true,  false] },
                    { label: "POS integrations", values: ["6", "12", "4", "2"] },
                  ]}
                />

                <BigQuote
                  quote="Banks spend 14 months building what we ship in 4 weeks."
                  attribution="Head of Innovation, Top 5 EU bank"
                />

                <BeforeAfter
                  title="What changes for a restaurant on day one"
                  before={{ heading: "Before", bullets: ["8-min checkout", "Cash tips lost", "POS reprogramming"] }}
                  after={{ heading: "After", bullets: ["30s self-pay", "Cashless tips routed", "Menu pushes live"] }}
                />

                <ValueProp
                  title="Three sides of the value prop"
                  segments={[
                    { name: "For customers",   pain: "Long wait.",          gain: "30-second checkout." },
                    { name: "For restaurants", pain: "Staff shortage.",     gain: "Higher turnover." },
                    { name: "For waiters",     pain: "Cash tips in pocket.", gain: "Cashless tips routed." },
                  ]}
                />

                <CustomerJourney
                  title="How a guest experiences ScanPay"
                  steps={[
                    { label: "Discover", body: "Sees QR on the table." },
                    { label: "Browse",   body: "Filters menu in 10s." },
                    { label: "Order",    body: "Adds items, sends to kitchen." },
                    { label: "Pay",      body: "Splits, tips, leaves." },
                  ]}
                />

                <WeeklyStatus
                  title="Workstream health"
                  streams={[
                    { name: "Product",     status: "on_track",    summary: "Beta shipped to 12 design partners." },
                    { name: "Sales",       status: "at_risk",     summary: "Two enterprise deals slipped to Q2." },
                    { name: "Engineering", status: "done",        summary: "Migration complete." },
                    { name: "Marketing",   status: "in_progress", summary: "Content engine 3 pieces / week." },
                  ]}
                />
              </section>
            </div>
          );
        }
        ''')


def _readme(brand: dict) -> str:
    company = brand.get("identity", {}).get("company_name", "The Heart")
    return dedent(f'''\
        # {company} — Design System

        Auto-generated from the `deck-builder` plugin.

        This repository contains the brand's design tokens and a typed React
        component library. It is importable into **Claude Design** via
        `setup = design-system → repo URL`.

        ## Quick start

        ```bash
        npm install
        npm run dev    # opens the Showcase page at http://localhost:5173
        ```

        ## What's inside

        ```
        tokens.json              W3C Design Tokens (DTCG)
        tailwind.preset.cjs      Tailwind theme exposing brand tokens
        src/tokens/tokens.css    CSS custom properties (--th-*)
        src/components/          Atomic widgets (KPITile, PersonCard, StatusPill, …)
        src/patterns/            Page-level slide patterns (Cover, OKRBoard, SWOTGrid, …)
        src/examples/Showcase    Renders every widget + pattern with realistic data
        ```

        ## Token namespacing

        All tokens live under the `th-` namespace so they don't collide with other
        token systems:

        | CSS variable                | Tailwind utility            | Token path             |
        | --------------------------- | --------------------------- | ---------------------- |
        | `--th-color-primary`        | `bg-th-primary`             | `color.brand.primary`  |
        | `--th-color-status-done`    | `bg-th-status-done`         | `color.status.done`    |
        | `--th-font-heading`         | `font-heading`              | `font.family.heading`  |
        | `--th-text-h1`              | `text-th-h1`                | `font.size.h1`         |

        ## Brand rules baked in

        - Primary red **#E61B25** dominates.
        - Blue **#0056A4** is **accent if needed** — never used for status
          colours; an "in progress" pill renders as black, not blue.
        - Typography is **Raleway** (regular / SemiBold / Light) with Arial as
          the documented fallback.
        - Status palette mirrors the plugin's
          [`colors.py`](../layouts/colors.py).

        ## Provenance

        Every file is regenerated by:

        ```bash
        python3 export_design_system.py --output ./dist/design-system
        ```

        Do not hand-edit — change `brand.yaml`, `layouts/widgets.py`, or
        `layouts/generic/*.py` upstream, then re-export.
        ''')


def _gitignore() -> str:
    return dedent('''\
        node_modules/
        dist/
        .vite/
        .DS_Store
        *.log
        ''')


def write_scaffold(out_dir, brand: dict):
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "README.md").write_text(_readme(brand))
    (out_dir / "package.json").write_text(_pkg_json(brand))
    (out_dir / "tsconfig.json").write_text(_tsconfig())
    (out_dir / "vite.config.ts").write_text(_vite_config())
    (out_dir / "tailwind.config.cjs").write_text(_tailwind_config())
    (out_dir / "postcss.config.cjs").write_text(_postcss_config())
    (out_dir / "index.html").write_text(_index_html(brand))
    (out_dir / ".gitignore").write_text(_gitignore())

    src = out_dir / "src"
    src.mkdir(exist_ok=True)
    (src / "main.tsx").write_text(_main_tsx())
    (src / "App.tsx").write_text(_app_tsx())
    (src / "vite-env.d.ts").write_text(
        '/// <reference types="vite/client" />\n'
        '// Required so `import svg from "./foo.svg?raw"` is typed as a string.\n'
        'declare module "*.svg?raw" { const content: string; export default content; }\n'
    )
    examples = src / "examples"
    examples.mkdir(exist_ok=True)
    (examples / "Showcase.tsx").write_text(_showcase_tsx())
