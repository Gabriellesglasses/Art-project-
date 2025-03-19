import os
from PIL import Image

# Define directories
full_dir = "images/fulls/"
thumb_dir = "images/thumbs/"

# Ensure the thumbs directory exists
if not os.path.exists(thumb_dir):
    os.makedirs(thumb_dir)

# Loop through all .jpg images in the full directory
for filename in os.listdir(full_dir):
    if filename.endswith(".jpg"):
        full_image_path = os.path.join(full_dir, filename)
        thumb_image_path = os.path.join(thumb_dir, filename)

        # Open the image
        img = Image.open(full_image_path)

        # Reduce quality and save to thumbs directory
        img.save(thumb_image_path, "JPEG", quality=10)  # Set quality as needed

        print(f"Processed {filename}")


