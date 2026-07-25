# =================================================================
# PROJECT: FLOWER RECOGNITION SYSTEM - STREAMLIT DEPLOYMENT (app.py)
# =================================================================
# RATIONALE: This application serves as the 'Functional Prototype' for 
# Task 1. It transitions the VGG16 model from a research environment 
# to a real-world, interactive web interface (LO1).

import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Intelligent Flower Classifier", layout="centered")

# =================================================================
# SECTION: MODEL LOADING & CACHING
# =================================================================
# RATIONALE: We use st.cache_resource to ensure the model is loaded 
# only once. This optimizes memory usage and ensures high-speed 
# inference, which is critical for positive user experience (LO3).

@st.cache_resource
def load_flower_model():
    try:
        # Load the serialized .keras file created in the notebook
        model = tf.keras.models.load_model('Flower_Recog_Model.keras')
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_flower_model()

# --- DEFINE CLASS NAMES ---
# RATIONALE: These must match the 'flower_names' list from the 
# training notebook to ensure 'Inference Parity' (LO1).
flower_names = ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']

# =================================================================
# SECTION: IMAGE PREPROCESSING PIPELINE
# =================================================================
# RATIONALE: Every input must undergo the EXACT same transformations 
# as the training data (Resizing to 180x180 and scaling to [0,1]). 
# Failure to do so would result in a 'Feature Mismatch' (LO1).

def predict_flower(img, model):
    # Resize and convert to array
    img = img.resize((180, 180)) 
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    
    # Normalize and expand dimensions (simulate batch size of 1)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    # Execute inference
    predictions = model.predict(img_array)
    
    # Extract index and confidence score
    result_idx = np.argmax(predictions[0])
    confidence = np.max(predictions[0])
    
    return flower_names[result_idx], confidence

# =================================================================
# SECTION: USER INTERFACE (UI) DESIGN
# =================================================================

st.title("🌸 Flower Species Identifier")
st.markdown("---")
st.write("Upload a photo of a flower, and our **VGG16-powered AI** will identify the species.")

# --- FILE UPLOADER ---
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    st.write("### AI Analysis in progress...")
    
    # Run Prediction
    with st.spinner('Analyzing patterns...'):
        label, score = predict_flower(image, model)
    
    # --- EXPERT PRESENTATION ---
    # RATIONALE: Presenting the 'Confidence Score' is vital for 
    # AI Transparency. It allows the user to judge the reliability 
    # of the model's decision in real-time (LO3).
    st.success(f"**Prediction:** {label.title()}")
    st.info(f"**Confidence Level:** {score*100:.2f}%")
    
    # Progress bar for visual representation of confidence
    st.progress(float(score))

# --- FOOTER ---
st.markdown("---")
st.caption("Developed for CET313 - Intelligent Systems Prototype.")