# Bolt's Performance Journal

## 2026-04-12 - Gzip Compression Implementation
**Learning:** Manual Gzip compression in Flask requires careful handling of `direct_passthrough` responses (like static files) because reading the response iterator exhausts it. The `Vary: Accept-Encoding` header is also critical for correct caching.
**Action:** Implement a robust `@app.after_request` handler that checks `Accept-Encoding`, avoids double compression, and correctly restores the response iterator when necessary.
