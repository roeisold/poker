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

## 2026-04-29 - [Image Optimization with WebP]
**Learning:** High-resolution JPEGs (1000x1000) are extremely wasteful when displayed at small sizes (22px-50px). Resizing to 100x100 and converting to WebP (quality 85) can reduce asset size by over 99% while maintaining perfect visual clarity at those display sizes.
**Action:** Always audit asset dimensions and formats. Favor WebP for web assets and ensure source dimensions are appropriate for their maximum intended display size.

**Performance Impact:**
- **What:** Resized 13 chip images from 1000x1000 to 100x100 and converted from JPG to WebP.
- **Why:** The original assets totaled ~5.8MB, which is a massive payload for a simple debt calculator.
- **Measurement:**
    - Total `static/` size reduced from ~5.8MB to 56KB (~99% reduction).
    - Drastically improves initial "Time to Interactive" and "Largest Contentful Paint" on slow connections.
