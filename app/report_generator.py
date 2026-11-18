import os
import numpy as np
from fpdf import FPDF
from google import genai

def generate_genai_clinical_narrative(patient_id, pred_class, confidence, area_mm2, risk_tier):
    """
    Uses Google GenAI SDK to synthesize a structured radiological narrative summary[cite: 6].
    Falls back to a clinical template if no API key is configured.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    prompt = (
        f"Write a concise, professional 3-sentence radiological clinical summary for an MRI report. "
        f"Patient ID: {patient_id}, Classification: {pred_class}, Confidence: {confidence:.2f}%, "
        f"Estimated Tumor Area: {area_mm2:.1f} sq mm, Risk Tier: {risk_tier}. "
        f"Maintain formal medical tone suitable for secondary clinician decision support."
    )

    if api_key:
        try:
            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            if response and response.text:
                return response.text.strip()
        except Exception:
            pass

    return (
        f"Automated multi-sequence MRI evaluation for Patient {patient_id} indicates findings consistent with "
        f"{pred_class} (model confidence: {confidence:.2f}%). Volumetric boundary estimation measures an anomaly "
        f"cross-sectional area of {area_mm2:.1f} sq mm, categorized under {risk_tier}. "
        f"Correlation with clinical history and formal radiologist sign-off is recommended prior to intervention."
    )

class MedicalPDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'BRAIN TUMOR DIAGNOSTIC & MLOPS CLINICAL REPORT', 0, 1, 'C')
        self.set_font('Arial', 'I', 9)
        self.cell(0, 6, 'Generated via Automated Medical AI & MLOps Pipeline', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()} | Confidential Medical Document', 0, 0, 'C')

def generate_pdf_report(patient_id, scan_type, pred_class, confidence, area_mm2, risk_tier, image_path=None):
    pdf = MedicalPDFReport()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # 1. Metadata
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 8, '1. Patient Metadata & Scan Information', 0, 1)
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 6, f'Patient ID: {patient_id}', 0, 1)
    pdf.cell(0, 6, f'Modality / Scan Type: {scan_type}', 0, 1)
    pdf.ln(4)

    # 2. AI Diagnostics & Narrative Summary
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 8, '2. Deep Learning Classification & Risk Analysis', 0, 1)
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 6, f'Primary Prediction Class: {pred_class}', 0, 1)
    pdf.cell(0, 6, f'Confidence Score: {confidence:.2f}%', 0, 1)
    pdf.cell(0, 6, f'Estimated Tumor Area: {area_mm2:.1f} sq mm', 0, 1)
    pdf.cell(0, 6, f'Malignancy Risk Tier: {risk_tier}', 0, 1)
    pdf.ln(4)

    # GenAI / Clinical Narrative Section
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 8, '3. Automated Clinical Narrative Summary', 0, 1)
    pdf.set_font('Arial', '', 10)
    narrative = generate_genai_clinical_narrative(patient_id, pred_class, confidence, area_mm2, risk_tier)
    pdf.multi_cell(0, 6, narrative)
    pdf.ln(6)

    # 4. Source Scan Visual Matrix
    if image_path and os.path.exists(image_path):
        pdf.set_font('Arial', 'B', 11)
        pdf.cell(0, 8, '4. Source Scan Visual Matrix', 0, 1)
        try:
            pdf.image(image_path, x=65, w=80)
        except Exception:
            pdf.cell(0, 6, '[Visual Matrix rendering error]', 0, 1)
        pdf.ln(6)

    # Disclaimer
    pdf.set_font('Arial', 'I', 8)
    pdf.multi_cell(0, 5, 'DISCLAIMER: This document is synthesized by an automated AI computer-aided diagnostic pipeline intended for secondary clinician support. Final medical diagnosis and treatment plans must be validated by a certified radiologist or oncologist.')

    output_filename = f"Report_{patient_id}.pdf"
    pdf.output(output_filename)
    return output_filename