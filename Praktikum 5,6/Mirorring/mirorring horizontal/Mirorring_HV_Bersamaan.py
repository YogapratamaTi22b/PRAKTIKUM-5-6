import numpy as np
import imageio as img
import matplotlib.pyplot as plt

path = r"C:\\Users\\ASUS\\Documents\\Smester 5\\Pengolahan citra digital\\Everest mountain.jpg"
image = img.imread(path)

# Membalikkan gambar secara horizontal dan vertikal
horizontal_flip = image[:, ::-1]   # Membalikkan gambar secara horizontal
vertical_flip = image[::-1, :]     # Membalikkan gambar secara vertikal
both_flip = image[::-1, ::-1]      # Membalikkan gambar secara horizontal dan vertikal

# Menampilkan hasil
plt.figure(figsize=(12, 8))

plt.subplot(1, 4, 1)
plt.imshow(image)
plt.title("Gambar Asli")

plt.subplot(1, 4, 2)
plt.imshow(horizontal_flip)
plt.title("Mirror Horizontal")

plt.subplot(1, 4, 3)
plt.imshow(vertical_flip)
plt.title("Mirror Vertikal")

plt.subplot(1, 4, 4)
plt.imshow(both_flip)
plt.title("Mirror Horizontal & Vertikal")

plt.show()
