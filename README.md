# image-grid-splitter
Script that takes an image and splits it into N same sized images. Works only
with same sized cells in a grid.

## Setup
1. Install Python 3.7
2. Create a virtual environment
3. `pip install -r requirements.txt`

## How to run?
### Cropping and resizing
1. Copy zip files containing images to `ZIPPED_IMAGES_PATH`
2. `ORIGINAL_IMAGES_PATH` will contain extracted images
3. `OUTPUT_IMAGES_PATH` will contain cropped and resized images
`python prep_stylegan_cropped_images.py [-z ZIPPED_IMAGES_PATH] [-o ORIGINAL_IMAGES_PATH] [-i OUTPUT_IMAGES_PATH]`

### Resizing
1. Copy zip files containing images to `ZIPPED_IMAGES_PATH`
2. `ORIGINAL_IMAGES_PATH` will contain extracted images
3. `OUTPUT_IMAGES_PATH` will contain cropped and resized images
`python prep_stylegan_resized_images.py [-z ZIPPED_IMAGES_PATH] [-o ORIGINAL_IMAGES_PATH] [-i OUTPUT_IMAGES_PATH]`
