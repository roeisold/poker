## 2026-04-08 - Flask Security Hardening
**Vulnerability:** Information leakage through raw exception messages and lack of Content Security Policy.
**Learning:** Returning `str(e)` in Flask JSON responses can expose internal application logic or stack traces to clients.
**Prevention:** Always use generic error messages for client-facing responses and implement CSP via `@app.after_request` to enforce resource loading policies.

## 2026-05-05 - JSON Payload Validation & DoS Mitigation
**Vulnerability:** Potential for `TypeError` or `AttributeError` when receiving non-dictionary JSON roots and DoS risk from unbounded player lists.
**Learning:** Flask's `request.json` can be any valid JSON type (list, number, etc.). If the code assumes it's a dictionary (e.g., `data.get(...)`), it may crash or behave unexpectedly.
**Prevention:** Always validate that `request.json` is a dictionary and enforce business-logic limits (like a maximum number of items in a list) to prevent resource exhaustion.
