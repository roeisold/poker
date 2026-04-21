## 2026-04-21 - [Image Asset Optimization]
**Learning:** High-resolution assets (1000x1000 JPEGs) were being served for small UI icons (22x22 and 50x50), leading to a ~5.3MB payload for a simple calculator.
**Action:** Always audit asset dimensions against their display size. Resizing to 100x100 and converting to WebP reduced the payload by over 99% (to ~26KB) without visible quality loss.
