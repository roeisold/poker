# Palette's Journal - Poker Debt Settler

## 2025-01-24 - Layout Robustness and Validation
**Learning:** Absolute positioning for interactive elements like removal buttons can create "dead zones" or "ghost click areas" that confuse users, especially on smaller screens or dynamic layouts. Using a dedicated grid column is more reliable.
**Action:** Always prefer grid or flexbox for alignment over absolute positioning for interactive elements.

## 2025-01-24 - Duplicate Data Prevention
**Learning:** Preventing duplicate names at the entry point is a simple but high-impact UX win that prevents downstream calculation errors and user confusion.
**Action:** Implement case-insensitive duplicate checks for list-based inputs.

## 2025-01-24 - State Cleanup on Data Reset
**Learning:** When clearing application data, ensure any global JavaScript state used for features like "Copy Settlement Plan" is explicitly reset. Failing to do so can lead to users copying stale, incorrect data from a previous session after they thought they had started fresh.
**Action:** Always include global state variables in data-clearing logic.
