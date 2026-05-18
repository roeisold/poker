## 2026-04-08 - Flask Security Hardening
**Vulnerability:** Information leakage through raw exception messages and lack of Content Security Policy.
**Learning:** Returning `str(e)` in Flask JSON responses can expose internal application logic or stack traces to clients.
**Prevention:** Always use generic error messages for client-facing responses and implement CSP via `@app.after_request` to enforce resource loading policies.

## 2026-05-18 - Backend Validation and Header Hardening
**Vulnerability:** Lack of server-side validation for player counts and names, and missing defensive headers.
**Learning:** Relying solely on frontend validation for business logic (like duplicate names) allows for easy bypass via direct API calls, potentially leading to inconsistent application state.
**Prevention:** Implement strict server-side schema validation (type checks, limits, and uniqueness) for all POST endpoints and enforce defense-in-depth headers (X-Frame-Options, X-Content-Type-Options) globally.
