## 2026-04-14 - Performance Baseline and Bottlenecks
**Learning:** Initial profiling of the Poker Debt Settler application revealed two primary performance bottlenecks:
1. **Lack of Compression:** The Flask server does not use Gzip or any other compression for text-based responses. The index page alone is ~17KB, which could be significantly reduced.
2. **Heavy Image Assets:** The `static/` directory contains 13 chip images totaling ~5.2MB. These high-resolution JPEGs are loaded synchronously and contribute to a high Page Weight.

**Action:** Implement manual Gzip compression for text/JSON responses in Flask and add `loading="lazy"` and `decoding="async"` attributes to images to improve perceived performance.
