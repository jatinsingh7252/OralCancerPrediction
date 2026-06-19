import streamlit as st
import joblib
import pandas as pd

# Load trained models
diagnosis_model = joblib.load("models/diagnosis_model.pkl")
stage_model = joblib.load("models/stage_model.pkl")
survival_model = joblib.load("models/survival_model.pkl")

# Page settings
st.set_page_config(page_title="Oral Cancer Prediction System")

# Title
st.title("AI-Based Oral Cancer Prediction System")
st.write("Enter patient details below")

# Input fields
age = st.number_input("Age", min_value=18, max_value=100)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

tobacco = st.selectbox(
    "Tobacco Use",
    ["Yes", "No"]
)

alcohol = st.selectbox(
    "Alcohol Consumption",
    ["Yes", "No"]
)

hpv = st.selectbox(
    "HPV Infection",
    ["Yes", "No"]
)

betel = st.selectbox(
    "Betel Quid Use",
    ["Yes", "No"]
)

# Predict button
if st.button("Predict"):

    # Convert categorical values into numbers
    gender_value = 1 if gender == "Male" else 0
    tobacco_value = 1 if tobacco == "Yes" else 0
    alcohol_value = 1 if alcohol == "Yes" else 0
    hpv_value = 1 if hpv == "Yes" else 0
    betel_value = 1 if betel == "Yes" else 0

    # Create input dataframe
    input_data = pd.DataFrame({
        "Age": [age],
        "Gender": [gender_value],
        "Tobacco Use": [tobacco_value],
        "Alcohol Consumption": [alcohol_value],
        "HPV Infection": [hpv_value],
        "Betel Quid Use": [betel_value]
    })

    # Predictions
    diagnosis_pred = diagnosis_model.predict(input_data)[0]
    stage_pred = stage_model.predict(input_data)[0]
    survival_pred = survival_model.predict(input_data)[0]

    # Convert predictions to readable format
    diagnosis = "Positive" if diagnosis_pred == 1 else "Negative"
    stage = f"Stage {stage_pred}"
    survival = f"{round(survival_pred, 2)}%"

    # Display results
    st.success("Prediction Completed Successfully")

    st.markdown("---")
    st.header("Prediction Results")

    st.metric("Oral Cancer Diagnosis", diagnosis)
    st.metric("Cancer Stage", stage)
    st.metric("5-Year Survival Rate", survival)

    st.markdown("---")
    st.subheader("Health Suggestions")

    if diagnosis == "Positive":
        st.warning("High Risk Detected")
        st.write("• Consult a doctor immediately.")
        st.write("• Avoid tobacco products.")
        st.write("• Avoid alcohol consumption.")
        st.write("• Maintain proper oral hygiene.")
        st.write("• Follow regular medical checkups.")
    else:
        st.success("Low Risk Detected")
        st.write("• Continue maintaining oral hygiene.")
        st.write("• Eat healthy food.")
        st.write("• Avoid tobacco and alcohol.")
        st.write("• Visit a dentist regularly.")

# Disclaimer
st.markdown("---")
st.warning(
    "This system is for educational purposes only and should not replace professional medical advice."
)

st.caption(
    "Developed by Jatin Singh | SRN: PES1PG25CA377 | PES University"
)