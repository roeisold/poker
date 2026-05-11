## 2025-05-15 - [Browser Caching for Static Assets]
**Learning:** In Flask 2.3+, `SEND_FILE_MAX_AGE_DEFAULT` is deprecated. Using an `@app.after_request` handler is the recommended way to set `Cache-Control` headers for static files when they are served by Flask.
**Action:** Always use `@app.after_request` for explicit cache control in modern Flask apps.

**Performance Impact:**
- **What:** Added `Cache-Control: public, max-age=31536000` to all files in `/static`.
- **Why:** The application serves ~5.2MB of chip images. Without caching, these are re-downloaded on every page load (or validated with 304s if ETag is present, which still takes round-trips).
- **Measurement:**
    - Initial load: ~5.2MB transferred.
    - Subsequent loads: 0MB transferred (loaded from disk/memory cache).
    - Reduces load time for returning visitors from seconds (depending on connection) to near-instant for images.

## 2026-05-11 - [Image Asset Optimization]
**Learning:** Serving high-resolution (1000x1000) source images for small UI icons (22px-50px) is a significant performance bottleneck. WebP provides superior compression over JPG for these assets.
**Action:** Always resize source images to their maximum intended display size and use WebP format with ~85% quality for a balance of speed and visual fidelity.

**Performance Impact:**
- **What:** Optimized 13 chip images by resizing to 200x200 and converting to WebP.
- **Why:** Reduced total static asset size from 5.2MB to 104KB.
- **Measurement:**
    - Size reduction: ~98%.
    - Load time: Significant reduction in initial page load time and bandwidth usage.
