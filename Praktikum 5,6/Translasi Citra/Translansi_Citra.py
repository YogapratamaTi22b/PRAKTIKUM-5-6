import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

def Translasi(image, shiftX, shiftY):
    imgTranslasi = np.roll(image, shift=shiftY, axis=0)  # Geser secara vertikal
    imgTranslasi = np.roll(imgTranslasi, shift=shiftX, axis=1)  # Geser secara horizontal
    
    # Mengisi area kosong dengan warna hitam (0)
    if shiftY > 0:
        imgTranslasi[:shiftY, :] = 0  # Area atas jika digeser ke bawah
    elif shiftY < 0:
        imgTranslasi[shiftY:, :] = 0  # Area bawah jika digeser ke atas
    if shiftX > 0:
        imgTranslasi[:, :shiftX] = 0  # Area kiri jika digeser ke kanan
    elif shiftX < 0:
        imgTranslasi[:, shiftX:] = 0  # Area kanan jika digeser ke kiri
    
    return imgTranslasi

image = img.imread(r"C:\\Users\\ASUS\\Documents\\Smester 5\\Pengolahan citra digital\\Everest mountain.jpg")
imgResult = Translasi(image, shiftX=50, shiftY=-300)

plt.figure(figsize=(10, 10))
plt.subplot(2, 1, 1)
plt.imshow(image)
plt.subplot(2, 1, 2)
plt.imshow(imgResult)
plt.show()
