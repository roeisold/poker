## 2026-05-14 - Asset Weight Optimization
**Learning:** High-resolution (1000x1000) source images used for small UI icons (22px-50px) created a significant performance bottleneck (~5.2MB total). Converting these to 200x200 WebP format with `quality=85` and `LANCZOS` resampling achieved a ~98% reduction in asset size (~104KB total) with no visible quality loss.
**Action:** Always audit static assets for over-dimensioned images and prefer modern formats like WebP for web delivery.
