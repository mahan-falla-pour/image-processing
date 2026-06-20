import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

img = Image.open(os.path.join(os.path.dirname(__file__), '..', 'Q1', 'download.jpeg'))
img_array = np.array(img)

R, G, B = img_array[:,:,0], img_array[:,:,1], img_array[:,:,2]
gray_array = (0.2989 * R + 0.5870 * G + 0.1140 * B).astype(np.uint8)

threshold = 128
binary_image = np.where(gray_array < threshold, 0, 255).astype(np.uint8)

negative_image = 255 - binary_image

print("--- Array Comparison (top-left 5x5 block) ---")
print("Original Binary Array:")
print(binary_image[0:5, 0:5])
print("\nNegative Binary Array:")
print(negative_image[0:5, 0:5])

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].imshow(binary_image, cmap='gray', vmin=0, vmax=255)
axes[0].set_title('Original Binary Image')
axes[0].axis('off')

axes[1].imshow(negative_image, cmap='gray', vmin=0, vmax=255)
axes[1].set_title('Negative Binary Image')
axes[1].axis('off')

plt.tight_layout()
plt.show()
