## 2026-04-08 - Flask Security Hardening
**Vulnerability:** Information leakage through raw exception messages and lack of Content Security Policy.
**Learning:** Returning `str(e)` in Flask JSON responses can expose internal application logic or stack traces to clients.
**Prevention:** Always use generic error messages for client-facing responses and implement CSP via `@app.after_request` to enforce resource loading policies.

## 2026-05-20 - Defense-in-Depth Headers
**Vulnerability:** Lack of standard security headers exposing the application to MIME-sniffing and clickjacking.
**Learning:** Even with a Content Security Policy, adding specific headers like `X-Content-Type-Options`, `X-Frame-Options`, and `Referrer-Policy` provides additional layers of protection that are recognized by all modern browsers.
**Prevention:** Standardize on a set of security headers for all Flask responses to ensure consistent protection across the application.
