import streamlit as st

# Page title
st.set_page_config(page_title="Oral Cancer Prediction System")

# Heading
<<<<<<< HEAD
st.title("AI-Based Oral Cancer Prediction System")
=======
st.title("🩺 AI-Based Oral Cancer Prediction System")
>>>>>>> de3bba5cfe9857bd2ef87985bf1e46edbc54aa2c

st.write("Enter patient details below")

# Input fields
age = st.number_input("Age", min_value=1, max_value=100)

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

    risk_score = 0
    if tobacco == "Yes":
        risk_score += 1
    if alcohol == "Yes":
        risk_score += 1
    if hpv == "Yes":
        risk_score += 1
    if betel == "Yes":
        risk_score += 1

    # Prediction Logic
    if risk_score >= 3:
        diagnosis = "Positive"
        stage = "Stage 2"
        survival = "70%"
    else:
        diagnosis = "Negative"
        stage = "Stage 0"
        survival = "95%"

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