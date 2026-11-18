import os
import pydicom
import numpy as np
import cv2

def load_dicom_scan(file_path):
    """
    Ingests raw DICOM medical imaging files (.dcm) and converts them 
    into a normalized multi-dimensional pixel array.
    """
    try:
        # Read DICOM file using pydicom
        dicom_data = pydicom.dcmread(file_path)
        
        # Extract pixel data matrix
        image_matrix = dicom_data.pixel_array.astype(np.float32)
        
        # Normalize pixel values to 0-255 range for image processing
        if np.max(image_matrix) != 0:
            image_matrix = cv2.normalize(image_matrix, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
            
        image_matrix = np.uint8(image_matrix)
        
        # Extract useful DICOM metadata if available
        metadata = {
            "PatientID": getattr(dicom_data, 'PatientID', 'Unknown'),
            "Modality": getattr(dicom_data, 'Modality', 'MRI'),
            "StudyDescription": getattr(dicom_data, 'StudyDescription', 'Brain Scan')
        }
        
        return image_matrix, metadata
    
    except Exception as e:
        print(f"Error loading DICOM file {file_path}: {e}")
        return None, None

def process_uploaded_scan(uploaded_file_path):
    """
    Handles general image formats (PNG/JPG) or routes DICOM files 
    through the ingestion quality gate.
    """
    if uploaded_file_path.endswith('.dcm'):
        return load_dicom_scan(uploaded_file_path)
    else:
        # Fallback for standard image uploads during testing
        img = cv2.imread(uploaded_file_path, cv2.IMREAD_GRAYSCALE)
        return img, {"PatientID": "Test_Patient", "Modality": "MRI", "StudyDescription": "Standard Upload"}