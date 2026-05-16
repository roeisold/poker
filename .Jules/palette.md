# Palette's Journal - Poker Debt Settler

## 2025-01-24 - Layout Robustness and Validation
**Learning:** Absolute positioning for interactive elements like removal buttons can create "dead zones" or "ghost click areas" that confuse users, especially on smaller screens or dynamic layouts. Using a dedicated grid column is more reliable.
**Action:** Always prefer grid or flexbox for alignment over absolute positioning for interactive elements.

## 2025-01-24 - Duplicate Data Prevention
**Learning:** Preventing duplicate names at the entry point is a simple but high-impact UX win that prevents downstream calculation errors and user confusion.
**Action:** Implement case-insensitive duplicate checks for list-based inputs.

## 2026-05-16 - Redundant Accessibility Attributes
**Learning:** Adding `aria-label` to elements that already have clear, visible text (like "Save Settings") is redundant for screen readers as they will read both or prioritize the label, potentially creating a repetitive experience. However, for icon-only buttons or ambiguous symbols (like "×"), `aria-label` and `title` are essential.
**Action:** Only add `aria-label` when the visible text is insufficient or non-existent (e.g., icons).
