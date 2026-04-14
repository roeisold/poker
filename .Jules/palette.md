# Palette's Journal - Poker Debt Settler

## 2025-01-24 - Layout Robustness and Validation
**Learning:** Absolute positioning for interactive elements like removal buttons can create "dead zones" or "ghost click areas" that confuse users, especially on smaller screens or dynamic layouts. Using a dedicated grid column is more reliable.
**Action:** Always prefer grid or flexbox for alignment over absolute positioning for interactive elements.

## 2025-01-24 - Duplicate Data Prevention
**Learning:** Preventing duplicate names at the entry point is a simple but high-impact UX win that prevents downstream calculation errors and user confusion.
**Action:** Implement case-insensitive duplicate checks for list-based inputs.

## 2026-04-14 - Clipboard Feedback Pattern
**Learning:** For "Copy to Clipboard" features, providing immediate visual feedback by changing the button text and style (e.g., to a "✓ Copied!" state) significantly improves user confidence. Also, disabling the copy button until data is available prevents empty clipboard operations.
**Action:** Use a temporary "✓ Copied!" state with  and toggle button classes for clear success feedback. Ensure the button state reflects the availability of data.

## 2026-04-14 - Clipboard Feedback Pattern
**Learning:** For "Copy to Clipboard" features, providing immediate visual feedback by changing the button text and style (e.g., to a "✓ Copied!" state) significantly improves user confidence. Also, disabling the copy button until data is available prevents empty clipboard operations.
**Action:** Use a temporary "✓ Copied!" state with setTimeout and toggle button classes for clear success feedback. Ensure the button state reflects the availability of data.
