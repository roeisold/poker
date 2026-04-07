## 2026-04-07 - [Flask Security Enhancements]
**Vulnerability:** Debug mode was enabled, internal errors were leaked to the client, and security headers (including CSP) were missing.
**Learning:** Even simple utility apps can expose critical vulnerabilities like remote code execution if Flask's interactive debugger is left active in a production-like environment. Leaking `str(e)` in JSON responses can expose database schemas or internal file paths.
**Prevention:** Always disable `debug` mode by default or use environment variables, implement generic error messages for the client, and use `@app.after_request` to enforce security headers like CSP and X-Frame-Options.
