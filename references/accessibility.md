# Accessibility Checks

Use these checks for every production-like HTML artifact.

## Structure

- Use one `h1` for the page or screen title.
- Preserve heading order.
- Use `header`, `nav`, `main`, `section`, `aside`, and `footer` when meaningful.
- Use buttons for actions and links for navigation.

## Controls

- Every input needs a visible label or an accessible label.
- Group related fields with `fieldset` and `legend` when useful.
- Provide clear validation and error text.
- Keep touch targets at least 44px where practical.
- Provide visible focus styles.

## Color And Contrast

- Do not rely on color alone for status.
- Pair status color with text or icon labels.
- Keep text contrast readable on all backgrounds.
- Avoid placing long text over busy imagery.

## Motion

- Keep animation subtle and purposeful.
- Respect `prefers-reduced-motion`.
- Do not animate layout in ways that hide controls or text.

## Responsive Behavior

- Check at mobile and desktop widths.
- Ensure horizontal scrolling is intentional only for data tables or code.
- Keep nav, filters, and primary actions reachable on mobile.
- Avoid viewport-scaled font sizes.
