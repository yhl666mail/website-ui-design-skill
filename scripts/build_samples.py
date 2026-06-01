#!/usr/bin/env python3
"""Validate and compile every website sample style pack."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WEBSITE_STYLE_PACK_DIR = ROOT / "assets" / "website-style-packs"
STYLE_SYSTEM_TEMPLATE = ROOT / "assets" / "html-template" / "style-system.html"
WEBSITE_TEMPLATE = ROOT / "assets" / "html-template" / "website-page.html"
DIST = ROOT / "dist"


def run(command: list[str]) -> None:
    print("$ " + " ".join(command))
    subprocess.run(command, cwd=ROOT, check=True)


def website_slug(path: Path) -> str:
    return path.name.removesuffix(".website.json")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build website sample style-pack artifacts.")
    parser.add_argument(
        "--strict-optional",
        action="store_true",
        default=True,
        help="Validate optional website component detail fields. Enabled by default.",
    )
    args = parser.parse_args()

    packs = sorted(WEBSITE_STYLE_PACK_DIR.glob("*.website.json"))
    if not packs:
        print(f"no website style packs found in {WEBSITE_STYLE_PACK_DIR}")
        return 1

    DIST.mkdir(parents=True, exist_ok=True)

    for pack in packs:
        slug = website_slug(pack)
        validate_cmd = [
            sys.executable,
            "scripts/validate_website_style_pack.py",
            "--style-pack",
            str(pack.relative_to(ROOT)),
        ]
        if args.strict_optional:
            validate_cmd.append("--strict-optional")
        run(validate_cmd)

        run(
            [
                sys.executable,
                "scripts/compile_style_pack.py",
                "--style-pack",
                str(pack.relative_to(ROOT)),
                "--template",
                str(STYLE_SYSTEM_TEMPLATE.relative_to(ROOT)),
                "--out",
                f"dist/{slug}-website-style-system.html",
            ]
        )
        run(
            [
                sys.executable,
                "scripts/compile_style_pack.py",
                "--style-pack",
                str(pack.relative_to(ROOT)),
                "--template",
                str(WEBSITE_TEMPLATE.relative_to(ROOT)),
                "--out",
                f"dist/{slug}-website.html",
            ]
        )

    print(f"built {len(packs)} website sample style packs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
