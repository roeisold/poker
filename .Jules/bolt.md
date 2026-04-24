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

## 2026-04-24 - [Image Payload Reduction with WebP and Resizing]
**Learning:** High-resolution JPGs (1000x1000) are excessive for small UI icons (22x22 and 50x50). Resizing to 100x100 and converting to WebP provides a massive payload reduction without perceptible quality loss.
**Action:** Always audit asset dimensions against their display size and use modern formats like WebP for photographic content.

**Performance Impact:**
- **What:** Resized 13 chip images from 1000x1000 to 100x100 and converted from JPG to WebP.
- **Why:** The total image payload was ~5.2MB, which is extremely heavy for a simple calculator utility.
- **Measurement:**
    - Total static assets size reduced from 5.2MB to 56KB (99% reduction).
    - Significantly improves First Contentful Paint (FCP) and total load time on slow connections.
