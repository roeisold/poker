# Palette's Journal - Poker Debt Settler

## 2025-01-24 - Layout Robustness and Validation
**Learning:** Absolute positioning for interactive elements like removal buttons can create "dead zones" or "ghost click areas" that confuse users, especially on smaller screens or dynamic layouts. Using a dedicated grid column is more reliable.
**Action:** Always prefer grid or flexbox for alignment over absolute positioning for interactive elements.

## 2025-01-24 - Duplicate Data Prevention
**Learning:** Preventing duplicate names at the entry point is a simple but high-impact UX win that prevents downstream calculation errors and user confusion.
**Action:** Implement case-insensitive duplicate checks for list-based inputs.

## 2025-01-24 - Contextual Accessibility for Inputs
**Learning:** For numeric inputs representing counts of specific items (like poker chips), adding the item's monetary value to the `aria-label` and `title` provides crucial context for screen reader users and helps all users verify they are entering data in the correct field.
**Action:** Enhance item-based numeric inputs with descriptive labels that include their specific value or unit.
