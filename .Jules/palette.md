# Palette's Journal - Poker Debt Settler

## 2025-01-24 - Layout Robustness and Validation
**Learning:** Absolute positioning for interactive elements like removal buttons can create "dead zones" or "ghost click areas" that confuse users, especially on smaller screens or dynamic layouts. Using a dedicated grid column is more reliable.
**Action:** Always prefer grid or flexbox for alignment over absolute positioning for interactive elements.

## 2025-01-24 - Duplicate Data Prevention
**Learning:** Preventing duplicate names at the entry point is a simple but high-impact UX win that prevents downstream calculation errors and user confusion.
**Action:** Implement case-insensitive duplicate checks for list-based inputs.

## 2026-05-08 - Visual Feedback for Clipboard Actions
**Learning:** Providing immediate, non-disruptive visual confirmation (e.g., toggling button text to "✓ Copied!" and changing the button style) significantly improves the perceived reliability of clipboard operations.
**Action:** Use temporary state changes (2s timeout) to confirm successful background actions.

## 2026-05-08 - Accessibility for Minimalist UI
**Learning:** In minimalist designs where visual labels are omitted (like player rows), `aria-label` and `title` attributes are essential for screen reader compatibility and desktop discoverability.
**Action:** Always include descriptive ARIA labels for inputs and titles for action buttons in dense, low-label interfaces.
