# Palette's Journal - Poker Debt Settler

## 2025-01-24 - Layout Robustness and Validation
**Learning:** Absolute positioning for interactive elements like removal buttons can create "dead zones" or "ghost click areas" that confuse users, especially on smaller screens or dynamic layouts. Using a dedicated grid column is more reliable.
**Action:** Always prefer grid or flexbox for alignment over absolute positioning for interactive elements.

## 2025-01-24 - Duplicate Data Prevention
**Learning:** Preventing duplicate names at the entry point is a simple but high-impact UX win that prevents downstream calculation errors and user confusion.
**Action:** Implement case-insensitive duplicate checks for list-based inputs.

## 2026-05-03 - Robust Sanitization and Sharing
**Learning:** `escapeHTML` implementations using logical OR (`||`) for defaults can accidentally suppress numeric `0`. Using nullish coalescing (`??`) ensures all valid data is rendered. Additionally, storing raw calculation results in a global variable (`window.lastCalculationData`) simplifies implementing sharing features like "Copy to Clipboard" by avoiding fragile DOM scraping.
**Action:** Use `??` for default values in template helpers and cache backend responses for secondary UI actions.
