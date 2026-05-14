## 2026-04-08 - Flask Security Hardening
**Vulnerability:** Information leakage through raw exception messages and lack of Content Security Policy.
**Learning:** Returning `str(e)` in Flask JSON responses can expose internal application logic or stack traces to clients.
**Prevention:** Always use generic error messages for client-facing responses and implement CSP via `@app.after_request` to enforce resource loading policies.

## 2026-05-14 - Flask Request Validation Patterns
**Vulnerability:** Potential for `TypeError` or unhandled exceptions when processing malformed JSON payloads.
**Learning:** When validating JSON payloads in Flask, always check `isinstance(data, dict)` after calling `request.get_json(silent=True)` to prevent errors when non-dictionary JSON roots (e.g., numbers, lists) are received.
**Prevention:** Use `request.get_json(silent=True)` and explicitly validate the data type and presence of required fields before processing.
