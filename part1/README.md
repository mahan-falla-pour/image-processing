# Digital Image Processing — Homework 1

A collection of fundamental image processing operations implemented from scratch using NumPy and PIL, without relying on high-level library functions.

## Topics Covered

| Question | Topic |
|----------|-------|
| Q1 | RGB → Grayscale → Binary conversion |
| Q2 | Image downsampling via block averaging |
| Q3 | Binary image negation |
| Q4 | Gamma correction |
| Q5 | 3×3 mean filter (manual convolution) |
| Q6 | Laplacian edge detection & image sharpening |
| Q7 | Histogram equalization |

## Project Structure

```
HW1_image/
├── Q1/
│   ├── Q1.py
│   ├── download.jpeg        # Input image for Q1–Q3
│   └── Figure_1.png         # Output
├── Q2/
│   ├── Q2.py
│   └── Figure_1.png
├── Q3/
│   ├── Q3.py
│   └── Figure_1.png
├── Q4/
│   ├── Q4.py
│   ├── question4.tif        # Input image for Q4–Q7
│   ├── Figure_1.png
│   └── Figure_2.png
├── Q5/
│   ├── Q5.py
│   └── Figure_1.png
├── Q6/
│   ├── Q6.py
│   └── Figure_1.png
├── Q7/
│   ├── Q7.py
│   └── Figure_1.png
└── README.md
```

## Requirements

- Python 3.8+
- NumPy
- Pillow (PIL)
- Matplotlib

Install dependencies:

```bash
pip install numpy pillow matplotlib
```

## How to Run

Each question is self-contained. Run any script from its own directory or from the project root:

```bash
# From the project root
python Q1/Q1.py
python Q2/Q2.py
python Q3/Q3.py
python Q4/Q4.py
python Q5/Q5.py
python Q6/Q6.py
python Q7/Q7.py
```

All file paths are relative, so the scripts work on any machine without modification.

## Results

Each script displays its output using Matplotlib. The rendered figures are also saved as `Figure_1.png` (and `Figure_2.png` where applicable) inside each question's folder.

## Implementation Notes

- All core operations (convolution, downsampling, histogram equalization) are implemented manually using NumPy — no `cv2` or `scipy` functions are used.
- Grayscale conversion uses the luminosity formula: `Y = 0.2989R + 0.5870G + 0.1140B`
- Q5 uses zero-padding before applying the mean filter to preserve image dimensions.
- Q6 uses a 4-neighbor Laplacian kernel and adds the result back to the original for sharpening.
