## 2026-04-08 - Flask Security Hardening
**Vulnerability:** Information leakage through raw exception messages and lack of Content Security Policy.
**Learning:** Returning `str(e)` in Flask JSON responses can expose internal application logic or stack traces to clients.
**Prevention:** Always use generic error messages for client-facing responses and implement CSP via `@app.after_request` to enforce resource loading policies.

## 2026-05-12 - Denial of Service (DoS) Mitigation
**Vulnerability:** Unbounded input processing in the `/calculate` endpoint allowed for potential CPU/memory exhaustion.
**Learning:** Complex calculation loops without input size limits are vulnerable to DoS attacks via large payloads.
**Prevention:** Enforce strict limits on the number of entities (e.g., 50 players) and validate input types (e.g., `isinstance(data, dict)`) at the entry point of sensitive endpoints.
