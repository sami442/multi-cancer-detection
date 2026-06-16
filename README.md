# 🏥 CancerShield AI — Multi-Cancer Detection

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Scikit--learn](https://img.shields.io/badge/Scikit--learn-1.0+-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Models](https://img.shields.io/badge/Models-SVM%20%7C%20RF%20%7C%20GB-orange)
[![Hugging Face](https://img.shields.io/badge/🤗-Hugging%20Face-yellow)](https://huggingface.co/mazharsamina26)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://multi-cancer-detection-9jme9mlzxhhllkct4ec3ft.streamlit.app/)

## 🚀 Live Demo
👉 [**Try the App Here**](https://multi-cancer-detection-9jme9mlzxhhllkct4ec3ft.streamlit.app/)

## 📌 Overview
CancerShield AI is an advanced machine learning 
dashboard for detecting multiple types of cancer 
using real clinical datasets. The system combines 
traditional ML algorithms with modern web deployment 
to provide accessible cancer screening tools for 
healthcare professionals and researchers.

## ✨ App Features
- 🎗️ **Breast Cancer Detection** — FNA measurements
- 🔬 **Ovarian Cancer Detection** — Biomarker analysis
- 🧠 **Brain Tumor** — Links to dedicated MRI app
- 📊 **Real-time predictions** with confidence scores
- 🎨 **Professional white/red UI** design
- ⚕️ **Medical disclaimer** included
- 🔗 **Integrated** with Brain Tumor app

## 🎯 Supported Cancer Types
| Cancer Type | Model | Dataset | Samples | Accuracy |
|-------------|-------|---------|---------|----------|
| 🎗️ Breast Cancer | SVM | Wisconsin UCI | 569 | 98.25% |
| 🔬 Ovarian Cancer | SVM | Coimbra UCI | 116 | 87.50% |
| 🧠 Brain Tumor | U-Net CNN | LGG MRI Kaggle | 3929 | 99.37% |

## 📊 Detailed Model Performance

### 🎗️ Breast Cancer (Wisconsin Dataset)
| Model | Accuracy | Notes |
|-------|----------|-------|
| Random Forest | 96.49% | Good baseline |
| Logistic Regression | 97.37% | Linear model |
| **SVM** | **98.25%** | **Best model** |

### 🔬 Ovarian Cancer (Coimbra Dataset)
| Model | Accuracy | Notes |
|-------|----------|-------|
| Random Forest | 79.17% | Good baseline |
| Gradient Boosting | 87.50% | Strong performer |
| **SVM** | **87.50%** | **Best model** |

### 📈 Overall Performance
| Cancer Type | Accuracy | AUC | Precision | Recall |
|-------------|----------|-----|-----------|--------|
| Breast Cancer | 98.25% | 0.99 | 98% | 99% |
| Ovarian Cancer | 87.50% | 0.91 | 86% | 89% |
| Brain Tumor | 99.37% | 0.99 | 99% | 99% |

## 🏗️ Model Details

### 🎗️ Breast Cancer Model
| Component | Detail |
|-----------|--------|
| Algorithm | Support Vector Machine (SVM) |
| Kernel | RBF |
| Features | 30 FNA measurements |
| Preprocessing | StandardScaler |
| Classes | Malignant / Benign |

### 🔬 Ovarian Cancer Model
| Component | Detail |
|-----------|--------|
| Algorithm | Support Vector Machine (SVM) |
| Features | 9 clinical biomarkers |
| Preprocessing | StandardScaler |
| Classes | Cancer / Healthy |
| Dataset | Real patient data |

## 📂 Datasets Used
| Dataset | Source | Samples | Features | Type |
|---------|--------|---------|----------|------|
| Wisconsin Breast Cancer | UCI ML Repository | 569 | 30 | Real |
| Coimbra Cancer Biomarkers | UCI ML Repository | 116 | 9 | Real |
| LGG MRI Segmentation | Kaggle | 3929 | Images | Real |

## 📈 Analysis Results

### 🎗️ Breast Cancer Analysis
![Breast Cancer EDA](https://raw.githubusercontent.com/sami442/multi-cancer-detection/main/results/breast_cancer_eda.png)

### 📊 Breast Cancer Results
![Breast Cancer Results](https://raw.githubusercontent.com/sami442/multi-cancer-detection/main/results/breast_cancer_results.png)

### 🔬 Ovarian Cancer Analysis
![Ovarian Cancer EDA](https://raw.githubusercontent.com/sami442/multi-cancer-detection/main/results/ovarian_cancer_eda.png)

### 📊 Ovarian Cancer Results
![Ovarian Cancer Results](https://raw.githubusercontent.com/sami442/multi-cancer-detection/main/results/ovarian_cancer_results.png)

## 🗂️ Project Structure
