# Palette's Journal - Poker Debt Settler

## 2025-01-24 - Layout Robustness and Validation
**Learning:** Absolute positioning for interactive elements like removal buttons can create "dead zones" or "ghost click areas" that confuse users, especially on smaller screens or dynamic layouts. Using a dedicated grid column is more reliable.
**Action:** Always prefer grid or flexbox for alignment over absolute positioning for interactive elements.

## 2025-01-24 - Duplicate Data Prevention
**Learning:** Preventing duplicate names at the entry point is a simple but high-impact UX win that prevents downstream calculation errors and user confusion.
**Action:** Implement case-insensitive duplicate checks for list-based inputs.

## 2025-01-24 - Clipboard Feedback and Data Storage
**Learning:** Providing immediate visual feedback (like changing button text to "✓ Copied!") significantly improves user confidence in clipboard operations. Storing calculation results in a global variable makes formatting these results for the clipboard cleaner than scraping the DOM.
**Action:** Always provide state-based feedback for clipboard actions and maintain a clean data model for external sharing.
