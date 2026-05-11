## 2026-04-08 - Flask Security Hardening
**Vulnerability:** Information leakage through raw exception messages and lack of Content Security Policy.
**Learning:** Returning `str(e)` in Flask JSON responses can expose internal application logic or stack traces to clients.
**Prevention:** Always use generic error messages for client-facing responses and implement CSP via `@app.after_request` to enforce resource loading policies.

## 2026-05-11 - Defensive JSON Validation
**Vulnerability:** Potential Denial of Service or application crash when receiving non-dictionary JSON payloads or extremely large lists.
**Learning:** Flask's `request.json` can be any valid JSON type. Accessing it as a dict without type checking can lead to unhandled TypeErrors. Lack of limits on input lists can lead to DoS.
**Prevention:** Always validate that `request.json` is a dictionary, verify field types, and enforce maximum length limits on user-provided lists.
