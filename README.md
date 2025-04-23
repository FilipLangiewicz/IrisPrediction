# Iris Recognition System 🧿

This project implements a complete iris recognition pipeline using classical image processing techniques. The goal is to extract and encode unique iris features from an eye image and generate a binary iris code for biometric identification.

## 🔍 Project Overview

The notebook contains a comprehensive pipeline for iris image analysis, including:

- Grayscale conversion and binarization  
- Pupil and iris boundary detection  
- Iris normalization through unwrapping  
- Feature extraction using Gabor-like transformations  
- Generation of a unique **iris code**  
- Visualization of all steps and intermediate results  

## ⚙️ How It Works

The main function is:

```python
predictIris(path, f=np.pi, save=False, output_width=128, sigma=4.42)
```

It processes an iris image from the given `path` and returns the binary iris code.

### Key Parameters:

- `f`: Frequency parameter for feature extraction  
- `output_width`: Width of the unwrapped iris  
- `sigma`: Gaussian sigma for smoothing  
- `save`: Whether to save processed images   

## 📦 Dependencies

Install the required packages using pip:

```bash
pip install numpy pillow matplotlib opencv-python scikit-learn imageio
```

## 🖼 Example

Example usage:

```python
code = predictIris("sample_eye_image.jpg", f=np.pi)
```

You'll see visualization of:

- Detected pupil and iris  
- Unwrapped iris image  
- Segmented feature bands  
- Final iris code  

## 📁 File Structure

```
main.ipynb                 # Full iris recognition pipeline
sample_eye_image.jpg       # (optional) Your test image
```

## 📌 Notes

- The system uses traditional computer vision techniques (no deep learning involved).  
- High-quality eye images with clearly visible iris patterns are recommended for best results.

## 🧪 Future Improvements

- Automate image quality checks  
- Add iris code comparison/matching system  
- Explore CNN-based iris encoding for benchmarking  
