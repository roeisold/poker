## 2025-05-15 - Image Optimization for Poker Chips
**Learning:** The application was serving 1000x1000 pixel JPEG images (~400KB each) for 22x22 and 50x50 icons. This resulted in over 5MB of image data being transferred for simple UI elements.
**Action:** Resize images to 100x100 and convert to WebP format to drastically reduce payload size while maintaining visual quality for the intended display size.
