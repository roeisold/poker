## 2026-05-16 - Asset delivery optimization: high-res JPG to WebP
**Learning:** Serving 1000x1000 JPG icons for 22px-50px UI elements caused a 5.2MB initial payload. Optimization to 200x200 WebP (quality 85) reduced asset weight by 98.7% (~70KB total).
**Action:** Always check source image resolutions against their rendered UI size. Prioritize WebP format and lazy loading for decorative or repeated assets.
