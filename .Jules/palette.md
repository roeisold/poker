# Palette's Journal - Poker Debt Settler

## 2025-01-24 - Layout Robustness and Validation
**Learning:** Absolute positioning for interactive elements like removal buttons can create "dead zones" or "ghost click areas" that confuse users, especially on smaller screens or dynamic layouts. Using a dedicated grid column is more reliable.
**Action:** Always prefer grid or flexbox for alignment over absolute positioning for interactive elements.

## 2025-01-24 - Duplicate Data Prevention
**Learning:** Preventing duplicate names at the entry point is a simple but high-impact UX win that prevents downstream calculation errors and user confusion.
**Action:** Implement case-insensitive duplicate checks for list-based inputs.

## 2025-05-22 - Immediate Feedback for Clipboard Actions
**Learning:** When users perform a "Copy to Clipboard" action, a transient visual change (like changing button text to "✓ Copied!") provides essential confirmation that the invisible action succeeded, reducing uncertainty.
**Action:** Always include a success state/feedback loop for clipboard operations.
