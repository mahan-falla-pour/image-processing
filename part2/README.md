# Digital Image Processing — Homework 2

Implementation of color image processing, noise reduction, and compression techniques using NumPy and PIL.

## Topics Covered

| Question | Topic |
|----------|-------|
| Q1 | RGB and HSI color space decomposition |
| Q2 | Grayscale image colorization using reference images (two methods) |
| Q3 | PSNR calculation from scratch (manual vs `cv2.PSNR` verification) |
| Q4 | Noise type identification, median filter reconstruction, and PSNR evaluation |
| Q5 | JPEG compression steps: DCT quantization, zig-zag scan, and Run-Length Coding (RLC) |

## Project Structure

```
part2/
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
├── HW2.pdf
├── Report.pdf
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

## Implementation Notes

- **Q1**: RGB channels extracted manually; HSI conversion uses the standard trigonometric formula.
- **Q2**: Two colorization methods — intensity-based RGB lookup and HSI-based mapping using three reference images.
- **Q3**: PSNR computed manually using the MSE formula `PSNR = 10 * log10(255² / MSE)`, then verified against `cv2.PSNR`.
- **Q4**: Noise type identified visually; median filter implemented manually using NumPy patch extraction (no `cv2.medianBlur`); PSNR evaluated using the Q3 function.
- **Q5**: Manual JPEG compression pipeline on a 4×4 DCT block — quantization with a custom Q-matrix, zig-zag scan, and Run-Length Coding (RLC).
