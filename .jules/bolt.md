## 2025-05-18 - Chip Image Optimization
**Learning:** Found that chip assets were 1000x1000 JPEGs (~400KB each), totaling over 5MB. Resizing them to 200x200 (sufficient for UI display) and converting to WebP reduced the total asset weight by ~98%.
**Action:** Prioritize auditing static asset sizes and formats, especially for repetitive UI elements like icons or avatars.
