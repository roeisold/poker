## 2026-04-16 - Flask Gzip Compression
**Learning:** Manual Gzip compression in Flask's `after_request` handler is an effective way to reduce payload sizes (73% reduction for HTML in this app). Using `request.accept_encodings` is more robust than manual header parsing. Always ensure `Vary: Accept-Encoding` is set and `direct_passthrough` is respected.
**Action:** When optimizing Flask apps, check if Gzip is already handled by the proxy (like Nginx). if not, implement it in `after_request` but only for payloads > 500 bytes and text-based mime types.
