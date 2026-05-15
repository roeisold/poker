# Bolt Journal - Performance Optimizations

## 2025-05-15 - Image Asset Optimization
**Learning:** Serving high-resolution (1000x1000) source images for small UI icons (22px-50px) created a significant performance bottleneck, increasing initial page load weight by over 5MB.
**Action:** Always audit static assets for appropriate sizing relative to their UI usage. Convert heavy formats like JPG/PNG to WebP and resize to the minimum necessary dimensions (e.g., 200x200 for icons) to minimize bandwidth and improve LCP.
