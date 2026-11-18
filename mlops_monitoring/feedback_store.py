import os
import csv
from datetime import datetime

FEEDBACK_LOG_PATH = "data/feedback_store.csv"

def initialize_feedback_store():
    """Initializes the CSV storage layer for active learning feedback loops."""
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(FEEDBACK_LOG_PATH):
        with open(FEEDBACK_LOG_PATH, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp", "PatientID", "PredictedLabel", "ClinicianValidatedLabel", "RiskTier", "ImageFilePath"])

def log_clinician_feedback(patient_id, predicted_label, validated_label, risk_tier, image_path):
    """
    Captures, structures, and saves clinician-confirmed validations 
    into a localized data layer to trigger automated background retraining intervals.
    """
    initialize_feedback_store()
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(FEEDBACK_LOG_PATH, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, patient_id, predicted_label, validated_label, risk_tier, image_path])
        
    return True