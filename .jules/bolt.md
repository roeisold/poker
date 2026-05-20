## 2026-05-20 - Image Optimization and Asset Weight Reduction
**Learning:** High-resolution JPG chip images (1000x1000) were being loaded even when displayed as small icons (22px-50px), leading to a ~5.2MB initial payload. Converting to WebP and resizing to 200x200 significantly reduces asset weight without visible quality loss for the intended use case.
**Action:** Always check the resolution and format of static image assets when auditing for initial load performance; prioritize WebP and appropriate scaling.

## 2026-05-20 - Backend Loop Optimization
**Learning:** Dictionary lookups for nested data (e.g., `data.get('buy_ins', {})`) inside a loop over players can be optimized by pre-fetching the nested dictionary once. While the impact is minor for small player counts, it improves code efficiency and follows best practices.
**Action:** Pre-fetch request data outside of processing loops to minimize redundant lookups.
