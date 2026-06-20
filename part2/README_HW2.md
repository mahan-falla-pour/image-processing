# Digital Image Processing — Homework 2

Implementation of color image processing techniques using NumPy and PIL.

## Topics Covered

| Question | Topic |
|----------|-------|
| Q1 | RGB and HSI color space decomposition |
| Q2 | Grayscale image colorization (two methods) |
| Q3 | PSNR calculation (manual vs OpenCV) |
| Q4 | Median filter for image reconstruction |
| Q5 | DCT quantization and Run-Length Coding (RLC) |

## Project Structure

```
HW2/
├── q1/
│   ├── image.jpg
│   ├── Red_Channel.png
│   ├── Green_Channel.png
│   ├── Blue_Channel.png
│   ├── Hue_Channel.png
│   ├── Saturation_Channel.png
│   └── Intensity_Channel.png
├── q2/
│   ├── grayscale.png
│   ├── ref1.jpg / ref2.jpg / ref3.jpg
│   ├── colorized_output.jpg
│   └── colorized2_hsi_output.jpg
├── q3/
│   ├── q3.jpg
│   └── q3_noisy.jpg
├── q4/
│   ├── 1.jpg / 2.jpg / 3.jpg
│   └── reconstructed_q4.jpg
├── q5/
├── Untitled.ipynb
└── README.md
```

## Requirements

- Python 3.8+
- NumPy
- Pillow (PIL)
- Matplotlib
- OpenCV

Install dependencies:

```bash
pip install numpy pillow matplotlib opencv-python
```

## How to Run

Open the notebook and run all cells in order:

```bash
jupyter notebook Untitled.ipynb
```

Or run cell by cell inside VS Code / JupyterLab.

## Implementation Notes

- **Q1**: RGB channels extracted manually; HSI conversion done with the standard trigonometric formula.
- **Q2**: Two colorization methods — intensity-based RGB lookup and HSI-based mapping.
- **Q3**: PSNR computed manually using MSE formula, verified against `cv2.PSNR`.
- **Q4**: Median filter implemented manually using NumPy patch extraction (no `cv2.medianBlur`).
- **Q5**: DCT coefficient matrix quantized with a custom Q-table, then encoded with zigzag scan and Run-Length Coding.
