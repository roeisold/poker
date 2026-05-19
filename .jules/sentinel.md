## 2026-04-08 - Flask Security Hardening
**Vulnerability:** Information leakage through raw exception messages and lack of Content Security Policy.
**Learning:** Returning `str(e)` in Flask JSON responses can expose internal application logic or stack traces to clients.
**Prevention:** Always use generic error messages for client-facing responses and implement CSP via `@app.after_request` to enforce resource loading policies.

## 2026-05-19 - Defense-in-Depth and Robust Input Validation
**Vulnerability:** Missing defense-in-depth security headers and lack of server-side input validation.
**Learning:** Relying solely on frontend validation for business logic (like duplicate names or player limits) is insufficient and leaves the application vulnerable to DoS or logic bypass via direct API manipulation.
**Prevention:** Implement standard security headers (X-Frame-Options, X-Content-Type-Options, Referrer-Policy) and perform exhaustive backend validation of all JSON payloads, including structure, types, and business constraints.
