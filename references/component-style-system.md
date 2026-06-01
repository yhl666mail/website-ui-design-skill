# Component Style System

Component recipes describe how a component should respond to a chosen aesthetic
direction. They are not fixed CSS snippets.

## Component Formula

```text
component style =
  functional role
  + required anatomy
  + required states
  + token usage
  + aesthetic-direction behavior
  + responsive behavior
  + accessibility behavior
  + product-specific detail
```

## What To Refine

For every important component, decide:

- **Shape**: radius, border, corners, grouping, hit area
- **Surface**: fill, border, shadow, texture, contrast
- **Typography**: size, weight, casing, numeric treatment, monospace use
- **Spacing**: padding, internal rhythm, relationship to neighboring elements
- **State**: default, hover, focus, active, selected, disabled, loading, error
- **Motion**: transition duration, easing, whether motion is allowed
- **Density**: compact, standard, spacious, dramatic
- **Responsiveness**: collapse, stack, scroll, pin, or transform
- **Delight detail**: one contextual detail that makes the component memorable

## State Quality

States should communicate meaning, not just decoration.

- Hover: previews clickability or section/card affordance.
- Focus: keyboard-visible and high contrast.
- Active: confirms press or selected mode.
- Selected: durable and distinguishable from hover.
- Disabled: explains why when the action is important.
- Loading: preserves layout and sets expectation.
- Error: identifies the issue and next recovery step.
- Empty: explains absence and offers a next action.

## Style Behavior Rules

Do not map directions to fixed colors. Map them to behavior.

Example:

```yaml
quiet-saas:
  surface: "border-first, low shadow, high readability"
  motion: "subtle feedback only"
technical-product:
  surface: "dark panels, crisp dividers, metadata-friendly density"
  motion: "fast state changes, no decorative drift"
editorial-premium:
  surface: "strong composition, fewer panels, deliberate contrast"
  motion: "one memorable reveal or hover treatment"
```

## Exceeding Expectations

Add at least one of these when appropriate:

- contextual microcopy based on the user's domain
- status language that reflects real decisions
- a memorable but restrained interaction
- a layout metaphor tied to the product
- a component state that typical demos omit
- a responsive transformation that feels intentional

Avoid adding complexity that does not support the user's task.

## Detail Depth

A component style is not detailed enough if it only names color, radius, and
padding. It is detailed enough when another agent can implement the component
without asking:

- what parts it contains
- how it behaves in at least four states
- how it changes on mobile
- how it remains accessible
- how it expresses the chosen aesthetic direction
- what product-specific detail makes it feel intentional

When the component is central to the UI, include the exact content device that
will make it exceed expectations. Examples:

- A proof card includes source, timeframe, segment, or result context.
- A button exposes a useful transient state like `Preparing preview`, `Copied`, `Submitting`, or `Request received`.
- A pricing card includes fit cues and tradeoff language.
- A testimonial includes role context and a before/after result.
- A form includes response time, privacy note, or next-step expectation.

