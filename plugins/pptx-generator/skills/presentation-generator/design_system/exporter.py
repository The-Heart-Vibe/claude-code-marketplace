"""exporter — orchestrate token, component, pattern, and scaffold writes.

Public entry point:

    from design_system import export_design_system
    export_design_system(brand_path="brand.yaml", output_dir="./dist/design-system")
"""
from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Optional

import yaml

from . import tokens, components, patterns, scaffold, icons, logos


def export_design_system(
    brand_path: str = "brand.yaml",
    output_dir: str = "dist/design-system",
    init_git: bool = True,
) -> Path:
    out = Path(output_dir).resolve()
    out.mkdir(parents=True, exist_ok=True)

    brand = yaml.safe_load(Path(brand_path).read_text())

    print(f"  [design-system] target: {out}")

    # 1. Scaffold (package.json, README, vite, tailwind, examples)
    scaffold.write_scaffold(out, brand)

    # 2. Tokens — DTCG + CSS + Tailwind preset
    (out / "tokens.json").write_text(json.dumps(tokens.to_dtcg(brand), indent=2))
    (out / "tailwind.preset.cjs").write_text(tokens.to_tailwind_preset(brand))
    (out / "src" / "tokens").mkdir(parents=True, exist_ok=True)
    (out / "src" / "tokens" / "tokens.css").write_text(tokens.to_css(brand))

    # 3. Atomic widgets → src/components/
    components.write_components(out / "src" / "components")

    # 4. Slide patterns → src/patterns/
    patterns.write_patterns(out / "src" / "patterns")

    # 5. Lucide icon library → src/icons/
    plugin_root = Path(brand_path).resolve().parent
    icons.write_icons(plugin_root, out / "src" / "icons")

    # 6. Brand logos (3 variants × 3 themes) → src/logos/
    logos.write_logos(plugin_root, out / "src" / "logos")

    # 7. Companion Claude skill — copy from the plugin so anyone who clones
    #    the design system also gets the on-brand-frontend instructions for
    #    Claude Code / Claude Design.
    skill_src = plugin_root / "skills" / "theheart-frontend" / "SKILL.md"
    if skill_src.exists():
        (out / ".claude" / "skills" / "theheart-frontend").mkdir(parents=True, exist_ok=True)
        (out / ".claude" / "skills" / "theheart-frontend" / "SKILL.md").write_text(
            skill_src.read_text(),
        )

    # 8. Prompts — copy the canonical Claude-Design "Other notes" text so
    #    anyone using this repo with Claude Design can paste the same
    #    on-brand instructions without reinventing them.
    prompts_src = plugin_root / "prompts"
    if prompts_src.is_dir():
        (out / "prompts").mkdir(parents=True, exist_ok=True)
        for prompt_file in prompts_src.glob("*.md"):
            (out / "prompts" / prompt_file.name).write_text(prompt_file.read_text())

    # 9. Optional git init so the directory is immediately importable
    if init_git and not (out / ".git").exists():
        try:
            subprocess.run(["git", "init", "-q", "-b", "main", str(out)], check=True)
            subprocess.run(["git", "-C", str(out), "add", "."], check=True)
            subprocess.run(
                ["git", "-C", str(out), "commit", "-q",
                 "-m", "feat: initial design-system export"],
                check=True,
                env=_git_env(),
            )
            print("  [design-system] initialised git repo")
        except subprocess.CalledProcessError as e:
            print(f"  [design-system] git init skipped: {e}")
        except FileNotFoundError:
            print("  [design-system] git not installed — skipping repo init")

    print(f"  [design-system] done → {out}")
    return out


def _git_env() -> dict:
    """Avoid signing/identity blowups on machines with strict git config."""
    import os
    env = os.environ.copy()
    env.setdefault("GIT_AUTHOR_NAME",  "deck-builder")
    env.setdefault("GIT_AUTHOR_EMAIL", "deck-builder@theheart.tech")
    env.setdefault("GIT_COMMITTER_NAME",  env["GIT_AUTHOR_NAME"])
    env.setdefault("GIT_COMMITTER_EMAIL", env["GIT_AUTHOR_EMAIL"])
    return env
