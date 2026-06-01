# Style Pack Workflow

Use this workflow when the user wants a public website that adapts to their
product, brand, story, and audience instead of using a fixed theme.

## Pipeline

```text
WebsiteIntent
  -> aesthetic direction
  -> memory point
  -> style pack JSON
  -> component recipes
  -> compiled HTML/CSS template
  -> page implementation
  -> critique
```

The AI designs the style pack. The compiler only turns structured decisions
into usable files.

## Required Design Decision

Before writing UI code, produce a compact design decision like this:

```yaml
selected_page: landing-page
selected_blocks:
  - site-header
  - website-hero
  - feature-section
  - proof-section
  - testimonial-section
  - pricing-section
  - faq-section
  - cta-section
  - site-footer
aesthetic_direction: editorial-premium
memory_point: "An annotated product briefing that makes the offer memorable before the first scroll ends."
token_strategy: "Warm editorial base, high-contrast accent, strong display typography, restrained cards, concrete proof captions."
component_strategy: "Hero, features, proof, pricing, FAQ, CTA, and footer all inherit the same editorial briefing language."
```

Do not expose this decision to the user unless it helps explain tradeoffs or the
user asked for the design rationale.

## Style Pack Responsibilities

A style pack must define:

- `meta`: name, version, aesthetic direction, audience, density, memory point
- `tokens`: color, typography, spacing, radius, shadow, motion, size
- `components`: website section and component style decisions derived from the tokens
- `quality_gates`: checks the output must satisfy

The style pack should be specific enough for consistent output, but flexible
enough that pages do not all look the same.

## Component Detail Contract

Each important website component in `components` must include:

```json
{
  "role": "What this component does in the workflow.",
  "style_intent": "How the global aesthetic appears in this component.",
  "anatomy_detail": [
    "Specific parts the component must render or account for."
  ],
  "states": {
    "default": "Baseline appearance and behavior.",
    "hover": "Pointer feedback.",
    "focus": "Keyboard-visible focus.",
    "loading": "Async or pending behavior."
  },
  "responsive_behavior": "How the component changes on narrow screens.",
  "accessibility_behavior": "Labels, semantics, focus, contrast, and non-color status.",
  "exceed_expectations": "One product-specific detail beyond a generic component."
}
```

This contract prevents shallow style packs that only set colors. If a section
is central to the website, it must have a detailed style decision.

## Token Strategy

Prefer token families over one-off values.

Good:

```json
{
  "tokens": {
    "density": { "mode": "compact" },
    "size": { "control_md": "36px", "table_row": "42px" },
    "radius": { "control": "6px", "panel": "10px" }
  }
}
```

Avoid:

```json
{
  "button_padding": "12px 17px",
  "table_cell_padding_left": "13px",
  "hero_card_radius": "11px"
}
```

Use derived values so a few decisions can shape the whole interface.

## Component Refinement

After choosing the overall aesthetic direction, refine each component using
`templates/component-recipes/index.yaml`.

For each component, decide:

- role in the user workflow
- visual weight
- density
- border/elevation policy
- typography policy
- state behavior
- responsive behavior
- accessibility behavior
- one detail that makes it feel designed for this product

Minimum website component coverage:

- Product/brand site: `site_header`, `hero`, `button`, `feature`, `proof`, `testimonial`, `cta`, `footer`
- SaaS landing page: `site_header`, `hero`, `feature`, `proof`, `pricing`, `faq`, `cta`, `footer`, `button`, `card`
- Portfolio/editorial site: `site_header`, `hero`, `feature`, `proof`, `testimonial`, `cta`, `footer`
- Ecommerce/product page: `site_header`, `hero`, `proof`, `pricing`, `faq`, `cta`, `footer`, `form`

## Compiler Use

When a standalone HTML style template is useful:

1. Create or edit a style pack JSON.
2. Run `scripts/compile_style_pack.py`.
3. Use the compiled HTML/CSS as the design system basis for the page.

Example:

```bash
python scripts/compile_style_pack.py \
  --style-pack assets/website-style-packs/editorial-premium.website.json \
  --template assets/html-template/style-system.html \
  --out dist/editorial-premium-website-style-system.html
```

The generated file is not the final page. It is the user's website style foundation.
Use it to build the actual requested page or section.

To prove a style pack works on a real website, compile the website template:

```bash
python scripts/build_samples.py

python scripts/compile_style_pack.py \
  --style-pack assets/website-style-packs/editorial-premium.website.json \
  --template assets/html-template/website-page.html \
  --out dist/editorial-premium-website.html
```

The website template intentionally exercises site header, hero, product preview,
features, proof, testimonial, pricing, FAQ, CTA, footer, buttons, cards, and
lead/contact-ready form tokens.

## Quality Bar

The result should feel like a designed interface, not a token swap.

Check:

- Does the memory point show up in layout, content, or interaction?
- Do components share a system without looking identical?
- Are states designed, not just colored?
- Does the density match the audience's work?
- Are typography, color, spacing, radius, shadow, and motion pulling in the same direction?

Then apply `expectation-lift-rubric.md`. At least three expectation-lift
decisions should be visible in the final artifact for important UI work.
