#!/usr/bin/env python3
"""Validate website style pack depth for public-facing UI design."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, List


CORE_COMPONENTS = ["site_header", "hero", "button", "feature", "proof", "cta", "footer"]
OPTIONAL_COMPONENTS = ["testimonial", "pricing", "faq", "card", "form"]
DETAIL_FIELDS = [
    "role",
    "style_intent",
    "anatomy_detail",
    "states",
    "responsive_behavior",
    "accessibility_behavior",
    "exceed_expectations",
]
TOKEN_FAMILIES = ["color", "typography", "spacing", "radius", "shadow", "motion", "size"]


def get(data: Dict[str, Any], path: str) -> Any:
    current: Any = data
    for part in path.split("."):
        if not isinstance(current, dict) or part not in current:
            return None
        current = current[part]
    return current


def validate_text(path: str, value: Any, errors: List[str], min_words: int = 4) -> None:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{path} must be a non-empty string")
        return
    words = re.findall(r"[A-Za-z0-9_'-]+", value)
    if len(words) < min_words:
        errors.append(f"{path} is too shallow; expected at least {min_words} words")


def validate_component(name: str, component: Any, errors: List[str]) -> None:
    path = f"components.{name}"
    if not isinstance(component, dict):
        errors.append(f"{path} must be an object")
        return
    for field in DETAIL_FIELDS:
        if field not in component:
            errors.append(f"{path}.{field} is required")

    validate_text(f"{path}.role", component.get("role"), errors, 3)
    validate_text(f"{path}.style_intent", component.get("style_intent"), errors, 8)
    validate_text(f"{path}.responsive_behavior", component.get("responsive_behavior"), errors, 8)
    validate_text(f"{path}.accessibility_behavior", component.get("accessibility_behavior"), errors, 8)
    validate_text(f"{path}.exceed_expectations", component.get("exceed_expectations"), errors, 8)

    anatomy = component.get("anatomy_detail")
    if not isinstance(anatomy, list) or len(anatomy) < 3:
        errors.append(f"{path}.anatomy_detail must include at least 3 parts")
    elif any(not isinstance(item, str) or not item.strip() for item in anatomy):
        errors.append(f"{path}.anatomy_detail items must be non-empty strings")

    states = component.get("states")
    if not isinstance(states, dict) or len(states) < 4:
        errors.append(f"{path}.states must describe at least 4 states")
    else:
        for state_name, state_value in states.items():
            validate_text(f"{path}.states.{state_name}", state_value, errors, 5)


def validate_style_pack(style_pack: Dict[str, Any], strict_optional: bool) -> List[str]:
    errors: List[str] = []
    for path, min_words in [
        ("meta.name", 2),
        ("meta.version", 1),
        ("meta.aesthetic_direction", 1),
        ("meta.audience", 3),
        ("meta.density", 1),
        ("meta.memory_point", 8),
    ]:
        validate_text(path, get(style_pack, path), errors, min_words)

    for family in TOKEN_FAMILIES:
        value = get(style_pack, f"tokens.{family}")
        if not isinstance(value, dict) or not value:
            errors.append(f"tokens.{family} must be a non-empty object")

    colors = get(style_pack, "tokens.color") or {}
    for color_name in ["background", "surface", "text", "muted", "border", "accent", "focus"]:
        value = colors.get(color_name)
        if not isinstance(value, str) or not re.match(r"^#[0-9a-fA-F]{6}$", value):
            errors.append(f"tokens.color.{color_name} must be a 6-digit hex color")

    components = style_pack.get("components")
    if not isinstance(components, dict):
        errors.append("components must be an object")
        return errors

    for name in CORE_COMPONENTS:
        validate_component(name, components.get(name), errors)
    if strict_optional:
        for name in OPTIONAL_COMPONENTS:
            validate_component(name, components.get(name), errors)

    quality_gates = style_pack.get("quality_gates")
    if not isinstance(quality_gates, list) or len(quality_gates) < 3:
        errors.append("quality_gates must include at least 3 website checks")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate website style pack detail depth.")
    parser.add_argument("--style-pack", required=True, type=Path)
    parser.add_argument("--strict-optional", action="store_true")
    args = parser.parse_args()

    style_pack = json.loads(args.style_pack.read_text(encoding="utf-8"))
    errors = validate_style_pack(style_pack, args.strict_optional)
    if errors:
        print("website style pack validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"website style pack validation passed: {args.style_pack}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
