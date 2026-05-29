#!/usr/bin/env python3
"""CLI entry point for the design-system exporter.

Usage:
    python3 export_design_system.py [--output ./dist/design-system] [--no-git]
"""
import argparse
from pathlib import Path

from design_system import export_design_system


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Export The Heart design system as a Claude-Design-importable repo.",
    )
    parser.add_argument("--brand", default="brand.yaml",
                        help="Path to brand.yaml (default: brand.yaml)")
    parser.add_argument("--output", default="dist/design-system",
                        help="Output directory (default: dist/design-system)")
    parser.add_argument("--no-git", action="store_true",
                        help="Skip initialising a git repository in the output dir")
    args = parser.parse_args()

    out = export_design_system(
        brand_path=str(Path(args.brand).resolve()),
        output_dir=args.output,
        init_git=not args.no_git,
    )
    print(f"\nDesign system ready at: {out}")
