import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

def manual_laplacian_sharpening(image_path, scale=1.0):
    img = Image.open(image_path)
    img_array = np.array(img, dtype=np.float32)

    if img_array.ndim == 3:
        R, G, B = img_array[:,:,0], img_array[:,:,1], img_array[:,:,2]
        gray_array = (0.2989 * R + 0.5870 * G + 0.1140 * B).astype(np.uint8)
    elif img_array.ndim == 2:
        gray_array = img_array
    else:
        raise ValueError("Unsupported image format")

    rows, cols = img_array.shape

    laplacian_mask = np.array([[ 0, -1,  0],
                               [-1,  4, -1],
                               [ 0, -1,  0]], dtype=np.float32)

    edges = np.zeros_like(img_array)

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            region = img_array[i-1:i+2, j-1:j+2]
            edges[i, j] = np.sum(region * laplacian_mask)

    sharpened_array = img_array + (scale * edges)
    sharpened_array = np.clip(sharpened_array, 0, 255).astype(np.uint8)
    edges_clipped = np.clip(edges, 0, 255).astype(np.uint8)

    return img_array.astype(np.uint8), edges_clipped, sharpened_array

image_path = os.path.join(os.path.dirname(__file__), '..', 'Q4', 'question4.tif')
img_orig, img_edges, img_sharp = manual_laplacian_sharpening(image_path, scale=1.0)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(img_orig, cmap='gray')
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(img_edges, cmap='gray')
axes[1].set_title('Laplacian Edges')
axes[1].axis('off')

axes[2].imshow(img_sharp, cmap='gray')
axes[2].set_title('Sharpened Image')
axes[2].axis('off')

plt.tight_layout()
plt.show()
