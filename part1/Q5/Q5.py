import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

img = Image.open(os.path.join(os.path.dirname(__file__), '..', 'Q4', 'question4.tif'))
img_array = np.array(img, dtype=float)

if img_array.ndim == 3:
    R, G, B = img_array[:,:,0], img_array[:,:,1], img_array[:,:,2]
    gray_array = (0.2989 * R + 0.5870 * G + 0.1140 * B).astype(np.uint8)
elif img_array.ndim == 2:
    gray_array = img_array
else:
    raise ValueError("Unsupported image format")

pad_width = 1
padded_img = np.pad(img_array, pad_width=pad_width, mode='constant', constant_values=0)

rows, cols = img_array.shape
smoothed_img = np.zeros((rows, cols), dtype=float)

for i in range(rows):
    for j in range(cols):
        region = padded_img[i : i+3, j : j+3]
        smoothed_img[i, j] = np.sum(region) / 9.0

smoothed_img_uint8 = np.clip(smoothed_img, 0, 255).astype(np.uint8)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(img_array, cmap='gray', vmin=0, vmax=255)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(smoothed_img_uint8, cmap='gray', vmin=0, vmax=255)
plt.title('Smoothed Image (3x3 Mean Filter)')
plt.axis('off')

plt.tight_layout()
plt.show()
