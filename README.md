# Digital Image Processing

Implementation of classical image processing algorithms based on **"Digital Image Processing" by Gonzalez & Woods (3rd Edition)**.

The course is divided into three homework assignments, each covering a different set of topics from the book.

---

## Assignments

### [Part 1](./part1) — Fundamentals
Covers the basics of digital images, spatial domain processing, and intensity transformations.

| Question | Topic |
|----------|-------|
| Q1 | RGB to Grayscale and Binary conversion |
| Q2 | Image downsampling via block averaging |
| Q3 | Binary image negation |
| Q4 | Gamma correction |
| Q5 | 3×3 mean filter (manual convolution) |
| Q6 | Laplacian edge detection & sharpening |
| Q7 | Histogram equalization |

---

### [Part 2](./part2) — Color & Filtering
Covers color image processing, noise reduction, and image quality metrics.

| Question | Topic |
|----------|-------|
| Q1 | RGB and HSI color space decomposition |
| Q2 | Grayscale image colorization using reference images (two methods) |
| Q3 | PSNR calculation from scratch (manual vs `cv2.PSNR` verification) |
| Q4 | Noise type identification, median filter reconstruction, and PSNR evaluation |
| Q5 | JPEG compression: DCT quantization, zig-zag scan, and Run-Length Coding (RLC) |

---

### [Part 3](./part3) — Morphology, Segmentation & Analysis
Covers morphological operations, image segmentation, and feature extraction.

| Question | Topic |
|----------|-------|
| Q1 | Object boundary extraction via morphological erosion |
| Q2 | Image segmentation using Otsu's thresholding, CCL, and region merging |
| Q3 | Cell detection, counting (149 cells), and feature extraction from microscopy images |

---

## Tech Stack

- Python 3.8+
- NumPy
- Pillow (PIL)
- Matplotlib
- OpenCV

Install dependencies:

```bash
pip install numpy pillow matplotlib opencv-python openpyxl pandas
```

---

## How to Run

**Part 1** — standalone Python scripts:
```bash
cd part1
python Q1/Q1.py
python Q2/Q2.py
# ...
```

**Parts 2 & 3** — Jupyter Notebook:
```bash
cd part2
jupyter notebook Untitled.ipynb

cd part3
jupyter notebook Untitled.ipynb
```

---

## Reference

> Gonzalez, R. C., & Woods, R. E. (2008). *Digital Image Processing* (3rd ed.). Prentice Hall.
