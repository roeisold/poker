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

## 2026-05-03 - [Optimized Image Assets with WebP]
**Learning:** Converting high-resolution JPG assets (1000x1000) to downsized WebP format (200x200) provides a massive reduction in payload size without compromising visual quality for UI components like chip icons.
**Action:** Always audit static assets for oversized dimensions and non-optimized formats. Use WebP at quality 85 with Lanczos resampling for a balance of speed and fidelity.
