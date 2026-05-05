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

## 2025-05-16 - [Optimized Chip Image Assets]
**Learning:** Serving 1000x1000 JPEGs (totaling 5.2MB) for icons displayed at < 50px is a massive performance anti-pattern. Resizing to 200x200 and using WebP provides a 98% reduction in payload size without visible quality loss at display scale.
**Action:** Always verify asset dimensions vs. display size and prefer modern formats like WebP/AVIF for photographic assets.

**Performance Impact:**
- **What:** Resized 13 chip images to 200x200 and converted them from JPEG to WebP format.
- **Why:** The original assets were over-optimized for quality (1000x1000px) but used in contexts where they are never larger than 50px.
- **Measurement:**
    - Original `static/` size: ~5.2MB (13 JPEGs).
    - New `static/` size: ~104KB (13 WebPs).
    - Payload reduction: ~98%.
    - Result: Significantly faster initial page load and reduced bandwidth usage for both server and client.
