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

## 2026-05-02 - [Optimizing UI Assets with WebP]
**Learning:** High-resolution JPEGs (1000x1000) were used for small UI elements (rendered at 22px-50px), resulting in a ~5.2MB payload for simple icons. Resizing to 100x100 and converting to WebP (quality 85) achieved a ~99% size reduction with no perceptible loss in quality at display scale.
**Action:** Audit static assets for resolution-to-display-size mismatches and prefer WebP for all UI icons.
