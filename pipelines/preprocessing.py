import cv2
import numpy as np

def process_uploaded_scan(uploaded_file):
    """
    Reads an uploaded image or DICOM file buffer and decodes it into a standard RGB matrix.
    """
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    if img is None:
        # Fallback to grayscale if color decoding fails
        img = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)
        if img is not None:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    return img

def apply_quality_gate(img, blur_threshold=100.0):
    """
    Applies a blur-based quality check using Laplacian variance.
    Returns (is_passed, variance_score).
    """
    if len(img.shape) == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    else:
        gray = img
    variance = cv2.Laplacian(gray, cv2.CV_64F).var()
    passed = bool(variance >= blur_threshold)
    return passed, variance

def preprocess_image(img, target_size=(224, 224)):
    """
    Standardizes image dimensions and scales pixel intensities from 0-255 to 0.0-1.0.
    """
    if len(img.shape) == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    else:
        gray = img
    resized = cv2.resize(gray, target_size)
    normalized = resized.astype(np.float32) / 255.0
    return np.expand_dims(normalized, axis=-1)  # Shape: (224, 224, 1)

def fuse_mri_modalities(t1_img, t2_img=None, flair_img=None, target_size=(224, 224)):
    """
    Fuses T1, T2, and FLAIR MRI sequences into a unified 3-channel normalized matrix (0.0 - 1.0)[cite: 5, 6].
    Falls back to duplicating the primary scan across channels if single-sequence input is provided.
    """
    def _prep_channel(im):
        if im is None:
            return None
        if len(im.shape) == 3:
            im = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
        resized = cv2.resize(im, target_size)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced = clahe.apply(resized.astype(np.uint8))
        return enhanced.astype(np.float32) / 255.0

    ch_t1 = _prep_channel(t1_img)
    if ch_t1 is None:
        ch_t1 = np.zeros(target_size, dtype=np.float32)
        
    ch_t2 = _prep_channel(t2_img) if t2_img is not None else ch_t1
    ch_flair = _prep_channel(flair_img) if flair_img is not None else ch_t1

    # Stack into a unified 3-channel tensor (H, W, 3)[cite: 5, 6]
    fused_tensor = np.stack([ch_t1, ch_t2, ch_flair], axis=-1)
    return np.expand_dims(fused_tensor, axis=0)  # Shape: (1, 224, 224, 3)