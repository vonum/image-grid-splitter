import cv2
import pdb

class ImageCropper:
  def __init__(self, rows=3, cols=3, width=512, height=512):
    self.rows = rows
    self.cols = cols
    self.width = width
    self.height = height

  def crop_images(self, images):
    output_images = []

    for image in images:
      cropped_images = self.crop_image(image)
      output_images += cropped_images

    return output_images

  def crop_image(self, image):
    xstep = image.shape[0] / self.rows
    ystep = image.shape[1] / self.cols

    final_images = []
    for row in range(0, self.rows):
      for col in range(0, self.cols):
        xstart = int(row * xstep)
        xend = int(xstart + xstep)
        ystart = int(col * ystep)
        yend = int(ystart + ystep)

        cropped_image = image[ystart:yend, xstart:xend]
        resized_image = cv2.resize(cropped_image,
                                  (self.width, self.height),
                                   interpolation = cv2.INTER_AREA)
        final_images.append(resized_image)

    return final_images

