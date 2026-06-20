import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

image = Image.open(os.path.join(os.path.dirname(__file__), '..', 'Q4', 'question4.tif'))
img_array = np.array(image)

if img_array.ndim == 3:
    R, G, B = img_array[:,:,0], img_array[:,:,1], img_array[:,:,2]
    gray_array = (0.2989 * R + 0.5870 * G + 0.1140 * B).astype(np.uint8)
elif img_array.ndim == 2:
    gray_array = img_array
else:
    raise ValueError("Unsupported image format")

L = 256

hist, bins = np.histogram(img_array.flatten(), bins=L, range=[0, 255])

pdf = hist / img_array.size

cdf = np.cumsum(pdf)

transformation_map = np.round(cdf * (L - 1)).astype(np.uint8)

equalized_img_array = transformation_map[img_array]

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].imshow(img_array, cmap='gray')
axes[0, 0].set_title("Original Image")
axes[0, 0].axis('off')

axes[0, 1].hist(img_array.flatten(), bins=L, range=[0, 255], color='blue', alpha=0.7)
axes[0, 1].set_title("Original Histogram")

axes[1, 0].imshow(equalized_img_array, cmap='gray')
axes[1, 0].set_title("Equalized Image")
axes[1, 0].axis('off')

axes[1, 1].hist(equalized_img_array.flatten(), bins=L, range=[0, 255], color='red', alpha=0.7)
axes[1, 1].set_title("Equalized Histogram")

plt.tight_layout()
plt.show()
