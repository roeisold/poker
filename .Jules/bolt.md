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

## 2026-04-09 - [Manual Gzip Compression]
**Learning:** Manual Gzip compression via `@app.after_request` is a viable way to reduce payload sizes for text-based responses (HTML, JSON, JS, CSS) in Flask when a reverse proxy or specialized middleware isn't available. Setting the `Vary: Accept-Encoding` header is critical for ensuring downstream caches correctly handle compressed vs. uncompressed versions.
**Action:** Implement Gzip compression for all non-binary, non-streaming responses to save bandwidth and improve load times.

**Performance Impact:**
- **What:** Added manual Gzip compression for text/html, application/json, text/css, and application/javascript responses.
- **Why:** Reduces the transfer size of main pages and calculation results, speeding up initial page loads and interactions, especially on slower connections.
- **Measurement:**
    - Initial HTML payload (uncompressed): ~15KB
    - Initial HTML payload (gzipped): ~4.5KB
    - Reduction: ~70% for text-based responses.
