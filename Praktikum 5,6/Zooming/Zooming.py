import numpy as np
import imageio as img
import matplotlib.pyplot as plt

def zoomPlus(image, factor):
  height, width = image.shape[:2]
  new_height = int(height / factor)
  new_width = int(width / factor)
  imgZoom = np.zeros((new_height, new_width, 3), dtype=image.dtype)
  for y in range(new_height):
    for x in range(new_width):
      ori_y = int(y * factor)
      ori_x = int(x * factor)
      ori_y = min(ori_y, height - 1)
      ori_x = min(ori_x, width - 1)
      imgZoom[y, x] = image[ori_y, ori_x]
  return imgZoom

image = img.imread(r"C:\\Users\\ASUS\\Documents\\Smester 5\\Pengolahan citra digital\\Everest mountain.jpg")
skala = 2.0

imgZoom= zoomPlus(image, skala)
img.imwrite(r"C:\\Users\\ASUS\\Documents\\Smester 5\\Pengolahan citra digital\\Everest mountain.jpg",imgZoom)
plt.subplot(1, 2, 1)
plt.imshow(image)

plt.subplot(1, 2, 2)
plt.imshow(imgZoom)
plt.show()