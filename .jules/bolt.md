## 2026-04-19 - Manual Gzip Compression
**Learning:** The application serves relatively large HTML (17KB) and JSON responses without any compression, increasing bandwidth usage and load times for users on slower connections. Flask doesn't enable Gzip compression by default.
**Action:** Implement manual Gzip compression in the `@app.after_request` handler for text-based responses when supported by the client.
