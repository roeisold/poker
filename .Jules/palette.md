# Palette's Journal - Poker Debt Settler

## 2025-01-24 - Layout Robustness and Validation
**Learning:** Absolute positioning for interactive elements like removal buttons can create "dead zones" or "ghost click areas" that confuse users, especially on smaller screens or dynamic layouts. Using a dedicated grid column is more reliable.
**Action:** Always prefer grid or flexbox for alignment over absolute positioning for interactive elements.

## 2025-01-24 - Duplicate Data Prevention
**Learning:** Preventing duplicate names at the entry point is a simple but high-impact UX win that prevents downstream calculation errors and user confusion.
**Action:** Implement case-insensitive duplicate checks for list-based inputs.

## 2026-04-19 - Accessibility-Rich Dynamic Labels
**Learning:** For inputs representing categories with dynamic values (like poker chips with configurable amounts), including the current value directly in the `aria-label` (e.g., "Green chip ($1.00) count") significantly improves clarity for screen reader users compared to static labels.
**Action:** Always include key dynamic attributes in accessibility labels for repetitive form elements.
