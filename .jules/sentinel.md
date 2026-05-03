## 2026-04-08 - Flask Security Hardening
**Vulnerability:** Information leakage through raw exception messages and lack of Content Security Policy.
**Learning:** Returning `str(e)` in Flask JSON responses can expose internal application logic or stack traces to clients.
**Prevention:** Always use generic error messages for client-facing responses and implement CSP via `@app.after_request` to enforce resource loading policies.

## 2026-05-03 - Robust JSON Input Validation
**Vulnerability:** Potential `TypeError` leading to 500 Internal Server Error when receiving non-dictionary JSON roots (e.g., `true`, `123`).
**Learning:** Checking for keys in `request.json` without verifying it is a `dict` first can cause crashes if the client sends a valid JSON payload that is not an object.
**Prevention:** Always verify `isinstance(data, dict)` before attempting to check for keys or access members of the JSON payload.
