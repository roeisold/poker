# Palette's Journal - Poker Debt Settler

## 2025-01-24 - Layout Robustness and Validation
**Learning:** Absolute positioning for interactive elements like removal buttons can create "dead zones" or "ghost click areas" that confuse users, especially on smaller screens or dynamic layouts. Using a dedicated grid column is more reliable.
**Action:** Always prefer grid or flexbox for alignment over absolute positioning for interactive elements.

## 2025-01-24 - Duplicate Data Prevention
**Learning:** Preventing duplicate names at the entry point is a simple but high-impact UX win that prevents downstream calculation errors and user confusion.
**Action:** Implement case-insensitive duplicate checks for list-based inputs.

## 2025-01-24 - Interactive State Management
**Learning:** Interactive results actions like 'Copy Settlement Plan' should be hidden until calculation results are successfully populated to prevent user confusion or errors with empty state. Similarly, when clearing application data, any global JavaScript state must be explicitly reset to prevent stale data from being shared.
**Action:** Use conditional visibility (e.g., `display:none`) and explicit state resets in data clearing functions for interactive result features.
