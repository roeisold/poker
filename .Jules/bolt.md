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

## 2026-04-10 - [Gzip Compression & Image Optimization]
**Learning:** Manual response compression in Flask requires careful handling of `direct_passthrough` responses (like static files) to avoid empty responses when compression is skipped. Setting `Vary: Accept-Encoding` is critical for CDN/cache compatibility.
**Action:** Use a robust `@app.after_request` handler for compression and always set `Vary`.

**Performance Impact:**
- **What:** Implemented manual Gzip compression for HTML, JSON, CSS, and JS. Added `loading="lazy"` and `decoding="async"` to chip images.
- **Why:** HTML payload was ~17KB, now ~4.6KB (~73% reduction). Large 1000x1000 chip images were blocking the main thread during decoding; `decoding="async"` offloads this.
- **Measurement:**
    - HTML Size: 17150 bytes -> 4677 bytes (Gzipped).
    - Perceived performance: Improved by lazy loading images and async decoding.
