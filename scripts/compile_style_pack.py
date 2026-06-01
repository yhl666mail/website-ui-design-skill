#!/usr/bin/env python3
"""Compile a style pack JSON into a placeholder-based HTML template.

This script intentionally uses only the Python standard library so the skill can
run in minimal local environments.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple


PLACEHOLDER_RE = re.compile(r"{{\s*([a-zA-Z0-9_.-]+)\s*}}")


DEFAULT_STYLE_PACK: Dict[str, Any] = {
    "meta": {
        "name": "Generated UI Style",
        "version": "0.1.0",
        "aesthetic_direction": "quiet-saas",
        "audience": "product users",
        "density": "standard",
        "memory_point": "A clear interface with one memorable product-specific detail.",
    },
    "tokens": {
        "color": {
            "background": "#F7F8FA",
            "surface": "#FFFFFF",
            "surface_alt": "#F1F3F5",
            "elevated": "#FFFFFF",
            "text": "#1F2328",
            "muted": "#667085",
            "border": "#D9DEE7",
            "accent": "#2563EB",
            "accent_soft": "#EAF1FF",
            "focus": "#7AA7FF",
            "success": "#16875A",
            "warning": "#B7791F",
            "danger": "#C2413A",
            "row_hover": "#F3F6FA",
            "selected": "#EAF1FF",
            "field": "#FFFFFF",
        },
        "typography": {
            "font_body": "Inter, ui-sans-serif, system-ui, sans-serif",
            "font_display": "Inter, ui-sans-serif, system-ui, sans-serif",
            "font_mono": "\"SFMono-Regular\", Consolas, monospace",
            "body_size": "14px",
            "label_size": "12px",
            "heading_weight": "700",
            "numeral_style": "tabular-nums",
        },
        "spacing": {
            "page": "24px",
            "section": "28px",
            "panel": "16px",
            "card_padding": "16px",
            "field_gap": "8px",
            "control_gap": "10px",
            "table_cell_x": "12px",
        },
        "radius": {
            "control": "7px",
            "panel": "10px",
            "pill": "999px",
        },
        "shadow": {
            "panel": "0 14px 40px rgba(31, 35, 40, 0.08)",
            "overlay": "0 24px 80px rgba(31, 35, 40, 0.18)",
            "action": "none",
        },
        "motion": {
            "duration_fast": "120ms",
            "duration_base": "180ms",
            "ease_standard": "cubic-bezier(0.2, 0.8, 0.2, 1)",
        },
        "size": {
            "control_sm": "30px",
            "control_md": "38px",
            "control_lg": "44px",
            "table_row": "44px",
            "nav_height": "48px",
        },
    },
    "components": {
        "button": {
            "primary_bg": "#2563EB",
            "primary_fg": "#FFFFFF",
            "secondary_bg": "#FFFFFF",
            "secondary_fg": "#1F2328",
            "border": "#D9DEE7",
            "hover_transform": "translateY(-1px)",
            "loading_label": "Working",
        },
        "card": {
            "surface": "#FFFFFF",
            "header_bg": "#F7F8FA",
            "border": "#D9DEE7",
            "metadata_color": "#667085",
            "status_detail": "Context metadata is visible where it helps decisions.",
        },
        "table": {
            "row_height": "44px",
            "header_bg": "#F7F8FA",
            "row_hover": "#F3F6FA",
            "status_style": "text labels plus color",
            "decision_column": "Status",
        },
        "form": {
            "field_bg": "#FFFFFF",
            "field_border": "#D9DEE7",
            "focus_border": "#2563EB",
            "helper_tone": "plain and actionable",
            "safety_detail": "Review changes before saving.",
        },
        "nav": {
            "background": "#FFFFFF",
            "active_bg": "#EAF1FF",
            "active_fg": "#1F2328",
            "scope_detail": "Current workspace is visible.",
        },
        "metric": {
            "value_weight": "760",
            "trend_bg": "#EAF1FF",
            "trend_fg": "#2563EB",
            "decision_cue": "Review values outside threshold.",
        },
        "hero": {
            "composition": "product preview with clear primary action",
            "proof_detail": "Shows realistic product state.",
        },
        "pricing": {
            "highlight_rule": "Highlight one recommended option.",
            "fit_cue": "Best fit is explained with concrete criteria.",
        },
        "chat": {
            "tool_call_surface": "#F7F8FA",
            "metadata": "tool status and changed artifact count",
        },
        "empty": {
            "next_action": "Create the first item.",
            "diagnostic_detail": "Explain what is missing.",
        },
    },
    "quality_gates": [],
}


def deep_merge(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    merged = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def lookup(data: Dict[str, Any], path: str) -> str:
    current: Any = data
    for part in path.split("."):
        if isinstance(current, dict) and part in current:
            current = current[part]
        else:
            return ""
    if isinstance(current, (dict, list)):
        return json.dumps(current, ensure_ascii=False)
    return str(current)


def css_var_name(path: Iterable[str]) -> str:
    return "--" + "-".join(part.replace("_", "-") for part in path)


def flatten_scalars(prefix: List[str], value: Any) -> Iterable[Tuple[str, str]]:
    if isinstance(value, dict):
        for key, child in value.items():
            yield from flatten_scalars(prefix + [key], child)
    elif isinstance(value, (str, int, float)):
        yield css_var_name(prefix), str(value)


def build_css_variables(style_pack: Dict[str, Any]) -> str:
    lines = [":root {"]
    for family in ("tokens", "components"):
        for name, value in flatten_scalars([], style_pack.get(family, {})):
            lines.append(f"  {name}: {value};")
    lines.append("}")
    return "\n".join(lines)


def build_component_css() -> str:
    return """
