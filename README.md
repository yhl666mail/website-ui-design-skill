# Website UI Design Skill

**Powered by [Codex](https://openai.com/codex/)**

`website-ui-design` is a Codex skill for generating polished public-facing website UI from a product idea. It is designed for landing pages, product pages, brand sites, portfolios, event pages, editorial pages, ecommerce pages, and single-file HTML website prototypes.

This is not a fixed CSS theme. The skill uses a style-pack workflow:

```text
user intent -> website archetype -> aesthetic direction -> style pack -> section/component refinement -> compiled HTML
```

The goal is to help an AI agent decide what a website should feel like, what each section should do, and how every component should express the chosen visual direction.

## Features

- Website-first design logic for public pages, not admin dashboards.
- Page templates for landing pages, product pages, brand sites, portfolios, events, and ecommerce product pages.
- Website section recipes for headers, heroes, features, proof, testimonials, pricing, FAQ, CTA bands, and footers.
- Aesthetic directions such as `quiet-saas`, `editorial-premium`, and `technical-product`.
- Style packs that describe tokens, component intent, states, responsive behavior, accessibility behavior, and quality gates.
- Placeholder-based HTML compilation with Python standard-library scripts.
- Validation scripts that check whether a website style pack is detailed enough before compilation.
- Sample generated website preview in `dist/editorial-premium-website.html`.

## Install

Clone or copy this folder into your Codex skills directory:

```bash
git clone https://github.com/YOUR_NAME/website-ui-design-skill.git
mkdir -p ~/.codex/skills
cp -R website-ui-design-skill ~/.codex/skills/website-ui-design
```

On Windows PowerShell:

```powershell
git clone https://github.com/YOUR_NAME/website-ui-design-skill.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force website-ui-design-skill "$env:USERPROFILE\.codex\skills\website-ui-design"
```

After installation, ask Codex to use the skill:

```text
Use $website-ui-design to design a landing page for an AI writing product.
```

## Quick Start

Build the bundled sample website:

```bash
python scripts/build_samples.py
```

Open the generated file:

```text
dist/editorial-premium-website.html
```

Or serve the folder locally:

```bash
python -m http.server 8123
```

Then visit:

```text
http://127.0.0.1:8123/dist/editorial-premium-website.html
```

## How It Works

1. **Infer intent**
   - Product type
   - Audience
   - Website goal
   - Content shape
   - Brand tone
   - Conversion goal
   - Constraints

2. **Select templates**
   - Page template from `templates/pages/`
   - Section templates from `templates/website-sections/`
   - Component recipes from `templates/component-recipes/`

3. **Choose aesthetic direction**
   - `quiet-saas` for calm B2B/product websites
   - `editorial-premium` for brand-forward launches and portfolios
   - `technical-product` for APIs, AI tools, infrastructure, open-source, and developer-facing websites

4. **Generate a style pack**
   - Global tokens
   - Section/component decisions
   - Interaction states
   - Responsive behavior
   - Accessibility behavior
   - Quality gates

5. **Compile HTML**
   - `scripts/compile_style_pack.py` replaces placeholders in HTML templates with values from the style pack.

## Validate a Website Style Pack

```bash
python scripts/validate_website_style_pack.py \
  --style-pack assets/website-style-packs/editorial-premium.website.json \
  --strict-optional
```

The validator checks that core website components include enough detail:

- role
- style intent
- anatomy
- at least four states
- responsive behavior
- accessibility behavior
- exceed-expectations detail

## Compile a Website

```bash
python scripts/compile_style_pack.py \
  --style-pack assets/website-style-packs/editorial-premium.website.json \
  --template assets/html-template/website-page.html \
  --out dist/editorial-premium-website.html
```

## Create a New Style Pack

Create a new file in `assets/website-style-packs/`, for example:

```text
assets/website-style-packs/my-product.website.json
```

Use the sample pack as a starting point:

```text
assets/website-style-packs/editorial-premium.website.json
```

Then update:

- `meta`: name, audience, density, memory point
- `tokens`: color, typography, spacing, radius, shadow, motion, size
- `components`: site header, hero, button, feature, proof, testimonial, pricing, FAQ, CTA, footer, card, form
- `quality_gates`: checks that the generated website must satisfy

## Extend Templates

Add new page types in:

```text
templates/pages/
```

Add new website sections in:

```text
templates/website-sections/
```

Add new component recipes in:

```text
templates/component-recipes/
```

Add new aesthetic directions in:

```text
templates/aesthetic-directions/
```

After adding a template, register it in the matching `index.yaml`.

## Design Philosophy

Most AI-generated websites fail because they lock into generic visual habits too early: oversized heroes, vague cards, decorative gradients, fake proof, and repeated sections that all look the same.

This skill separates the design process into decisions:

- What kind of website is this?
- What does the visitor need to understand first?
- What should the page be remembered for?
- What proof is credible?
- What does each section do?
- How should each component behave under the chosen style?

Templates provide structure. Style packs provide design judgment. The compiler makes the result repeatable.

## Repository Structure

```text
SKILL.md                         # Codex skill instructions
agents/openai.yaml               # Skill display metadata
assets/html-template/            # Placeholder HTML templates
assets/website-style-packs/      # Sample website style packs
dist/                            # Generated sample outputs
references/                      # Design workflow references
schemas/                         # Style pack schema
scripts/                         # Validators and compiler
templates/                       # Page, section, component, and style templates
```

## License

MIT
