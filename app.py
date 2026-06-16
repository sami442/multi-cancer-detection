import streamlit as st
import numpy as np
import pickle
import requests
from io import BytesIO

# Page config
st.set_page_config(
    page_title="Multi-Cancer Detection AI",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, 
            #0a0a1a 0%, #0d1b2a 50%, #0a0a1a 100%);
        color: white;
    }
    .metric-card {
        background: linear-gradient(135deg, 
            #1a1a2e, #16213e);
        border: 1px solid #00d2ff33;
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
    }
    .section-title {
        color: #00d2ff;
        font-size: 1.3rem;
        font-weight: 700;
        border-left: 3px solid #7b2ff7;
        padding-left: 0.8rem;
        margin-bottom: 1rem;
    }
    .result-positive {
        background: #ff000022;
        border: 1px solid #ff000055;
        border-radius: 10px;
        padding: 1rem;
        color: #ff6b6b;
        text-align: center;
        font-size: 1.2rem;
        font-weight: 700;
    }
    .result-negative {
        background: #00ff0022;
        border: 1px solid #00ff0055;
        border-radius: 10px;
        padding: 1rem;
        color: #6bff6b;
        text-align: center;
        font-size: 1.2rem;
        font-weight: 700;
    }
    .divider {
        height: 2px;
        background: linear-gradient(90deg, 
            #00d2ff, #7b2ff7);
        border: none;
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div style='text-align: center; padding: 2rem 0;'>
    <p style='font-size: 3rem; font-weight: 800;
    background: linear-gradient(90deg, #00d2ff, #7b2ff7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;'>🏥 Multi-Cancer Detection AI</p>
    <p style='color: #8892b0; font-size: 1.1rem;'>
    AI-powered detection for Breast & Ovarian Cancer
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='divider'></div>",
    unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style='text-align: center;'>
        <p style='font-size: 1.3rem; font-weight: 700;
        background: linear-gradient(90deg, #00d2ff, #7b2ff7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;'>
        🏥 Cancer Detection AI</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div style='background: linear-gradient(135deg, 
        #1a1a2e, #16213e);
        border: 1px solid #00d2ff33;
        border-radius: 10px; padding: 1rem;'>
        <p style='color: #00d2ff; font-weight: 600;'>
        📊 Model Performance</p>
        <p style='color: #ccd6f6;'>
        🎗️ Breast Cancer: <b>98.25%</b></p>
        <p style='color: #ccd6f6;'>
        🔬 Ovarian Cancer: <b>87.50%</b></p>
        <p style='color: #ccd6f6;'>
        🧠 Brain Tumor: <b>99.37%</b></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div style='background: linear-gradient(135deg,
        #1a1a2e, #16213e);
        border: 1px solid #7b2ff733;
        border-radius: 10px; padding: 1rem;'>
        <p style='color: #7b2ff7; font-weight: 600;'>
        👩‍💻 Developer</p>
        <p style='color: #ccd6f6;'><b>Samina Mazhar</b></p>
        <p style='color: #8892b0;'>BS Artificial Intelligence</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div style='text-align: center;'>
        <a href='https://github.com/sami442'
        style='color: #00d2ff;'>🐙 GitHub</a>
        &nbsp;|&nbsp;
        <a href='https://huggingface.co/mazharsamina26'
        style='color: #7b2ff7;'>🤗 HuggingFace</a>
    </div>
    """, unsafe_allow_html=True)

# Load Models
@st.cache_resource
def load_models():
    try:
        with open('models/breast_cancer_model.pkl', 'rb') as f:
            breast_model = pickle.load(f)
        with open('models/breast_cancer_scaler.pkl', 'rb') as f:
            breast_scaler = pickle.load(f)
        with open('models/ovarian_cancer_model.pkl', 'rb') as f:
            ovarian_model = pickle.load(f)
        with open('models/ovarian_cancer_scaler.pkl', 'rb') as f:
            ovarian_scaler = pickle.load(f)
        return breast_model, breast_scaler, \
               ovarian_model, ovarian_scaler, True
    except Exception as e:
        st.sidebar.error(f"Error: {e}")
        return None, None, None, None, False

breast_model, breast_scaler, \
ovarian_model, ovarian_scaler, \
models_loaded = load_models()

if models_loaded:
    st.sidebar.markdown("""
    <div style='background: #00ff0011;
    border: 1px solid #00ff0055;
    border-radius: 8px; padding: 0.5rem;
    text-align: center; color: #6bff6b;
    margin-top: 1rem;'>
    ✅ All Models Ready
    </div>""", unsafe_allow_html=True)
else:
    st.sidebar.warning("⚠️ Models not found!")

# Cancer Type Selection
st.markdown("""
<p class='section-title'>🔬 Select Cancer Type</p>
""", unsafe_allow_html=True)

cancer_type = st.radio(
    "",
    ["🎗️ Breast Cancer Detection",
     "🔬 Ovarian Cancer Detection",
     "🧠 Brain Tumor Detection"],
    horizontal=True
)

st.markdown("<div class='divider'></div>",
    unsafe_allow_html=True)

# Breast Cancer Detection
if cancer_type == "🎗️ Breast Cancer Detection":
    st.markdown("""
    <p class='section-title'>
    🎗️ Breast Cancer Detection</p>
    <p style='color: #8892b0;'>
    Enter cell nucleus measurements from
    fine needle aspirate (FNA) of breast mass.
    </p>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        mean_radius = st.number_input(
            'Mean Radius', 0.0, 30.0, 14.0)
        mean_texture = st.number_input(
            'Mean Texture', 0.0, 40.0, 19.0)
        mean_perimeter = st.number_input(
            'Mean Perimeter', 0.0, 200.0, 92.0)
        mean_area = st.number_input(
            'Mean Area', 0.0, 2500.0, 655.0)
        mean_smoothness = st.number_input(
            'Mean Smoothness', 0.0, 0.2, 0.096)
        mean_compactness = st.number_input(
            'Mean Compactness', 0.0, 0.4, 0.104)
        mean_concavity = st.number_input(
            'Mean Concavity', 0.0, 0.5, 0.089)
        mean_concave_points = st.number_input(
            'Mean Concave Points', 0.0, 0.2, 0.049)
        mean_symmetry = st.number_input(
            'Mean Symmetry', 0.0, 0.4, 0.181)
        mean_fractal = st.number_input(
            'Mean Fractal Dimension', 0.0, 0.1, 0.063)

    with col2:
        se_radius = st.number_input(
            'SE Radius', 0.0, 3.0, 0.405)
        se_texture = st.number_input(
            'SE Texture', 0.0, 5.0, 1.217)
        se_perimeter = st.number_input(
            'SE Perimeter', 0.0, 22.0, 2.866)
        se_area = st.number_input(
            'SE Area', 0.0, 550.0, 40.34)
        se_smoothness = st.number_input(
            'SE Smoothness', 0.0, 0.04, 0.007)
        se_compactness = st.number_input(
            'SE Compactness', 0.0, 0.15, 0.025)
        se_concavity = st.number_input(
            'SE Concavity', 0.0, 0.4, 0.032)
        se_concave_points = st.number_input(
            'SE Concave Points', 0.0, 0.06, 0.012)
        se_symmetry = st.number_input(
            'SE Symmetry', 0.0, 0.08, 0.020)
        se_fractal = st.number_input(
            'SE Fractal', 0.0, 0.03, 0.004)

    with col3:
        worst_radius = st.number_input(
            'Worst Radius', 0.0, 40.0, 16.27)
        worst_texture = st.number_input(
            'Worst Texture', 0.0, 50.0, 25.68)
        worst_perimeter = st.number_input(
            'Worst Perimeter', 0.0, 260.0, 107.26)
        worst_area = st.number_input(
            'Worst Area', 0.0, 4300.0, 880.58)
        worst_smoothness = st.number_input(
            'Worst Smoothness', 0.0, 0.3, 0.132)
        worst_compactness = st.number_input(
            'Worst Compactness', 0.0, 1.1, 0.254)
        worst_concavity = st.number_input(
            'Worst Concavity', 0.0, 1.3, 0.272)
        worst_concave_points = st.number_input(
            'Worst Concave Points', 0.0, 0.3, 0.115)
        worst_symmetry = st.number_input(
            'Worst Symmetry', 0.0, 0.7, 0.290)
        worst_fractal = st.number_input(
            'Worst Fractal', 0.0, 0.3, 0.084)

    if st.button('🔍 Analyze for Breast Cancer',
                 use_container_width=True):
        if models_loaded:
            features = np.array([[
                mean_radius, mean_texture,
                mean_perimeter, mean_area,
                mean_smoothness, mean_compactness,
                mean_concavity, mean_concave_points,
                mean_symmetry, mean_fractal,
                se_radius, se_texture,
                se_perimeter, se_area,
                se_smoothness, se_compactness,
                se_concavity, se_concave_points,
                se_symmetry, se_fractal,
                worst_radius, worst_texture,
                worst_perimeter, worst_area,
                worst_smoothness, worst_compactness,
                worst_concavity, worst_concave_points,
                worst_symmetry, worst_fractal
            ]])

            scaled = breast_scaler.transform(features)
            prediction = breast_model.predict(scaled)
            probability = breast_model.predict_proba(
                scaled)[0]

            st.markdown("<br>", unsafe_allow_html=True)

            if prediction[0] == 0:
                st.markdown(f"""
                <div class='result-positive'>
                ⚠️ MALIGNANT DETECTED<br>
                <span style='font-size: 1.5rem;'>
                Confidence: {probability[0]*100:.1f}%
                </span>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class='result-negative'>
                ✅ BENIGN - No Cancer Detected<br>
                <span style='font-size: 1.5rem;'>
                Confidence: {probability[1]*100:.1f}%
                </span>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("""
            <div style='background: #ffffff11;
            border-radius: 8px; padding: 0.8rem;
            color: #8892b0; font-size: 0.85rem;
            margin-top: 1rem;'>
            ⚕️ <b>Disclaimer:</b> For research only.
            Consult a medical professional.
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("❌ Models not loaded!")

# Ovarian Cancer Detection
elif cancer_type == "🔬 Ovarian Cancer Detection":
    st.markdown("""
    <p class='section-title'>
    🔬 Ovarian Cancer Detection</p>
    <p style='color: #8892b0;'>
    Enter patient biomarker values for analysis.
    </p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input('Age', 20, 100, 50)
        bmi = st.number_input('BMI', 10.0, 50.0, 23.0)
        glucose = st.number_input(
            'Glucose (mg/dL)', 50.0, 200.0, 92.0)
        leptin = st.number_input(
            'Leptin (ng/mL)', 0.0, 100.0, 20.0)
        adiponectin = st.number_input(
            'Adiponectin (μg/mL)', 0.0, 50.0, 10.0)

    with col2:
        insulin = st.number_input(
            'Insulin (μU/mL)', 0.0, 60.0, 10.0)
        homa = st.number_input(
            'HOMA Index', 0.0, 30.0, 2.0)
        resistin = st.number_input(
            'Resistin (ng/mL)', 0.0, 100.0, 15.0)
        mcp1 = st.number_input(
            'MCP-1 (pg/dL)', 0.0, 2000.0, 500.0)

    if st.button('🔍 Analyze for Ovarian Cancer',
                 use_container_width=True):
        if models_loaded:
            features = np.array([[
                age, bmi, glucose, insulin,
                homa, leptin, adiponectin,
                resistin, mcp1
            ]])

            scaled = ovarian_scaler.transform(features)
            prediction = ovarian_model.predict(scaled)
            probability = ovarian_model.predict_proba(
                scaled)[0]

            st.markdown("<br>", unsafe_allow_html=True)

            if prediction[0] == 1:
                st.markdown(f"""
                <div class='result-positive'>
                ⚠️ CANCER INDICATORS DETECTED<br>
                <span style='font-size: 1.5rem;'>
                Confidence: {probability[1]*100:.1f}%
                </span>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class='result-negative'>
                ✅ NO CANCER INDICATORS<br>
                <span style='font-size: 1.5rem;'>
                Confidence: {probability[0]*100:.1f}%
                </span>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("""
            <div style='background: #ffffff11;
            border-radius: 8px; padding: 0.8rem;
            color: #8892b0; font-size: 0.85rem;
            margin-top: 1rem;'>
            ⚕️ <b>Disclaimer:</b> For research only.
            Consult a medical professional.
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("❌ Models not loaded!")

# Brain Tumor Detection
elif cancer_type == "🧠 Brain Tumor Detection":
    st.markdown("""
    <p class='section-title'>
    🧠 Brain Tumor Detection</p>
    <p style='color: #8892b0;'>
    Upload a brain MRI scan for tumor segmentation.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='background: linear-gradient(135deg,
        #1a1a2e, #16213e);
        border: 1px solid #00d2ff33;
        border-radius: 15px; padding: 2rem;
        text-align: center;'>
        <p style='color: #00d2ff; font-size: 1.2rem;
        font-weight: 600;'>
        🧠 Brain Tumor Segmentation</p>
        <p style='color: #8892b0;'>
        This feature uses our dedicated U-Net model
        with 99.37% accuracy</p>
        <a href='https://medical-image-segmentation-jc6hrzsdhjimse9d47n5uz.streamlit.app/'
        target='_blank'
        style='background: linear-gradient(90deg,
        #00d2ff, #7b2ff7);
        color: white; padding: 0.8rem 2rem;
        border-radius: 25px; text-decoration: none;
        font-weight: 600; display: inline-block;
        margin-top: 1rem;'>
        🚀 Open Brain Tumor App
        </a>
    </div>
    """, unsafe_allow_html=True)

# Performance Metrics
st.markdown("<div class='divider'></div>",
    unsafe_allow_html=True)
st.markdown("""
<p class='section-title'>📊 Model Performance</p>
""", unsafe_allow_html=True)

col3, col4, col5 = st.columns(3)
with col3:
    st.markdown("""
    <div class='metric-card'>
        <p style='color: #8892b0;'>🎗️ Breast Cancer</p>
        <p style='color: #00d2ff; font-size: 2rem;
        font-weight: 800;'>98.25%</p>
        <p style='color: #6bff6b;'>SVM Classifier</p>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown("""
    <div class='metric-card'>
        <p style='color: #8892b0;'>🔬 Ovarian Cancer</p>
        <p style='color: #7b2ff7; font-size: 2rem;
        font-weight: 800;'>87.50%</p>
        <p style='color: #6bff6b;'>SVM Classifier</p>
    </div>
    """, unsafe_allow_html=True)
with col5:
    st.markdown("""
    <div class='metric-card'>
        <p style='color: #8892b0;'>🧠 Brain Tumor</p>
        <p style='color: #00d2ff; font-size: 2rem;
        font-weight: 800;'>99.37%</p>
        <p style='color: #6bff6b;'>U-Net CNN</p>
    </div>
    """, unsafe_allow_html=True)

# Results Images
st.markdown("<div class='divider'></div>",
    unsafe_allow_html=True)
st.markdown("""
<p class='section-title'>📈 Analysis Results</p>
""", unsafe_allow_html=True)

col6, col7 = st.columns(2)
with col6:
    st.markdown("""
    <p style='color: #8892b0; text-align: center;'>
    🎗️ Breast Cancer Analysis</p>
    """, unsafe_allow_html=True)
    st.image(
        "https://raw.githubusercontent.com/sami442/multi-cancer-detection/main/results/breast_cancer_results.png",
        use_container_width=True
    )
with col7:
    st.markdown("""
    <p style='color: #8892b0; text-align: center;'>
    🔬 Ovarian Cancer Analysis</p>
    """, unsafe_allow_html=True)
    st.image(
        "https://raw.githubusercontent.com/sami442/multi-cancer-detection/main/results/ovarian_cancer_results.png",
        use_container_width=True
    )

# Footer
st.markdown("<div class='divider'></div>",
    unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; color: #8892b0;'>
    <p>Developed with ❤️ by
    <b style='color: #00d2ff;'>Samina Mazhar</b> |
    BS Artificial Intelligence |
    <a href='https://github.com/sami442'
    style='color: #7b2ff7;'>GitHub</a> |
    <a href='https://huggingface.co/mazharsamina26'
    style='color: #00d2ff;'>Hugging Face</a></p>
</div>
""", unsafe_allow_html=True)
