# Assignment 1: Image Basics with OpenCV
# Task 1: Read an Image and Display Its Properties

import cv2
import os

# Get the main project folder path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Read the input colour image
IMAGE_PATH = os.path.join(BASE_DIR, "input", "input_image.jpg")
img = cv2.imread(IMAGE_PATH)

# Check whether the image is loaded successfully
if img is None:
    print("Error: Image not found!")
    exit()

# Get image height, width and number of channels
height, width, channels = img.shape

# Display image properties
print("\n----- Image Properties -----")
print("Shape:", img.shape)
print("Height:", height)
print("Width:", width)
print("Channels:", channels)
print("Total Pixels:", height * width)
print("Total Elements:", img.size)
print("Data Type:", img.dtype)

# Display one pixel value at row 100 and column 100
if height > 100 and width > 100:
    pixel = img[100, 100]

    # OpenCV stores colour channels in BGR order
    print("\n----- Pixel Information -----")
    print("Pixel Value (B, G, R):", pixel)

else:
    print("\nImage is too small to access pixel (100, 100).")
