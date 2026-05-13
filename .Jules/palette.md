# Palette's Journal - Poker Debt Settler

## 2025-01-24 - Layout Robustness and Validation
**Learning:** Absolute positioning for interactive elements like removal buttons can create "dead zones" or "ghost click areas" that confuse users, especially on smaller screens or dynamic layouts. Using a dedicated grid column is more reliable.
**Action:** Always prefer grid or flexbox for alignment over absolute positioning for interactive elements.

## 2025-01-24 - Duplicate Data Prevention
**Learning:** Preventing duplicate names at the entry point is a simple but high-impact UX win that prevents downstream calculation errors and user confusion.
**Action:** Implement case-insensitive duplicate checks for list-based inputs.

## 2025-05-13 - Instant Feedback for Utility Actions
**Learning:** For simple utility actions like "Copy to Clipboard", providing immediate visual feedback by changing the button's internal state (text and color) is more effective and less disruptive than using external notifications like toasts or alerts.
**Action:** Use temporary button state changes (e.g., "📋 Copy" -> "✓ Copied!") for quick confirmation of success.
