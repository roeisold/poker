import os
from PIL import Image

def optimize_images():
    static_dir = 'static'
    for filename in os.listdir(static_dir):
        if filename.endswith('.jpg'):
            filepath = os.path.join(static_dir, filename)
            with Image.open(filepath) as img:
                # Resize to 200x200 using LANCZOS for high quality
                img = img.resize((200, 200), Image.Resampling.LANCZOS)
                # Define new filename
                new_filename = os.path.splitext(filename)[0] + '.webp'
                new_filepath = os.path.join(static_dir, new_filename)
                # Save as WebP with 85% quality
                img.save(new_filepath, 'WEBP', quality=85)
                print(f"Optimized {filename} -> {new_filename}")

if __name__ == "__main__":
    optimize_images()
