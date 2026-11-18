import cv2
import numpy as np

def extract_tumor_dimensions(image, prediction_confidence):
    """
    Computes spatial area and maximum cross-sectional pixel boundaries 
    of the detected anomaly to estimate tumor dimensions and risk tier.
    """
    # Convert to grayscale if necessary
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) if len(image.shape) == 3 else image
    
    # Thresholding to isolate high-intensity anomaly regions
    _, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
    
    # Find contours of the tumor region
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    max_area_pixels = 0
    bounding_box = (0, 0, 0, 0)
    
    if contours:
        # Find the largest contour which likely corresponds to the tumor mass
        largest_contour = max(contours, key=cv2.contourArea)
        max_area_pixels = cv2.contourArea(largest_contour)
        bounding_box = cv2.boundingRect(largest_contour) # (x, y, w, h)
        
    # Estimate real-world scaling approximation (e.g., standard MRI voxel conversion factor ~0.2 mm/pixel)
    voxel_scale_mm2 = 0.04  # sq mm per pixel approximation
    estimated_area_mm2 = max_area_pixels * voxel_scale_mm2
    
    # Determine Malignancy Risk Tier based on area and confidence metrics
    if max_area_pixels < 50 or prediction_confidence < 0.50:
        risk_tier = "Low Risk / Benign Indicator"
    elif max_area_pixels < 300:
        risk_tier = "Moderate Risk / Intermediate Anomaly"
    else:
        risk_tier = "High Risk / Critical Malignancy Threshold"
        
    measurement_results = {
        "pixel_area": float(max_area_pixels),
        "estimated_area_mm2": round(estimated_area_mm2, 2),
        "bounding_box": bounding_box,
        "risk_tier": risk_tier
    }
    
    return measurement_results