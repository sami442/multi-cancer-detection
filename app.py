@st.cache_resource
def load_models():
    try:
        import os
        # Get the directory of app.py
        base_dir = os.path.dirname(
            os.path.abspath(__file__))
        
        breast_path = os.path.join(
            base_dir, 'models', 
            'breast_cancer_model.pkl')
        breast_scaler_path = os.path.join(
            base_dir, 'models',
            'breast_cancer_scaler.pkl')
        ovarian_path = os.path.join(
            base_dir, 'models',
            'ovarian_cancer_model.pkl')
        ovarian_scaler_path = os.path.join(
            base_dir, 'models',
            'ovarian_cancer_scaler.pkl')

        with open(breast_path, 'rb') as f:
            breast_model = pickle.load(f)
        with open(breast_scaler_path, 'rb') as f:
            breast_scaler = pickle.load(f)
        with open(ovarian_path, 'rb') as f:
            ovarian_model = pickle.load(f)
        with open(ovarian_scaler_path, 'rb') as f:
            ovarian_scaler = pickle.load(f)

        return breast_model, breast_scaler, \
               ovarian_model, ovarian_scaler, True
    except Exception as e:
        st.sidebar.error(f"Error: {str(e)}")
        return None, None, None, None, False
