# Expectation Lift Rubric

Use this after the style pack and component recipes are selected. The goal is
to make the result feel better than a competent template.

## The Lift Principle

Do not add surprise randomly. Add one or two details that make the UI feel
designed for the user's product, audience, and workflow.

Good expectation lift:

- reduces user uncertainty
- clarifies a decision
- exposes useful state
- makes the product's mental model memorable
- improves recovery from empty, failed, loading, or risky states

Bad expectation lift:

- decorative motion unrelated to the task
- extra chrome that reduces scanning
- visual novelty that breaks accessibility
- fake metrics or fake terminal text

## Required Lift Decisions

For every important UI, choose at least three:

1. **Decision cue**: Add a field, label, threshold, or next action that helps the user decide.
2. **State depth**: Include a state ordinary demos omit, such as dirty, queued, retrying, partial, stale, blocked, copied, or recovered.
3. **Product-specific content**: Replace generic copy with domain language, realistic entities, owners, dates, IDs, or limits.
4. **Memory point**: Make the chosen memory point visible in layout, content, or interaction.
5. **Safety detail**: Add preview, test, undo, dry run, confirmation, permission scope, or rollback when an action has risk.
6. **Responsive transformation**: Make mobile behavior intentional, not merely stacked.
7. **Inspection affordance**: Let users inspect why a status, score, or recommendation exists.

## Component Lift Examples

- Button: `Save` becomes `Test connection`, `Queue run`, `Promote to production`, or `Retry failed step`.
- Table: add `Risk`, `Owner`, `Queue age`, `Confidence`, `Next checkpoint`, or `Blocked by`.
- Metric: include time window, threshold, and implication: `p95 1.8s · investigate above 2s`.
- Form: include dry-run, preview, undo window, permission scope, or validation with expected format.
- Empty state: identify the missing source and provide the exact recovery action.
- Chat/tool call: show elapsed time, changed artifacts, failed tool, retry option, and inspection link.
- Navigation: expose workspace, environment, branch, model, queue count, or current mode.
- Hero: show the actual workflow or product state instead of decorative abstraction.

## Quality Gate

Before finalizing, answer:

- What detail could only belong to this product?
- What state would a real product need but a shallow demo would omit?
- What component now helps the user make a better decision?
- Where is the memory point visible?
- Did the lift improve usefulness without increasing noise?
