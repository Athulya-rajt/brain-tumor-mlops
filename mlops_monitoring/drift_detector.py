import numpy as np
from scipy.stats import ks_2samp

def check_data_drift(baseline_features, incoming_features, threshold=0.05):
    """
    Calculates real-time input data distribution statistics against 
    baseline training partitions using the Kolmogorov-Smirnov test.
    Triggers automated alert flags if statistical drift occurs.
    """
    if baseline_features is None or incoming_features is None:
        return False, "Insufficient data for drift calculation."
    
    # Flatten arrays for statistical comparison
    baseline_flat = np.array(baseline_features).flatten()
    incoming_flat = np.array(incoming_features).flatten()
    
    # Perform Kolmogorov-Smirnov test
    ks_stat, p_value = ks_2samp(baseline_flat, incoming_flat)
    
    # If p_value is below threshold, data distribution has drifted significantly
    is_drift_detected = p_value < threshold
    
    status_message = (
        f"Data Drift Alert Triggered! (p-value: {p_value:.5f})" 
        if is_drift_detected 
        else f"Data Distribution Stable (p-value: {p_value:.5f})"
    )
    
    return is_drift_detected, status_message