import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

img = Image.open(os.path.join(os.path.dirname(__file__), '..', 'Q1', 'download.jpeg'))
img_array = np.array(img)

R, G, B = img_array[:,:,0], img_array[:,:,1], img_array[:,:,2]
gray_image = (0.2989 * R + 0.5870 * G + 0.1140 * B).astype(np.uint8)

def downsample_average(image, k):
    H, W = image.shape
    H_new = (H // k) * k
    W_new = (W // k) * k
    img_cropped = image[:H_new, :W_new]
    downsampled_img = img_cropped.reshape(H_new // k, k, W_new // k, k).mean(axis=(1, 3))
    return downsampled_img.astype(np.uint8)

img_half_scale = downsample_average(gray_image, 2)
img_quarter_scale = downsample_average(gray_image, 4)

print(f"Original Grayscale Shape: {gray_image.shape}")
print(f"1/2 Scale Image Shape:    {img_half_scale.shape}")
print(f"1/4 Scale Image Shape:    {img_quarter_scale.shape}")

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(gray_image, cmap='gray')
axes[0].set_title('Original Grayscale\nShape: {}'.format(gray_image.shape))
axes[0].axis('off')

axes[1].imshow(img_half_scale, cmap='gray')
axes[1].set_title('1/2 Scale (2x2 Avg)\nShape: {}'.format(img_half_scale.shape))
axes[1].axis('off')

axes[2].imshow(img_quarter_scale, cmap='gray')
axes[2].set_title('1/4 Scale (4x4 Avg)\nShape: {}'.format(img_quarter_scale.shape))
axes[2].axis('off')

plt.tight_layout()
plt.show()
