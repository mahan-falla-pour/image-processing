import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

img = Image.open(os.path.join(os.path.dirname(__file__), 'download.jpeg'))
img_array = np.array(img)

R, G, B = img_array[:,:,0], img_array[:,:,1], img_array[:,:,2]
gray_img = (0.2989 * R + 0.5870 * G + 0.1140 * B).astype(np.uint8)

threshold = 127
binary_img = np.where(gray_img > threshold, 255, 0).astype(np.uint8)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(img_array)
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(gray_img, cmap='gray')
axes[1].set_title('Grayscale Image')
axes[1].axis('off')

axes[2].imshow(binary_img, cmap='gray')
axes[2].set_title('Binary Image')
axes[2].axis('off')

plt.tight_layout()
plt.show()

print("Original image shape:", img_array.shape)
print("First 2x2 pixels (RGB):\n", img_array[:2, :2])
print("\nGrayscale image shape:", gray_img.shape)
print("First 2x2 pixels:\n", gray_img[:2, :2])
print("\nBinary image shape:", binary_img.shape)
print("First 2x2 pixels:\n", binary_img[:2, :2])
