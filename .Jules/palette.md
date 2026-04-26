# Palette's Journal - Poker Debt Settler

## 2025-01-24 - Layout Robustness and Validation
**Learning:** Absolute positioning for interactive elements like removal buttons can create "dead zones" or "ghost click areas" that confuse users, especially on smaller screens or dynamic layouts. Using a dedicated grid column is more reliable.
**Action:** Always prefer grid or flexbox for alignment over absolute positioning for interactive elements.

## 2025-01-24 - Duplicate Data Prevention
**Learning:** Preventing duplicate names at the entry point is a simple but high-impact UX win that prevents downstream calculation errors and user confusion.
**Action:** Implement case-insensitive duplicate checks for list-based inputs.

## 2025-01-24 - State Reset and Clipboard Safety
**Learning:** When adding features that rely on global JavaScript state (like a 'Copy Settlement' button), it's crucial to explicitly reset that state when the user clears data. Failing to do so can lead to users accidentally sharing stale or incorrect information from a previous session.
**Action:** Always ensure that any global application state is synchronized with data clearing operations.
