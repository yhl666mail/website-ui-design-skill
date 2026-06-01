# Template Authoring

Use this reference when adding or upgrading templates.

## Template Rules

- Use ASCII file names and kebab-case IDs.
- Use semantic versioning in `version`.
- Keep each template focused on one page, block, or style.
- Include both `use_when` and `avoid_when`.
- Include required states for interactive or data-backed UI.
- Include anti-patterns so AI can reject bad fits.
- Add the new template to the matching `index.yaml`.

## Required Fields

```yaml
id: example-template
version: 1.0.0
kind: page | block | aesthetic-direction | component-recipe
summary: ""
use_when: []
avoid_when: []
```

## Page Template Fields

```yaml
audience: []
density: low | medium | high
goals: []
required_sections: []
optional_sections: []
required_states: []
layout_rules: []
common_blocks: []
compatible_aesthetic_directions: []
anti_patterns: []
output_notes: []
```

## Block Template Fields

```yaml
role: ""
required_elements: []
state_rules: []
layout_rules: []
content_rules: []
accessibility_notes: []
anti_patterns: []
```

## Aesthetic Direction Template Fields

```yaml
intent:
  emotional_quality: ""
  work_quality: ""
  visual_energy: ""
  density_bias: ""
memory_point_prompts: []
token_rules:
  color: {}
  typography: {}
  spacing: {}
  radius: {}
  shadow: {}
  motion: {}
component_tendencies: {}
anti_patterns: []
```

Do not make aesthetic directions fixed themes. Avoid hard-coded palettes unless
they are examples. Use token rules and behavior descriptions.

## Component Recipe Fields

```yaml
role: ""
summary: ""
anatomy: []
variants: []
tokens_consumed: {}
state_matrix: {}
style_behavior:
  quiet-saas: {}
  editorial-premium: {}
  technical-product: {}
responsive_rules: []
accessibility_rules: []
anti_patterns: []
exceed_expectations: []
```

Component recipes describe how a component responds to a global style. They
should cover structure, states, responsiveness, accessibility, and one
product-specific detail that can lift the result above a generic template.

## Versioning

- Patch version: wording, examples, or small rule clarifications.
- Minor version: new sections, states, or compatibility additions.
- Major version: changed selection semantics or incompatible structure.

Do not delete templates used by downstream agents. Mark them as deprecated with
`deprecated: true` and add a replacement ID.

