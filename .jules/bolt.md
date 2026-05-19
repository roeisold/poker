## 2026-05-19 - Image Optimization Impact
**Learning:** Optimizing large (1000x1000) JPEG assets by converting them to 200x200 WebP with 85% quality achieved a ~98.6% reduction in asset weight (~5.2MB to ~70KB). Using `LANCZOS` resampling ensures high visual quality even at smaller dimensions.
**Action:** Always check static assets for resizing opportunities, especially when they are displayed at much smaller sizes than their source resolution. Implement `loading="lazy"` on all non-critical images to improve Largest Contentful Paint (LCP).
