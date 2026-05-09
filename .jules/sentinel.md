## 2026-04-08 - Flask Security Hardening
**Vulnerability:** Information leakage through raw exception messages and lack of Content Security Policy.
**Learning:** Returning `str(e)` in Flask JSON responses can expose internal application logic or stack traces to clients.
**Prevention:** Always use generic error messages for client-facing responses and implement CSP via `@app.after_request` to enforce resource loading policies.

## 2026-05-09 - Server-side Input Validation and DoS Protection
**Vulnerability:** Lack of server-side input validation and player limits in the `/calculate` endpoint.
**Learning:** Client-side validation is insufficient for security; attackers can bypass it to send malformed or excessively large payloads, potentially causing server-side errors or Denial of Service.
**Prevention:** Implement strict type checking for JSON payloads and enforce reasonable limits on input data (e.g., maximum 50 players) at the API level.
