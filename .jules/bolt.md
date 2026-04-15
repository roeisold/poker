# Bolt's Performance Journal

This journal tracks critical performance discoveries and optimizations.

## 2026-04-15 - Initial Gzip Implementation
**Learning:** Manual Gzip compression in Flask is a high-impact, low-complexity optimization for text-based responses. It reduces the main HTML payload size by ~73% (17.1KB to ~4.6KB).
**Action:** Always verify `Vary: Accept-Encoding` is set and `direct_passthrough` responses are handled correctly to avoid empty or double-encoded responses.
