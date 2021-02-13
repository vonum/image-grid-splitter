import cv2
import zipfile
from os import listdir
from os.path import isfile, join
import pdb

from image_cropper import ImageCropper

ZIPPED_PATH = "zipped_images"
ORIGINAL_PATH = "original_images"
OUTPUT_PATH = "images"

def list_files(path):
  return [
    join(path, f) for f in listdir(path)
    if isfile(join(path, f))
  ]

zip_files = list_files(ZIPPED_PATH)
print(f"Unzipping files:\n{zip_files}\n\n")

for f in zip_files:
  with zipfile.ZipFile(f, "r") as zip_file:
    zip_file.extractall(ORIGINAL_PATH)

original_images = list_files(ORIGINAL_PATH)
images = [cv2.imread(image) for image in original_images]
print(f"Cropping images:\n{original_images}\n\n")

cropper = ImageCropper()
output_images = cropper.crop_images(images)

for i, image in enumerate(output_images):
  cv2.imwrite(f"{OUTPUT_PATH}/{i}.jpg", image)
