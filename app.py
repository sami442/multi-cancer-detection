import streamlit as st
import numpy as np
import pickle
import os

# Page config
st.set_page_config(
    page_title="CancerShield AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background: #f8f9fa;
        color: #2c3e50;
    }
    .stat-card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 2px 15px rgba(0,0,0,0.08);
        text-align: center;
        border-top: 4px solid;
    }
    .section-header {
        font-size: 1.5rem;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #e74c3c;
    }
    .input-card {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 2px 15px rgba(0,0,0,0.08);
        margin-bottom: 1rem;
    }
    .tag {
        display: inline-block;
        background: #edf2f7;
        border-radius: 20px;
        padding: 0.3rem 1rem;
        font-size: 0.85rem;
        color: #2c3e50;
        margin: 0.2rem;
        font-weight: 500;
    }
    .stButton > button {
        background: linear-gradient(135deg,
            #e74c3c, #c0392b);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.7rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        width: 100%;
        box-shadow: 0 4px 15px rgba(231,76,60,0.4);
    }
    section[data-testid="stSidebar"] {
        background: #2c3e50 !important;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div style='background: white; padding: 2rem;
border-radius: 20px;
box-shadow: 0 2px 15px rgba(0,0,0,0.08);
margin-bottom: 2rem; text-align: center;'>
    <p style='font-size: 3rem; font-weight: 800;
    color: #e74c3c; margin: 0;'>
    🛡️ CancerShield AI</p>
    <p style='color: #7f8c8d; font-size: 1.1rem;
    margin: 0.5rem 0;'>
    Advanced AI-Powered Cancer Detection System
    </p>
    <div style='margin-top: 1rem;'>
        <span class='tag'>🎗️ Breast Cancer</span>
        <span class='tag'>🔬 Ovarian Cancer</span>
        <span class='tag'>🧠 Brain Tumor</span>
        <span class='tag'>🤖 AI Powered</span>
        <span class='tag'>⚕️ Medical Grade</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style='text-align: center; padding: 1rem;'>
        <p style='font-size: 1.8rem;'>🛡️</p>
        <p style='font-size: 1.2rem; font-weight: 700;
        color: white;'>CancerShield AI</p>
        <p style='color: #bdc3c7; font-size: 0.9rem;'>
        Early Detection Saves Lives</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <p style='color: #e74c3c; font-weight: 600;
    font-size: 0.9rem;'>📊 MODEL ACCURACY</p>
    <div style='margin: 0.5rem 0;'>
        <p style='color: #ecf0f1; margin: 0;
        font-size: 0.85rem;'>🎗️ Breast Cancer</p>
        <div style='background: #34495e;
        border-radius: 10px; height: 8px;'>
            <div style='background: #e74c3c;
            width: 98%; height: 8px;
            border-radius: 10px;'></div>
        </div>
        <p style='color: #e74c3c; margin: 0;
        font-size: 0.85rem; text-align: right;'>
        98.25%</p>
    </div>
    <div style='margin: 0.5rem 0;'>
        <p style='color: #ecf0f1; margin: 0;
        font-size: 0.85rem;'>🔬 Ovarian Cancer</p>
        <div style='background: #34495e;
        border-radius: 10px; height: 8px;'>
            <div style='background: #e67e22;
            width: 87%; height: 8px;
            border-radius: 10px;'></div>
        </div>
        <p style='color: #e67e22; margin: 0;
        font-size: 0.85rem; text-align: right;'>
        87.50%</p>
    </div>
    <div style='margin: 0.5rem 0;'>
        <p style='color: #ecf0f1; margin: 0;
        font-size: 0.85rem;'>🧠 Brain Tumor</p>
        <div style='background: #34495e;
        border-radius: 10px; height: 8px;'>
            <div style='background: #27ae60;
            width: 99%; height: 8px;
            border-radius: 10px;'></div>
        </div>
        <p style='color: #27ae60; margin: 0;
        font-size: 0.85rem; text-align: right;'>
        99.37%</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div style='background: #34495e;
    border-radius: 10px; padding: 1rem;'>
        <p style='color: #e74c3c; font-weight: 600;
        margin: 0; font-size: 0.9rem;'>
        👩‍💻 DEVELOPER</p>
        <p style='color: white; font-weight: 700;
        margin: 0.3rem 0;'>Samina Mazhar</p>
        <p style='color: #bdc3c7; font-size: 0.8rem;
        margin: 0;'>BS Artificial Intelligence</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div style='text-align: center;'>
        <a href='https://github.com/sami442'
        style='color: #e74c3c;
        text-decoration: none;'>🐙 GitHub</a>
        &nbsp;&nbsp;
        <a href='https://huggingface.co/mazharsamina26'
        style='color: #e67e22;
        text-decoration: none;'>🤗 HuggingFace</a>
    </div>
    """, unsafe_allow_html=True)

# Load Models
@st.cache_resource
def load_models():
    try:
        base_dir = os.path.dirname(
            os.path.abspath(__file__))

        with open(os.path.join(base_dir, 'models',
            'breast_cancer_model.pkl'), 'rb') as f:
            breast_model = pickle.load(f)

        with open(os.path.join(base_dir, 'models',
            'breast_cancer_scaler.pkl'), 'rb') as f:
            breast_scaler = pickle.load(f)

        with open(os.path.join(base_dir, 'models',
            'ovarian_cancer_model.pkl'), 'rb') as f:
            ovarian_model = pickle.load(f)

        with open(os.path.join(base_dir, 'models',
            'ovarian_cancer_scaler.pkl'), 'rb') as f:
            ovarian_scaler = pickle.load(f)

        return breast_model, breast_scaler, \
               ovarian_model, ovarian_scaler, True
    except Exception as e:
        st.sidebar.error(f"❌ Error: {str(e)}")
        return None, None, None, None, False

breast_model, breast_scaler, \
ovarian_model, ovarian_scaler, \
models_loaded = load_models()

if models_loaded:
    st.sidebar.markdown("""
    <div style='background: #27ae60;
    border-radius: 8px; padding: 0.5rem;
    text-align: center; color: white;
    margin-top: 1rem; font-weight: 600;'>
    ✅ All Models Loaded
    </div>""", unsafe_allow_html=True)
else:
    st.sidebar.warning("⚠️ Models not found!")

# Cancer Selection
st.markdown("""
<p class='section-header'>🔬 Select Detection Type</p>
""", unsafe_allow_html=True)

cancer_type = st.radio(
    "",
    ["🎗️ Breast Cancer",
     "🔬 Ovarian Cancer",
     "🧠 Brain Tumor"],
    horizontal=True
)

st.markdown("<br>", unsafe_allow_html=True)

# Breast Cancer
if cancer_type == "🎗️ Breast Cancer":
    st.markdown("""
    <div class='input-card'>
    <p class='section-header'>
    🎗️ Breast Cancer Analysis</p>
    <p style='color: #7f8c8d;'>
    Enter FNA measurements from breast mass biopsy
    </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**📏 Mean Values**")
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
            'Mean Fractal', 0.0, 0.1, 0.063)

    with col2:
        st.markdown("**📐 Standard Error**")
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
        st.markdown("**⚠️ Worst Values**")
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

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button('🔍 Run Breast Cancer Analysis',
                 use_container_width=True):
        if models_loaded:
            with st.spinner('Analyzing...'):
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
                pred = breast_model.predict(scaled)
                prob = breast_model.predict_proba(scaled)[0]

                st.markdown("<br>", unsafe_allow_html=True)
                col_r1, col_r2, col_r3 = st.columns(3)

                with col_r1:
                    st.markdown(f"""
                    <div style='background: white;
                    border-radius: 15px; padding: 1.5rem;
                    box-shadow: 0 2px 15px rgba(0,0,0,0.08);
                    text-align: center;
                    border-top: 4px solid #e74c3c;'>
                        <p style='color: #7f8c8d; margin: 0;
                        font-size: 0.9rem;'>DIAGNOSIS</p>
                        <p style='color: {"#e74c3c" if pred[0]==0 else "#27ae60"};
                        font-size: 1.3rem; font-weight: 800;
                        margin: 0.5rem 0;'>
                        {"⚠️ MALIGNANT" if pred[0]==0 else "✅ BENIGN"}
                        </p>
                    </div>
                    """, unsafe_allow_html=True)

                with col_r2:
                    st.markdown(f"""
                    <div style='background: white;
                    border-radius: 15px; padding: 1.5rem;
                    box-shadow: 0 2px 15px rgba(0,0,0,0.08);
                    text-align: center;
                    border-top: 4px solid #3498db;'>
                        <p style='color: #7f8c8d; margin: 0;
                        font-size: 0.9rem;'>CONFIDENCE</p>
                        <p style='color: #3498db;
                        font-size: 1.3rem; font-weight: 800;
                        margin: 0.5rem 0;'>
                        {max(prob)*100:.1f}%
                        </p>
                    </div>
                    """, unsafe_allow_html=True)

                with col_r3:
                    st.markdown(f"""
                    <div style='background: white;
                    border-radius: 15px; padding: 1.5rem;
                    box-shadow: 0 2px 15px rgba(0,0,0,0.08);
                    text-align: center;
                    border-top: 4px solid #9b59b6;'>
                        <p style='color: #7f8c8d; margin: 0;
                        font-size: 0.9rem;'>MODEL</p>
                        <p style='color: #9b59b6;
                        font-size: 1.3rem; font-weight: 800;
                        margin: 0.5rem 0;'>SVM</p>
                    </div>
                    """, unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)
                st.warning("⚕️ For research purposes only. "
                          "Always consult a medical professional.")
        else:
            st.error("❌ Models not loaded!")

# Ovarian Cancer
elif cancer_type == "🔬 Ovarian Cancer":
    st.markdown("""
    <div class='input-card'>
    <p class='section-header'>
    🔬 Ovarian Cancer Analysis</p>
    <p style='color: #7f8c8d;'>
    Enter patient biomarker values
    </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**🩺 Patient Information**")
        age = st.number_input('Age (years)',
                              20, 100, 50)
        bmi = st.number_input('BMI (kg/m²)',
                              10.0, 50.0, 23.0)
        glucose = st.number_input(
            'Glucose (mg/dL)', 50.0, 200.0, 92.0)
        leptin = st.number_input(
            'Leptin (ng/mL)', 0.0, 100.0, 20.0)
        adiponectin = st.number_input(
            'Adiponectin (μg/mL)', 0.0, 50.0, 10.0)

    with col2:
        st.markdown("**🔬 Biomarker Values**")
        insulin = st.number_input(
            'Insulin (μU/mL)', 0.0, 60.0, 10.0)
        homa = st.number_input(
            'HOMA Index', 0.0, 30.0, 2.0)
        resistin = st.number_input(
            'Resistin (ng/mL)', 0.0, 100.0, 15.0)
        mcp1 = st.number_input(
            'MCP-1 (pg/dL)', 0.0, 2000.0, 500.0)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button('🔍 Run Ovarian Cancer Analysis',
                 use_container_width=True):
        if models_loaded:
            with st.spinner('Analyzing biomarkers...'):
                features = np.array([[
                    age, bmi, glucose, insulin,
                    homa, leptin, adiponectin,
                    resistin, mcp1
                ]])

                scaled = ovarian_scaler.transform(features)
                pred = ovarian_model.predict(scaled)
                prob = ovarian_model.predict_proba(
                    scaled)[0]

                st.markdown("<br>", unsafe_allow_html=True)
                col_r1, col_r2, col_r3 = st.columns(3)

                with col_r1:
                    st.markdown(f"""
                    <div style='background: white;
                    border-radius: 15px; padding: 1.5rem;
                    box-shadow: 0 2px 15px rgba(0,0,0,0.08);
                    text-align: center;
                    border-top: 4px solid #e67e22;'>
                        <p style='color: #7f8c8d; margin: 0;
                        font-size: 0.9rem;'>DIAGNOSIS</p>
                        <p style='color: {"#e74c3c" if pred[0]==1 else "#27ae60"};
                        font-size: 1.3rem; font-weight: 800;
                        margin: 0.5rem 0;'>
                        {"⚠️ CANCER" if pred[0]==1 else "✅ HEALTHY"}
                        </p>
                    </div>
                    """, unsafe_allow_html=True)

                with col_r2:
                    st.markdown(f"""
                    <div style='background: white;
                    border-radius: 15px; padding: 1.5rem;
                    box-shadow: 0 2px 15px rgba(0,0,0,0.08);
                    text-align: center;
                    border-top: 4px solid #3498db;'>
                        <p style='color: #7f8c8d; margin: 0;
                        font-size: 0.9rem;'>CONFIDENCE</p>
                        <p style='color: #3498db;
                        font-size: 1.3rem; font-weight: 800;
                        margin: 0.5rem 0;'>
                        {max(prob)*100:.1f}%
                        </p>
                    </div>
                    """, unsafe_allow_html=True)

                with col_r3:
                    st.markdown(f"""
                    <div style='background: white;
                    border-radius: 15px; padding: 1.5rem;
                    box-shadow: 0 2px 15px rgba(0,0,0,0.08);
                    text-align: center;
                    border-top: 4px solid #9b59b6;'>
                        <p style='color: #7f8c8d; margin: 0;
                        font-size: 0.9rem;'>MODEL</p>
                        <p style='color: #9b59b6;
                        font-size: 1.3rem; font-weight: 800;
                        margin: 0.5rem 0;'>SVM</p>
                    </div>
                    """, unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)
                st.warning("⚕️ For research purposes only. "
                          "Always consult a medical professional.")
        else:
            st.error("❌ Models not loaded!")

# Brain Tumor
elif cancer_type == "🧠 Brain Tumor":
    st.markdown("""
    <div style='background: white;
    border-radius: 20px; padding: 3rem;
    box-shadow: 0 2px 15px rgba(0,0,0,0.08);
    text-align: center;'>
        <p style='font-size: 4rem; margin: 0;'>🧠</p>
        <p style='font-size: 1.5rem; font-weight: 700;
        color: #2c3e50; margin: 1rem 0;'>
        Brain Tumor Segmentation</p>
        <p style='color: #7f8c8d; margin-bottom: 2rem;'>
        Our dedicated U-Net model analyzes brain MRI
        scans with 99.37% accuracy</p>
        <a href='https://medical-image-segmentation-jc6hrzsdhjimse9d47n5uz.streamlit.app/'
        target='_blank'
        style='background: #e74c3c;
        color: white; padding: 1rem 3rem;
        border-radius: 10px;
        text-decoration: none;
        font-weight: 700; font-size: 1.1rem;
        display: inline-block;'>
        🚀 Launch Brain Tumor App
        </a>
    </div>
    """, unsafe_allow_html=True)

# Performance
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<p class='section-header'>📊 System Performance</p>
""", unsafe_allow_html=True)

col3, col4, col5, col6 = st.columns(4)
with col3:
    st.markdown("""
    <div class='stat-card' style='border-color:#e74c3c;'>
        <p style='color:#7f8c8d;margin:0;
        font-size:0.85rem;'>BREAST CANCER</p>
        <p style='color:#e74c3c;font-size:2rem;
        font-weight:800;margin:0.5rem 0;'>98.25%</p>
        <p style='color:#27ae60;margin:0;
        font-size:0.85rem;'>SVM Classifier</p>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown("""
    <div class='stat-card' style='border-color:#e67e22;'>
        <p style='color:#7f8c8d;margin:0;
        font-size:0.85rem;'>OVARIAN CANCER</p>
        <p style='color:#e67e22;font-size:2rem;
        font-weight:800;margin:0.5rem 0;'>87.50%</p>
        <p style='color:#27ae60;margin:0;
        font-size:0.85rem;'>SVM Classifier</p>
    </div>
    """, unsafe_allow_html=True)
with col5:
    st.markdown("""
    <div class='stat-card' style='border-color:#27ae60;'>
        <p style='color:#7f8c8d;margin:0;
        font-size:0.85rem;'>BRAIN TUMOR</p>
        <p style='color:#27ae60;font-size:2rem;
        font-weight:800;margin:0.5rem 0;'>99.37%</p>
        <p style='color:#27ae60;margin:0;
        font-size:0.85rem;'>U-Net CNN</p>
    </div>
    """, unsafe_allow_html=True)
with col6:
    st.markdown("""
    <div class='stat-card' style='border-color:#3498db;'>
        <p style='color:#7f8c8d;margin:0;
        font-size:0.85rem;'>CANCER TYPES</p>
        <p style='color:#3498db;font-size:2rem;
        font-weight:800;margin:0.5rem 0;'>3</p>
        <p style='color:#27ae60;margin:0;
        font-size:0.85rem;'>Detected</p>
    </div>
    """, unsafe_allow_html=True)

# Results Images
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<p class='section-header'>📈 Model Analysis Results</p>
""", unsafe_allow_html=True)

col7, col8 = st.columns(2)
with col7:
    st.markdown("""
    <p style='color:#7f8c8d;font-weight:600;
    text-align:center;'>🎗️ Breast Cancer Results</p>
    """, unsafe_allow_html=True)
    st.image(
        "https://raw.githubusercontent.com/sami442/multi-cancer-detection/main/results/breast_cancer_results.png",
        use_container_width=True
    )
with col8:
    st.markdown("""
    <p style='color:#7f8c8d;font-weight:600;
    text-align:center;'>🔬 Ovarian Cancer Results</p>
    """, unsafe_allow_html=True)
    st.image(
        "https://raw.githubusercontent.com/sami442/multi-cancer-detection/main/results/ovarian_cancer_results.png",
        use_container_width=True
    )

# Footer
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style='background: #2c3e50;
border-radius: 15px; padding: 2rem;
text-align: center;'>
    <p style='color: white; font-size: 1.1rem;
    font-weight: 600; margin: 0;'>
    Developed with ❤️ by
    <span style='color: #e74c3c;'>Samina Mazhar</span>
    </p>
    <p style='color: #bdc3c7; margin: 0.5rem 0;'>
    BS Artificial Intelligence |
    Islamia University Bahawalpur</p>
    <p style='margin: 0;'>
    <a href='https://github.com/sami442'
    style='color:#e74c3c;text-decoration:none;'>
    🐙 GitHub</a> &nbsp;|&nbsp;
    <a href='https://huggingface.co/mazharsamina26'
    style='color:#e67e22;text-decoration:none;'>
    🤗 HuggingFace</a> &nbsp;|&nbsp;
    <a href='https://medical-image-segmentation-jc6hrzsdhjimse9d47n5uz.streamlit.app/'
    style='color:#27ae60;text-decoration:none;'>
    🧠 Brain Tumor App</a>
    </p>
</div>
""", unsafe_allow_html=True)
