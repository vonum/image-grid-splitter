import argparse
import cv2
import zipfile
from pathlib import Path

from image_cropper import ImageCropper

def list_files(path, extension="*.jpg"):
  return [str(p) for p in Path(path).rglob(extension)]

ap = argparse.ArgumentParser()
ap.add_argument(
  "--zipped_images_path",
  "-z",
  type=str,
  default="zipped_images",
  help="Path of zipped images"
)
ap.add_argument(
  "--original_images_path",
  "-o",
  type=str,
  default="original_images",
  help="Path of original images"
)
ap.add_argument(
  "--output_images_path",
  "-i",
  type=str,
  default="images",
  help="Path of output images"
)
ap.add_argument(
  "--width",
  "-w",
  type=int,
  default=1024,
  help="Width of resized images"
)
ap.add_argument(
  "--height",
  "-hh",
  type=int,
  default=1024,
  help="Height of resized images"
)

args = vars(ap.parse_args())
ZIPPED_PATH = args["zipped_images_path"]
ORIGINAL_PATH = args["original_images_path"]
OUTPUT_PATH = args["output_images_path"]
WIDTH = args["width"]
HEIGHT = args["height"]

zip_files = list_files(ZIPPED_PATH, extension="*.zip")
print(f"Unzipping files:\n{zip_files}\n\n")

for f in zip_files:
  with zipfile.ZipFile(f, "r") as zip_file:
    zip_file.extractall(ORIGINAL_PATH)

original_images = list_files(ORIGINAL_PATH)

cropper = ImageCropper(width=WIDTH, height=HEIGHT)
batch_size = 50

for i in range(0, len(original_images), batch_size):
  original_images_batch = original_images[i:i+batch_size]
  images = [cv2.imread(image) for image in original_images_batch]
  print(f"Resizing images:\n{original_images_batch}\n\n")

  output_images = cropper.resize_images(images)

  for idx, image in enumerate(output_images):
    cv2.imwrite(f"{OUTPUT_PATH}/{i}-{idx}.jpg", image)
