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

## 2025-05-16 - [Optimize Poker Chip Assets]
**Learning:** The 13 poker chip images in `/static` were originally 1000x1000 JPEGs totaling ~5.2MB, which is overkill for 22px-50px display sizes. Resizing them to 100x100 and converting to WebP (quality 85) significantly reduces payload without visible quality loss.
**Action:** Always check asset dimensions vs display size and use modern formats like WebP for photographic elements.

**Performance Impact:**
- **What:** Optimized 13 poker chip images (resizing to 100x100 and converting to WebP).
- **Why:** Reduces initial page load payload by over 5.1MB.
- **Measurement:** Total asset weight reduced from 5.2MB to ~32KB (99.4% reduction).
