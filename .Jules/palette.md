# Palette's Journal - Poker Debt Settler

## 2025-01-24 - Layout Robustness and Validation
**Learning:** Absolute positioning for interactive elements like removal buttons can create "dead zones" or "ghost click areas" that confuse users, especially on smaller screens or dynamic layouts. Using a dedicated grid column is more reliable.
**Action:** Always prefer grid or flexbox for alignment over absolute positioning for interactive elements.

## 2025-01-24 - Duplicate Data Prevention
**Learning:** Preventing duplicate names at the entry point is a simple but high-impact UX win that prevents downstream calculation errors and user confusion.
**Action:** Implement case-insensitive duplicate checks for list-based inputs.

## 2025-05-15 - Clipboard Feedback and State Management
**Learning:** Toggling button classes (e.g., from `btn-outline-success` to `btn-success`) alongside text changes provides effective, non-disruptive visual confirmation for clipboard operations. Also, when clearing application data, ensure any global JavaScript state used for features like 'Copy Settlement Plan' is explicitly reset to prevent stale data from being shared.
**Action:** Use temporary class and text changes for action confirmation; explicitly nullify global state on data reset.
