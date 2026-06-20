# Digital Image Processing

Implementation of classical image processing algorithms based on **"Digital Image Processing" by Gonzalez & Woods (3rd Edition)**.

The course is divided into three homework assignments, each covering a different set of chapters from the book.

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
| Q2 | Grayscale image colorization (two methods) |
| Q3 | PSNR calculation (manual vs OpenCV) |
| Q4 | Median filter for image reconstruction |
| Q5 | DCT quantization and Run-Length Coding (RLC) |

---

### Part 3 — Coming Soon
Frequency domain processing and morphological operations.

---

## Tech Stack

- Python 3.8+
- NumPy
- Pillow (PIL)
- Matplotlib
- OpenCV

Install dependencies:

```bash
pip install numpy pillow matplotlib opencv-python
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

**Part 2** — Jupyter Notebook:
```bash
cd part2
jupyter notebook Untitled.ipynb
```

---

## Reference

> Gonzalez, R. C., & Woods, R. E. (2008). *Digital Image Processing* (3rd ed.). Prentice Hall.
