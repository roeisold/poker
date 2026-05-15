## 2026-04-08 - Flask Security Hardening
**Vulnerability:** Information leakage through raw exception messages and lack of Content Security Policy.
**Learning:** Returning `str(e)` in Flask JSON responses can expose internal application logic or stack traces to clients.
**Prevention:** Always use generic error messages for client-facing responses and implement CSP via `@app.after_request` to enforce resource loading policies.

## 2026-04-10 - Defensive Input Validation
**Vulnerability:** Potential for `TypeError` or DoS when processing malformed or oversized JSON payloads.
**Learning:** Flask's `request.json` can return any valid JSON type (list, string, etc.). Accessing keys on a non-dict root without type verification causes unhandled exceptions. Additionally, lack of item count limits on lists can lead to resource exhaustion.
**Prevention:** Use `request.get_json(silent=True)` followed by `isinstance(data, dict)` checks. Explicitly validate list types and enforce reasonable length limits (e.g., 50 items) for collection fields.
