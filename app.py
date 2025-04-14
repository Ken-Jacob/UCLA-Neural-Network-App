import streamlit as st
import numpy as np
from data_preprocessing import load_and_preprocess_data
from model_training import train_model
from logger import get_logger

logger = get_logger(__name__)
st.set_page_config(page_title="🎓 UCLA Admission Predictor", layout="centered")

st.title("🎓 UCLA Admission Predictor")
st.write("Enter candidate details to predict the chance of admission.")

# Load and preprocess data
X_train, X_test, y_train, y_test, scaler = load_and_preprocess_data("data/Admission.csv")
model = train_model(X_train, y_train)

# Inputs
gre = st.slider("GRE Score", 260, 340, 300)
toefl = st.slider("TOEFL Score", 0, 120, 100)
univ_rating = st.slider("University Rating", 1, 5, 3)
sop = st.slider("SOP Strength (1-5)", 1.0, 5.0, 3.5)
lor = st.slider("LOR Strength (1-5)", 1.0, 5.0, 3.0)
cgpa = st.slider("CGPA (out of 10)", 5.0, 10.0, 8.0)
research = st.radio("Research Experience", ["No", "Yes"])

# Predict
if st.button("Predict"):
    input_data = np.array([[gre, toefl, univ_rating, sop, lor, cgpa, 1 if research == "Yes" else 0]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]
    st.success(f"🎯 Predicted Admission Chance: {prediction * 100:.2f}%")
