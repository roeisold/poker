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

## 2025-05-17 - [Image Optimization and WebP Conversion]
**Learning:** High-resolution JPG images (1000x1000) used for small UI icons (22px-50px) create a massive performance bottleneck. Resizing to a reasonable size (200x200) and converting to WebP format provides significant bandwidth savings without visible quality loss.
**Action:** Always audit image assets for size vs. display resolution and prefer WebP for web assets.

**Performance Impact:**
- **What:** Optimized 13 chip images from 1000x1000 JPGs to 200x200 WebP (85% quality). Added `loading="lazy"` to templates.
- **Why:** The original 5.2MB payload for simple icons was excessive and slowed down the first-paint and total load time.
- **Measurement:**
    - Combined asset size: 5.2MB -> 70KB (~98.7% reduction).
    - Drastically reduces initial load time and data consumption for all users.
