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

def zoomMinus(image, factor):
    height, width = image.shape[:2]
    new_height = int(height * factor)
    new_width = int(width * factor)
    imgZoom = np.zeros((new_height, new_width, 3), dtype=image.dtype)
    for y in range(new_height):
        for x in range(new_width):
            ori_y = int(y / factor)
            ori_x = int(x / factor)
            ori_y = min(ori_y, height - 1)
            ori_x = min(ori_x, width - 1)
            imgZoom[y, x] = image[ori_y, ori_x]
    return imgZoom

# Membaca gambar
image = img.imread(r"C:\\Users\\ASUS\\Documents\\Smester 5\\Pengolahan citra digital\\Everest mountain.jpg")

# Faktor zoom
skala = 2.0

# Melakukan zoom plus (perbesaran)
imgZoom = zoomPlus(image, skala)

# Melakukan zoom minus (perkecil)
imgZoomMinus = zoomMinus(image, skala)

# Menyimpan gambar hasil zoom
img.imwrite(r"C:\\Users\\ASUS\\Documents\\Smester 5\\Pengolahan citra digital\\Everest mountain.jpg", imgZoom)
img.imwrite(r"C:\\Users\\ASUS\\Documents\\Smester 5\\Pengolahan citra digital\\Everest mountain.jpg", imgZoomMinus)

# Menampilkan gambar asli dan hasil zoom
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.imshow(image)
plt.title("Gambar Asli")

plt.subplot(1, 3, 2)
plt.imshow(imgZoom)
plt.title(f"Zoom Plus (x{skala})")

plt.subplot(1, 3, 3)
plt.imshow(imgZoomMinus)
plt.title(f"Zoom Minus (x{skala})")

plt.show()
