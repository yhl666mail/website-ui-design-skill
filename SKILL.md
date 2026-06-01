---
name: website-ui-design
description: Use when generating, redesigning, or reviewing public website UI artifacts such as landing pages, brand sites, product pages, portfolios, event pages, editorial pages, ecommerce pages, and single-file HTML websites; selecting website page, section, and aesthetic direction templates; creating website style packs; refining website section/component styles after a global style is chosen; compiling placeholder HTML/CSS website templates; or authoring new template metadata for AI-driven website UI selection.
metadata:
  short-description: Style-pack-driven website UI design
---

# Website UI Design

Use this skill to turn website intent into polished public-facing website UI artifacts through
explicit design decisions, reusable templates, component style recipes, and a
critique loop.

This skill is website-first. It is for public-facing website pages and sections,
not admin dashboards, internal tools, or backend management screens.

The skill supports two primary design levels:

- **Whole-site/page design**: choose a website archetype, combine website sections, derive an aesthetic direction, then produce a complete HTML artifact.
- **Section refinement**: improve one specific website section inside an existing page, preserving surrounding layout, tokens, and brand intent.
- **Style-pack compilation**: generate a structured style pack, compile it into
  a placeholder HTML/CSS template, then use that template as the user's design
  foundation.

It can also be used to add or update templates.

## Core Workflow

1. Infer a `UIIntent` from the user request:
   - `product_type`
   - `audience`
   - `website_goal`
   - `content_density`
   - `content_shape`
   - `interaction_depth`
   - `platform`
   - `brand_tone`
   - `constraints`
2. Select structure templates:
   - For whole pages, read `templates/pages/index.yaml`, then the relevant page template.
   - For website sections, read `references/website-section-refinement.md`, `templates/website-sections/index.yaml`, then the relevant section template.
3. Select an aesthetic direction:
   - Read `templates/aesthetic-directions/index.yaml`, then one direction template.
   - Commit to one memory point that will make the UI feel designed for this product.
4. Create a style pack:
   - Read `references/style-pack-workflow.md`.
   - Use `schemas/style-pack.schema.json` as the structural contract.
   - Derive tokens and component decisions from the chosen aesthetic direction.
5. Refine component styles:
   - Read `references/component-style-system.md`.
   - Read `templates/component-recipes/index.yaml`, then recipes for important website components.
   - Ensure site header, hero, buttons, feature sections, proof, testimonials, pricing, FAQ, CTA, footer, cards, media, and forms adapt to the global style.
6. Optionally compile a reusable style template:
   - Validate style-pack depth with `scripts/validate_style_pack.py` when component detail matters.
   - Use `scripts/compile_style_pack.py` with `assets/html-template/style-system.html`.
   - The compiled output is a style foundation, not the final page unless the user asked for a design-system preview.
7. Generate or revise the HTML:
   - Prefer a single self-contained HTML file unless working inside an existing codebase.
   - Use semantic HTML, CSS variables, responsive constraints, and real states.
   - Preserve existing stack and design tokens when editing existing code.
8. Critique before finalizing:
   - Read `references/anti-ai-slop.md` for visual quality failures.
   - Read `references/expectation-lift-rubric.md` to add useful product-specific details beyond a generic template.
   - Read `references/accessibility.md` when forms, navigation, controls, charts, or production-like UX are involved.
   - Fix issues before delivering.
9. Verify visually when possible:
   - Open or render the HTML.
   - Check at least mobile and desktop widths.
   - Confirm text does not overflow or overlap.

## Reference Map

- `references/selection-rubric.md`: template selection, scoring, and tie breakers.
- `references/style-pack-workflow.md`: style pack generation and compiler flow.
- `references/component-style-system.md`: how global style becomes component-level detail.
- `references/expectation-lift-rubric.md`: how to make the output exceed a generic template.
- `references/website-section-refinement.md`: targeted website section redesign workflow.
- `references/anti-ai-slop.md`: visual quality failures to avoid.
- `references/accessibility.md`: accessibility checks for website UI.
- `references/template-authoring.md`: how to add or upgrade templates.

## Template Model

Templates are not static screenshots or fixed CSS themes. They are decision
records. Each template must explain:

- when to use it
- when to avoid it
- required sections or elements
- required states
- layout rules
- compatible aesthetic directions
- common failure modes

Do not blindly copy a template. Use it to decide structure, density, states,
constraints, and style behavior.

## Style Pack Model

After choosing an aesthetic direction, generate a style pack:

```text
UIIntent -> aesthetic direction -> memory point -> style pack -> component recipes -> HTML/CSS
```

The style pack is the bridge between freeform design judgment and deterministic
HTML output. It should contain:

- global tokens: colors, typography, spacing, radius, shadow, motion, sizes
- website component decisions: site header, hero, button, feature section, proof, testimonial, pricing, FAQ, CTA, footer, card, form
- quality gates: the checks this specific UI must satisfy

Do not hard-code one permanent style for a component. Describe how the component
expresses the selected global style.

## Whole-Page Design

Use this path when the user asks for a website, landing page, product page,
brand site, portfolio, event page, editorial page, ecommerce page, campaign
page, or public-facing prototype.

Minimum output expectations:

- coherent information hierarchy
- responsive layout for mobile and desktop
- clear primary visitor action
- realistic content, not filler
- hover, focus, empty, loading, and error states where relevant
- one dominant visual direction
- one visible memory point tied to the brand, offer, product, or story
- detailed component states shaped by the style pack
- no decorative clutter that weakens the task

Avoid defaulting to dashboard, table, sidebar, admin, or internal-tool patterns
unless the user explicitly asks for an app or management surface.

If no stack is specified, create `index.html` using plain HTML, CSS, and minimal
vanilla JavaScript only when interaction is needed.

## Website Section Refinement

Use this path when the user asks to improve a specific website section, such as:

- site header
- hero
- feature section
- product preview
- proof strip
- testimonial section
- pricing section
- FAQ
- CTA band
- footer
- newsletter/contact form
- gallery/editorial section

Rules:

- Keep the section boundary tight.
- Preserve surrounding page architecture unless the user asks for a broader redesign.
- Reuse existing tokens and component conventions when present.
- If a global style is missing, infer or create a style pack before changing component details.
- Add missing states and accessibility semantics.
- Do not introduce a new visual language for one section unless the current page has no coherent system.

## Compiler Workflow

Use the compiler when the user wants templates, reusable style foundations, or a
repeatable style system:

```bash
python scripts/build_samples.py

python scripts/validate_website_style_pack.py \
  --style-pack assets/website-style-packs/editorial-premium.website.json \
  --strict-optional

python scripts/compile_style_pack.py \
  --style-pack assets/website-style-packs/editorial-premium.website.json \
  --template assets/html-template/website-page.html \
  --out dist/editorial-premium-website.html
```

For final user work, create a user-specific style pack first instead of relying
on the sample pack.

## Output Contract

For a new standalone artifact:

- Use one HTML file.
- Put reusable values in `:root` CSS variables.
- Include a compact reset.
- Use semantic landmarks where appropriate.
- Use stable dimensions for headers, hero media, grids, cards, galleries, forms, and navigation.
- Use media queries or container-aware rules for responsiveness.
- Keep scripts small and local to demonstrable interaction.

For existing code:

- Match the project framework and local conventions.
- Keep edits scoped to the requested module or screen.
- Avoid unrelated refactors.

## Upgrade Path

When adding templates, follow `references/template-authoring.md`.

Keep `SKILL.md` stable. Add new design knowledge as templates or references so
future versions can expand without bloating the core workflow.