.ui-card {
  background: var(--card-surface, var(--color-surface));
  border: 1px solid var(--card-border, var(--color-border));
  border-radius: var(--radius-panel);
  box-shadow: var(--shadow-panel);
  padding: var(--spacing-card-padding);
}

.ui-card-header {
  display: flex;
  align-items: start;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 14px;
}

.ui-card h2,
.ui-empty h2 {
  margin: 0;
  font-size: 18px;
  line-height: 1.2;
}

.ui-muted {
  color: var(--color-muted);
}

.ui-actions {
  display: flex;
  flex-wrap: wrap;
  gap: var(--spacing-control-gap);
  margin-top: 20px;
}

.ui-button {
  min-height: var(--size-control-md);
  border: 1px solid var(--button-border, var(--color-border));
  border-radius: var(--radius-control);
  padding: 0 13px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  cursor: pointer;
  font-weight: 680;
  transition:
    transform var(--motion-duration-fast) var(--motion-ease-standard),
    border-color var(--motion-duration-fast) var(--motion-ease-standard),
    background var(--motion-duration-fast) var(--motion-ease-standard);
}

.ui-button:hover {
  transform: var(--button-hover-transform, translateY(-1px));
}

.ui-button:focus-visible,
.ui-form :is(input, select, textarea):focus-visible {
  outline: 3px solid color-mix(in srgb, var(--color-focus) 36%, transparent);
  outline-offset: 2px;
}

.ui-button-primary {
  background: var(--button-primary-bg, var(--color-accent));
  color: var(--button-primary-fg, #fff);
  box-shadow: var(--shadow-action);
}

.ui-button-secondary {
  background: var(--button-secondary-bg, var(--color-surface-alt));
  color: var(--button-secondary-fg, var(--color-text));
}

.ui-facts {
  display: grid;
  gap: 12px;
  margin: 0;
}

.ui-facts div {
  padding: 10px 0;
  border-bottom: 1px solid var(--color-border);
}

.ui-facts dt {
  color: var(--color-muted);
  font-size: var(--typography-label-size);
}

.ui-facts dd {
  margin: 3px 0 0;
}

.ui-metric-value {
  font-variant-numeric: var(--typography-numeral-style);
  font-size: 38px;
  line-height: 1;
  font-weight: var(--metric-value-weight, 760);
  margin: 6px 0 8px;
}

.ui-chip,
.ui-status {
  width: fit-content;
  border-radius: var(--radius-pill);
  padding: 4px 8px;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: var(--metric-trend-bg, var(--color-accent-soft));
  color: var(--metric-trend-fg, var(--color-accent));
  font-size: var(--typography-label-size);
  font-weight: 680;
}

.ui-chip-warning {
  background: color-mix(in srgb, var(--color-warning) 16%, transparent);
  color: var(--color-warning);
}

.ui-status.success {
  background: color-mix(in srgb, var(--color-success) 16%, transparent);
  color: var(--color-success);
}

.ui-status.warning {
  background: color-mix(in srgb, var(--color-warning) 16%, transparent);
  color: var(--color-warning);
}

.ui-status.danger {
  background: color-mix(in srgb, var(--color-danger) 16%, transparent);
  color: var(--color-danger);
}

.ui-table-wrap {
  overflow-x: auto;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-control);
}

