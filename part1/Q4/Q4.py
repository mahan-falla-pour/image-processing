import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

img = Image.open(os.path.join(os.path.dirname(__file__), 'question4.tif'))
img_array = np.array(img)

if img_array.ndim == 3:
    R, G, B = img_array[:,:,0], img_array[:,:,1], img_array[:,:,2]
    gray_array = (0.2989 * R + 0.5870 * G + 0.1140 * B).astype(np.uint8)
elif img_array.ndim == 2:
    gray_array = img_array
else:
    raise ValueError("Unsupported image format")

def apply_gamma_correction(image_array, gamma):
    normalized_img = image_array / 255.0
    corrected_img = np.power(normalized_img, gamma)
    final_img = (corrected_img * 255).astype(np.uint8)
    return final_img

gamma_1 = 0.3
gamma_2 = 2.0

img_gamma_05 = apply_gamma_correction(gray_array, gamma_1)
img_gamma_20 = apply_gamma_correction(gray_array, gamma_2)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(gray_array, cmap='gray', vmin=0, vmax=255)
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(img_gamma_05, cmap='gray', vmin=0, vmax=255)
axes[1].set_title(rf'Gamma Correction ($\gamma$ = {gamma_1})' + '\n(Brighter)')
axes[1].axis('off')

axes[2].imshow(img_gamma_20, cmap='gray', vmin=0, vmax=255)
axes[2].set_title(rf'Gamma Correction ($\gamma$ = {gamma_2})' + '\n(Darker)')
axes[2].axis('off')

plt.tight_layout()
plt.show()
