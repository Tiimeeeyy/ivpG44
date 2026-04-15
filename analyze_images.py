import os
from collections import Counter
from PIL import Image

# UPDATE THIS to the exact path where your training images are stored
IMG_DIR = "/Data/training_images"

def analyze_directory(directory):
    print(f"Scanning directory: {directory}...\n")
    
    sizes = Counter()
    modes = Counter()
    total_images = 0
    
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            filepath = os.path.join(directory, filename)
            try:
                # We open the image to read metadata, but don't load the pixel data into memory
                # This makes it very fast even for 17,000+ images.
                with Image.open(filepath) as img:
                    sizes[img.size] += 1
                    modes[img.mode] += 1
                    total_images += 1
            except Exception as e:
                print(f"Error reading {filename}: {e}")
                
    print(f"Total valid images analyzed: {total_images}")
    
    print("\n--- Image Sizes (Width x Height) ---")
    for size, count in sizes.most_common():
        print(f"  {size[0]} x {size[1]} pixels: {count} images")
        
    print("\n--- Image Color Modes ---")
    for mode, count in modes.most_common():
        print(f"  Mode '{mode}' (e.g., 'RGB'=Color, 'L'=Grayscale): {count} images")

if __name__ == "__main__":
    analyze_directory(IMG_DIR)