.ui-table {
  width: 100%;
  min-width: 640px;
  border-collapse: collapse;
  font-variant-numeric: var(--typography-numeral-style);
}

.ui-table th,
.ui-table td {
  height: var(--table-row-height, var(--size-table-row));
  padding: 0 var(--spacing-table-cell-x);
  border-bottom: 1px solid var(--color-border);
  text-align: left;
  white-space: nowrap;
}

.ui-table th {
  background: var(--table-header-bg, var(--color-surface-alt));
  color: var(--color-muted);
  font-size: var(--typography-label-size);
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

.ui-table tbody tr:hover {
  background: var(--table-row-hover, var(--color-row-hover));
}

.ui-table code,
.ui-tool-call {
  font-family: var(--typography-font-mono);
}

.ui-form {
  display: grid;
  gap: 14px;
}

.ui-form label {
  display: grid;
  gap: 7px;
  color: var(--color-muted);
  font-size: var(--typography-label-size);
}

.ui-form input,
.ui-form select {
  width: 100%;
  min-height: var(--size-control-md);
  border: 1px solid var(--form-field-border, var(--color-border));
  border-radius: var(--radius-control);
  background: var(--form-field-bg, var(--color-field));
  color: var(--color-text);
  padding: 0 11px;
}

.ui-chat {
  display: grid;
  gap: 12px;
}

.ui-message {
  max-width: 760px;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-panel);
  padding: 12px 14px;
  background: var(--color-surface-alt);
}

.ui-message.user {
  margin-left: auto;
  background: var(--color-selected);
}

.ui-tool-call {
  border: 1px dashed var(--color-border);
  border-radius: var(--radius-control);
  padding: 10px 12px;
  background: var(--chat-tool-call-surface, var(--color-surface-alt));
  color: var(--color-muted);
  font-size: 13px;
}

.ui-empty {
  display: grid;
  align-content: start;
  gap: 10px;
}
""".strip()


def color_scheme_for_background(style_pack: Dict[str, Any]) -> str:
    value = lookup(style_pack, "tokens.color.background").strip()
    if not re.match(r"^#[0-9a-fA-F]{6}$", value):
        return "light dark"
    red = int(value[1:3], 16) / 255
    green = int(value[3:5], 16) / 255
    blue = int(value[5:7], 16) / 255

    def linear(channel: float) -> float:
        if channel <= 0.03928:
            return channel / 12.92
        return ((channel + 0.055) / 1.055) ** 2.4

    luminance = 0.2126 * linear(red) + 0.7152 * linear(green) + 0.0722 * linear(blue)
    return "light" if luminance > 0.5 else "dark"


def build_context(style_pack: Dict[str, Any]) -> Dict[str, Any]:
    context = dict(style_pack)
    context["generated"] = {
        "css_variables": build_css_variables(style_pack),
        "component_css": build_component_css(),
        "color_scheme": color_scheme_for_background(style_pack),
    }
    return context


def render_template(template: str, context: Dict[str, Any]) -> str:
    def replace(match: re.Match[str]) -> str:
        return lookup(context, match.group(1))

    return PLACEHOLDER_RE.sub(replace, template)


def validate_style_pack(style_pack: Dict[str, Any]) -> List[str]:
    warnings: List[str] = []
    required_paths = [
        "meta.name",
        "meta.version",
        "meta.aesthetic_direction",
        "meta.memory_point",
        "tokens.color.background",
        "tokens.color.surface",
        "tokens.color.text",
        "tokens.color.accent",
        "components.button.primary_bg",
        "components.table.row_height",
    ]
    for path in required_paths:
        if not lookup(style_pack, path):
            warnings.append(f"missing {path}; fallback default was used")
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Compile a style pack into HTML.")
    parser.add_argument("--style-pack", required=True, type=Path)
    parser.add_argument("--template", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()

    user_pack = json.loads(args.style_pack.read_text(encoding="utf-8"))
    style_pack = deep_merge(DEFAULT_STYLE_PACK, user_pack)
    warnings = validate_style_pack(style_pack)
    context = build_context(style_pack)

    template = args.template.read_text(encoding="utf-8")
    output = render_template(template, context)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(output, encoding="utf-8")

    print(f"compiled {args.out}")
    for warning in warnings:
        print(f"warning: {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
