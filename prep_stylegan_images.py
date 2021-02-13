import cv2
import zipfile
from pathlib import Path

from image_cropper import ImageCropper

ZIPPED_PATH = "zipped_images"
ORIGINAL_PATH = "original_images"
OUTPUT_PATH = "images"

def list_files(path, extension="*.jpg"):
  return [str(p) for p in Path(path).rglob(extension)]

zip_files = list_files(ZIPPED_PATH, extension="*.zip")
print(f"Unzipping files:\n{zip_files}\n\n")

for f in zip_files:
  with zipfile.ZipFile(f, "r") as zip_file:
    zip_file.extractall(ORIGINAL_PATH)

original_images = list_files(ORIGINAL_PATH)

cropper = ImageCropper()
batch_size = 50

for i in range(0, len(original_images), batch_size):
  original_images_batch = original_images[i:i+batch_size]
  images = [cv2.imread(image) for image in original_images_batch]
  print(f"Cropping images:\n{original_images}\n\n")

  output_images = cropper.crop_images(images)

  for idx, image in enumerate(output_images):
    cv2.imwrite(f"{OUTPUT_PATH}/{i}-{idx}.jpg", image)
