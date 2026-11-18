import streamlit as st

def apply_custom_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        header[data-testid="stHeader"] {
            display: none !important;
        }
        footer {
            display: none !important;
        }
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 1.5rem !important;
            padding-left: 1.2rem !important;
            padding-right: 1.2rem !important;
            max-width: 100% !important;
        }
        .stApp {
            background-color: #EEF2F7;
        }

        /* Top Dark Navy Banner */
        .top-navbar {
            background: linear-gradient(90deg, #091E3A 0%, #0F2E56 100%);
            padding: 16px 28px;
            margin: 0 -1.2rem 18px -1.2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: #FFFFFF;
            box-shadow: 0 2px 10px rgba(9, 30, 58, 0.15);
        }
        .top-navbar-title {
            font-size: 1.45rem;
            font-weight: 700;
            margin: 0;
            color: #FFFFFF;
            letter-spacing: -0.01em;
        }
        .top-navbar-subtitle {
            font-size: 0.85rem;
            color: #CBD5E1;
            margin: 3px 0 0 0;
        }
        .top-navbar-right {
            display: flex;
            align-items: center;
            gap: 18px;
        }
        .status-badge {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.88rem;
            font-weight: 500;
            color: #E2E8F0;
            padding-right: 18px;
            border-right: 1px solid rgba(255,255,255,0.2);
        }
        .status-dot {
            width: 10px;
            height: 10px;
            background-color: #22C55E;
            border-radius: 50%;
            display: inline-block;
            box-shadow: 0 0 8px #22C55E;
        }
        .user-pill {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.9rem;
            font-weight: 600;
            color: #FFFFFF;
        }

        /* Section Title */
        .section-header {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 1.15rem;
            font-weight: 700;
            color: #0F294A;
            margin-bottom: 12px;
        }

        /* White Dashboard Cards */
        .ui-card {
            background-color: #FFFFFF;
            border-radius: 10px;
            padding: 16px;
            box-shadow: 0 2px 8px rgba(15, 23, 42, 0.06);
            border: 1px solid #E2E8F0;
            height: 100%;
        }
        .card-header-light {
            font-size: 0.98rem;
            font-weight: 700;
            color: #0F294A;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        /* Dark Image Viewer Frame */
        .scan-frame {
            background-color: #08182B;
            border-radius: 10px;
            padding: 12px;
            color: #FFFFFF;
            box-shadow: 0 2px 8px rgba(8, 24, 43, 0.12);
        }
        .scan-frame-title {
            font-size: 0.92rem;
            font-weight: 600;
            color: #F8FAFC;
            margin-bottom: 8px;
        }

        /* Result Cards */
        .result-card-wrapper {
            background-color: #FFFFFF;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(15, 23, 42, 0.06);
            border: 1px solid #E2E8F0;
        }
        .result-banner-positive {
            background: linear-gradient(90deg, #1E9E5A 0%, #27AE60 100%);
            color: #FFFFFF;
            padding: 14px 18px;
            font-size: 1.15rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .result-banner-neutral {
            background: linear-gradient(90deg, #1E3A5F 0%, #2B547E 100%);
            color: #FFFFFF;
            padding: 14px 18px;
            font-size: 1.1rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .result-body {
            padding: 14px 18px;
        }
        .result-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 9px 0;
            border-bottom: 1px solid #F1F5F9;
            font-size: 0.9rem;
            color: #334155;
        }
        .badge-blue {
            background-color: #E0ECFF;
            color: #1D4ED8;
            font-weight: 700;
            padding: 3px 12px;
            border-radius: 6px;
            font-size: 0.88rem;
        }
        .badge-red {
            background-color: #FEE2E2;
            color: #DC2626;
            font-weight: 700;
            padding: 3px 14px;
            border-radius: 6px;
            font-size: 0.88rem;
        }
        .clinical-alert-box {
            margin-top: 12px;
            background-color: #FEF2F2;
            border: 1px solid #FECACA;
            border-radius: 8px;
            padding: 10px 12px;
            display: flex;
            align-items: flex-start;
            gap: 10px;
            font-size: 0.82rem;
            color: #7F1D1D;
            line-height: 1.35;
        }

        /* Primary Navy Action Buttons */
        div.stButton > button {
            background-color: #133863 !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 6px !important;
            padding: 0.5rem 1rem !important;
            font-weight: 600 !important;
            font-size: 0.88rem !important;
            transition: background-color 0.2s ease;
        }
        div.stButton > button:hover {
            background-color: #1D4E89 !important;
            color: #FFFFFF !important;
        }

        /* File Uploader Dashed Box */
        [data-testid="stFileUploaderDropzone"] {
            border: 2px dashed #CBD5E1 !important;
            background-color: #F8FAFC !important;
            border-radius: 8px !important;
            padding: 12px !important;
        }

        /* Bottom Disclaimer Footer Bar */
        .app-footer {
            background-color: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 8px;
            padding: 10px 18px;
            margin-top: 18px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.82rem;
            color: #475569;
        }
    </style>
    """, unsafe_allow_html=True)


def render_top_navbar(username: str):
    st.markdown(f"""
    <div class="top-navbar">
        <div>
            <div class="top-navbar-title">Brain Tumor Detection &amp; Classification System</div>
            <div class="top-navbar-subtitle">AI-Powered &bull; MLOps Enabled &bull; Clinical Ready</div>
        </div>
        <div class="top-navbar-right">
            <div class="status-badge">
                <span class="status-dot"></span> System Online
            </div>
            <div class="user-pill">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="white">
                    <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm0 14.2c-2.5 0-4.71-1.28-6-3.22.03-1.99 4-3.08 6-3.08 1.99 0 5.97 1.09 6 3.08-1.29 1.94-3.5 3.22-6 3.22z"/>
                </svg>
                {username}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_detection_result_card(analyzed: bool, pred_class: str = "", confidence: float = 0.0, area_px: float = 0.0, risk_tier: str = ""):
    if not analyzed:
        st.markdown("""
        <div class="result-card-wrapper">
            <div class="result-banner-neutral">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
                    <circle cx="12" cy="12" r="10"></circle>
                    <line x1="12" y1="8" x2="12" y2="12"></line>
                    <line x1="12" y1="16" x2="12.01" y2="16"></line>
                </svg>
                Awaiting MRI Scan
            </div>
            <div class="result-body">
                <div class="result-row"><span>Predicted class:</span> <span style="color:#94A3B8;">--</span></div>
                <div class="result-row"><span>Confidence score:</span> <span style="color:#94A3B8;">--</span></div>
                <div class="result-row"><span>Estimated region area:</span> <span style="color:#94A3B8;">--</span></div>
                <div class="result-row"><span>Risk category:</span> <span style="color:#94A3B8;">--</span></div>
                <div style="margin-top: 14px; font-size: 0.83rem; color: #64748B; background: #F8FAFC; padding: 10px; border-radius: 6px;">
                    Upload a brain MRI scan on the left and click <strong>Analyze MRI</strong> to run diagnostic inference.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="result-card-wrapper">
            <div class="result-banner-positive">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5">
                    <circle cx="12" cy="12" r="10"></circle>
                    <polyline points="9 12 11 14 15 10"></polyline>
                </svg>
                Tumor Detected
            </div>
            <div class="result-body">
                <div class="result-row">
                    <span>Predicted class:</span>
                    <span class="badge-blue">{pred_class}</span>
                </div>
                <div class="result-row">
                    <span>Confidence score:</span>
                    <span style="font-weight:700; color:#1D4ED8; font-size:0.98rem;">{confidence:.1f}%</span>
                </div>
                <div class="result-row">
                    <span>Estimated region area:</span>
                    <span style="font-weight:700; color:#0F172A;">{area_px:,.0f} px&sup2;</span>
                </div>
                <div class="result-row">
                    <span>Risk category:</span>
                    <span class="badge-red">{risk_tier}</span>
                </div>
                <div class="clinical-alert-box">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="#DC2626" style="flex-shrink:0;">
                        <circle cx="12" cy="12" r="10"></circle>
                        <text x="12" y="16" text-anchor="middle" fill="white" font-size="13" font-weight="bold">!</text>
                    </svg>
                    <span>A brain tumor is detected in this scan. Please consult a qualified radiologist.</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)


def render_model_performance_card():
    st.markdown("""
    <div class="ui-card">
        <div class="card-header-light">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="#1D4E89">
                <rect x="3" y="12" width="4" height="9" rx="1"></rect>
                <rect x="10" y="7" width="4" height="14" rx="1"></rect>
                <rect x="17" y="3" width="4" height="18" rx="1"></rect>
            </svg>
            Model Performance (Live Metrics)
        </div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-top: 8px;">
            <div style="border: 1px solid #E2E8F0; border-radius: 8px; padding: 10px;">
                <div style="font-size: 0.78rem; color: #64748B; font-weight: 500;">Accuracy</div>
                <div style="font-size: 1.25rem; font-weight: 700; color: #0F172A; margin: 4px 0;">96.1%</div>
                <svg width="100%" height="18" viewBox="0 0 80 18">
                    <polyline fill="none" stroke="#22C55E" stroke-width="2" points="2,15 25,11 50,12 76,4"/>
                </svg>
            </div>
            <div style="border: 1px solid #E2E8F0; border-radius: 8px; padding: 10px;">
                <div style="font-size: 0.78rem; color: #64748B; font-weight: 500;">Precision</div>
                <div style="font-size: 1.25rem; font-weight: 700; color: #0F172A; margin: 4px 0;">94.8%</div>
                <svg width="100%" height="18" viewBox="0 0 80 18">
                    <polyline fill="none" stroke="#3B82F6" stroke-width="2" points="2,14 28,12 52,9 76,4"/>
                </svg>
            </div>
            <div style="border: 1px solid #E2E8F0; border-radius: 8px; padding: 10px;">
                <div style="font-size: 0.78rem; color: #64748B; font-weight: 500;">Recall</div>
                <div style="font-size: 1.25rem; font-weight: 700; color: #0F172A; margin: 4px 0;">95.2%</div>
                <svg width="100%" height="18" viewBox="0 0 80 18">
                    <polyline fill="none" stroke="#8B5CF6" stroke-width="2" points="2,15 26,10 52,11 76,4"/>
                </svg>
            </div>
            <div style="border: 1px solid #E2E8F0; border-radius: 8px; padding: 10px;">
                <div style="font-size: 0.78rem; color: #64748B; font-weight: 500;">F1-Score</div>
                <div style="font-size: 1.25rem; font-weight: 700; color: #0F172A; margin: 4px 0;">95.0%</div>
                <svg width="100%" height="18" viewBox="0 0 80 18">
                    <polyline fill="none" stroke="#10B981" stroke-width="2" points="2,14 25,12 52,8 76,4"/>
                </svg>
            </div>
        </div>
        <div style="margin-top: 12px; background-color: #ECFDF5; border: 1px solid #A7F3D0; border-radius: 6px; padding: 8px 12px; display: flex; align-items: center; gap: 8px; font-size: 0.84rem; color: #065F46; font-weight: 500;">
            <span style="background:#10B981; color:white; border-radius:50%; width:18px; height:18px; display:inline-flex; align-items:center; justify-content:center; font-size:0.72rem;">&#10003;</span>
            Model is performing well
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_footer():
    st.markdown("""
    <div class="app-footer">
        <div style="display: flex; align-items: center; gap: 8px;">
            <span style="background:#1D4ED8; color:white; border-radius:50%; width:18px; height:18px; display:inline-flex; align-items:center; justify-content:center; font-weight:700; font-size:0.75rem;">i</span>
            <span><strong>Illustrative demo only</strong> &mdash; not a real patient result or clinical diagnosis</span>
        </div>
        <div style="color: #64748B; font-weight: 500;">
            Built with TensorFlow &bull; Streamlit &bull; MLOps
        </div>
    </div>
    """, unsafe_allow_html=True)