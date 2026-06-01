# Template Selection Rubric

Use this rubric before generating UI. The goal is to select templates from
product intent, not from superficial style words.

## UIIntent Schema

Infer or ask for missing values only when the uncertainty would change the
template family.

```yaml
product_type: ""
audience: ""
  website_goal: ""
secondary_tasks: []
content_density: "low | medium | high"
content_shape: "marketing | product | editorial | portfolio | ecommerce | event | mixed"
interaction_depth: "static | light | conversion | content-rich"
platform: "desktop | mobile | responsive | kiosk | email"
brand_tone: "quiet | premium | technical | playful | warm | institutional | experimental"
conversion_goal: ""
constraints: []
existing_system: ""
```

## Page Template Scoring

Score candidate page templates from 0 to 5.

| Factor | Weight | Meaning |
|---|---:|---|
| Intent fit | 40 | Does the page structure match the primary task? |
| Audience fit | 20 | Does the density and language fit the users? |
| Content fit | 20 | Does it support the available content and data shape? |
| Interaction fit | 10 | Does it support required controls and states? |
| Visual fit | 10 | Does it match brand tone without hurting usability? |

Select the highest score. If two are close, choose the simpler page template and
add block templates for missing needs.

## Page Selection Hints

- Use `landing-page` when the goal is explaining, positioning, converting, or launching.
- Use website sections for brand sites, product pages, portfolios, campaigns, and editorial pages.
- Use app/dashboard templates only when the user explicitly asks for an app or internal tool.

Avoid landing-page structure for operational tools. Avoid dashboard structure
for emotional brand introductions with little data.

## Block Selection Hints

Blocks are composable. Pick only blocks that serve the primary task.

- Use `site-header` for brand, navigation, and primary visitor action.
- Use `website-hero` for first-viewport orientation and conversion.
- Use `feature-section` for outcome explanation.
- Use `proof-section` for credibility, source, logos, metrics, or proof.
- Use `testimonial-section` for human proof.
- Use `pricing-section` for plan comparison and conversion.
- Use `faq-section` for objection handling.
- Use `cta-section` for focused next step.
- Use `site-footer` for trust, links, contact, and closure.

## Aesthetic Direction Selection

Choose one aesthetic direction template and apply it consistently. Read
`templates/aesthetic-directions/index.yaml`, then the selected direction.

- Use `quiet-saas` for professional B2B websites and product landing pages.
- Use `editorial-premium` for launches, portfolios, campaigns, and brand-led pages.
- Use `technical-product` only for public websites selling technical tools, APIs, AI/dev products, or open-source projects.

Do not mix styles unless the page explicitly needs separate product surfaces.

After selection, define a memory point. The memory point is the design idea that
prevents template sameness. It may be a layout metaphor, interaction detail,
content device, or product-specific visual system.

Examples:

- "A compact triage cockpit with status lanes."
- "A product launch page that feels like an annotated field guide."
- "A mobile finance screen organized around tomorrow's cash position."

## Component Recipe Selection

After selecting blocks, read `templates/component-recipes/index.yaml` and load
recipes for components that will materially affect the page.

Minimum recipes by website type:

- `landing-page`: site-header, hero, button, feature-section, proof-strip, pricing-card, faq, cta-band, site-footer
- `brand-site`: site-header, hero, feature-section, proof-strip, testimonial, cta-band, site-footer
- `portfolio`: site-header, hero, feature-section, proof-strip, testimonial, cta-band, site-footer
- `technical-product-site`: site-header, hero, feature-section, proof-strip, pricing-card, faq, cta-band, site-footer

Use component recipes to derive component-specific styles from the selected
aesthetic direction. Do not use them as fixed CSS snippets.

## Tie Breakers

- Prefer task clarity over novelty.
- Prefer real content density over decorative emptiness.
- Prefer fewer sections with stronger hierarchy over many weak sections.
- Prefer stable, readable layouts over viewport-driven typography tricks.
- Prefer established component behavior over custom interaction for common controls.

