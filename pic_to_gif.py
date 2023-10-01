from PIL import Image
import glob
import os

# Use glob to get all .jpg files
image_folder = " "  # Please make sure this is the actual folder path where your images are stored
image_paths = glob.glob(os.path.join(image_folder, "*.jpg"))

# Sort the list
image_paths.sort()

# Read the images
images = [Image.open(image_path) for image_path in image_paths]

# Create a GIF
images[0].save("animated.gif",
               save_all=True,
               append_images=images[1:],
               loop=0,
               duration=50)

# Delete all .jpg images
for image_path in image_paths:
    os.remove(image_path)
