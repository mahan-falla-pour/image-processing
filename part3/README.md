# Digital Image Processing — Homework 3

Implementation of morphological operations, image segmentation, and cell analysis using NumPy — all core algorithms implemented from scratch.

## Topics Covered

| Question | Topic |
|----------|-------|
| Q1 | Object boundary extraction via morphological erosion |
| Q2 | Image segmentation using Otsu's thresholding, connected component labeling, and region merging |
| Q3 | Cell detection, counting, and feature extraction from microscopy images |

## Project Structure

```
part3/
├── Cells.png               # Input microscopy image for Q3
├── cells_data.csv          # Output: per-cell area and mean intensity
├── HW_3.pdf                # Assignment description
├── Untitled.ipynb          # Solutions notebook
├── Report.pdf              # Written report
└── README.md
```

## Requirements

- Python 3.8+
- NumPy
- Matplotlib
- OpenCV (`cv2.imread`, `cv2.cvtColor` only)
- openpyxl or pandas (for Excel/CSV output in Q3)

Install dependencies:

```bash
pip install numpy matplotlib opencv-python openpyxl pandas
```

## How to Run

```bash
jupyter notebook Untitled.ipynb
```

## Implementation Notes

- **Q1**: Erosion implemented manually using a sliding structuring element window. Boundary extracted via `Boundary = A - (A ⊖ B)`. Number of boundary components counted using a custom flood-fill (BFS).
- **Q2**: Otsu's threshold computed manually by maximizing between-class variance `σ²_B(T) = w₀(T)·w₁(T)·[μ₀(T) - μ₁(T)]²`. Connected component labeling implemented with BFS (no `scipy.ndimage.label` or `bwlabel`). Region merging applied when neighboring region mean intensities differ by less than a specified threshold.
- **Q3**: Cells detected and labeled using a custom BFS-based connected component algorithm. For each detected cell `k`: `Area_k = Σ pixels`, `Mean Intensity_k = (1/Area_k) Σ I(pixel)`. Results saved to `cells_data.csv`. Total detected: **149 cells**.
