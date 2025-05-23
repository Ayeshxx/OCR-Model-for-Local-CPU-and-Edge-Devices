import pytesseract
import cv2
from PIL import Image
import os
import shutil


def check_and_move_corrupted_images(directory, corrupted_dir):
    total = 0
    corrupted = 0

    # Create the corrupted image directory if it doesn't exist
    os.makedirs(corrupted_dir, exist_ok=True)

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')):
                file_path = os.path.join(root, file)
                total += 1
                try:
                    with Image.open(file_path) as img:
                        img.verify()
                except (IOError, SyntaxError) as e:
                    print(f"❌ Corrupted image found: {file_path}")
                    corrupted += 1
                    # Move corrupted file
                    corrupted_path = os.path.join(corrupted_dir, file)
                    shutil.move(file_path, corrupted_path)

    print(f"\n✅ Scan complete.\nTotal images: {total}\nCorrupted images moved: {corrupted}")

if __name__ == "__main__":
    directory = r"C:\Users\nazia\OCR-Model-for-Local-CPU-and-Edge-Devices"  # Path to your image dataset
    corrupted_dir = r"C:\Users\nazia\OCR-Model-for-Local-CPU-and-Edge-Devicescorrupted"  # Where to move corrupted images
    check_and_move_corrupted_images(directory, corrupted_dir)
