# Anti-AI-Slop Checklist

Check this before finalizing any UI artifact.

## Visual Failures

Fix these when present:

- excessive gradients, glow effects, glassmorphism, or blur
- decorative blobs, floating orbs, or background noise
- every section styled as a card
- cards nested inside cards without functional reason
- giant hero sections for operational tools
- vague headings like "Unlock your potential" without product substance
- identical repeated cards with weak hierarchy
- random icon choices that do not clarify meaning
- over-rounded controls that make dense UI feel toy-like
- one-note palettes dominated by a single hue
- fake charts or metrics without labels, units, or plausible values
- text that overflows, overlaps, or becomes too small on mobile

## Structural Failures

Fix these when present:

- no clear primary task
- no first-viewport signal of the product or workflow
- missing navigation for app-like screens
- tables without filters, status, or row actions
- forms without labels, validation, or save/cancel behavior
- empty states that do not tell users how to proceed
- proof or metric bands with numbers but no source, context, or next action
- landing pages with many claims but no concrete proof

## Copy Failures

Replace generic copy with concrete domain language.

Bad:

- "Streamline your workflow"
- "Powerful insights"
- "Seamless collaboration"

Better:

- "Review overdue invoices before the 4 PM payment run"
- "Spot stores with inventory below the reorder threshold"
- "Compare model eval failures by dataset, owner, and release"

## Final Gate

The UI should answer:

- What is this?
- Who is it for?
- What should the user do first?
- What information matters most?
- What happens when data is loading, empty, invalid, or failed?
