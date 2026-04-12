# Palette's Journal - Poker Debt Settler

## 2025-01-24 - Layout Robustness and Validation
**Learning:** Absolute positioning for interactive elements like removal buttons can create "dead zones" or "ghost click areas" that confuse users, especially on smaller screens or dynamic layouts. Using a dedicated grid column is more reliable.
**Action:** Always prefer grid or flexbox for alignment over absolute positioning for interactive elements.

## 2025-01-24 - Duplicate Data Prevention
**Learning:** Preventing duplicate names at the entry point is a simple but high-impact UX win that prevents downstream calculation errors and user confusion.
**Action:** Implement case-insensitive duplicate checks for list-based inputs.

## 2025-01-24 - Input Flow Efficiency
**Learning:** For dynamic lists (like adding players), automatically focusing the first input field of the new entry significantly reduces friction and speeds up data entry.
**Action:** Always auto-focus primary inputs on dynamically added form elements.

## 2025-01-24 - Contextual Accessibility
**Learning:** ARIA labels for numeric inputs should include the units or context (e.g., monetary value of a chip) if the visual context is purely graphical.
**Action:** Enhance numeric input labels with their specific meaning or unit value (e.g., "(value: 0.25)").
