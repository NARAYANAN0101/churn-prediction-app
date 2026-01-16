import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Customer Churn Predictor", layout="centered")

st.title("📊 Customer Churn Prediction System")

# Load model and feature columns
model = joblib.load("churn_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")

st.subheader("Enter Customer Details")

# === INPUTS (MATCHING EXCEL SHEET) ===
tenure = st.number_input("Tenure (months)", min_value=0, value=5)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=80.0)
total_charges = st.number_input("Total Charges", min_value=0.0, value=400.0)

contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
payment = st.selectbox("Payment Method", ["Electronic check", "Credit card", "Bank transfer"])
internet = st.selectbox("Internet Service", ["Fiber optic", "DSL"])

if st.button("Predict Churn"):

    model_input = dict.fromkeys(feature_columns, 0)

    model_input["tenure"] = tenure
    model_input["MonthlyCharges"] = monthly_charges
    model_input["TotalCharges"] = total_charges
    model_input["avg_monthly_spend"] = total_charges / tenure if tenure != 0 else 0

    if contract != "Month-to-month":
        model_input[f"Contract_{contract}"] = 1

    if payment != "Bank transfer":
        model_input[f"PaymentMethod_{payment}"] = 1

    if internet == "Fiber optic":
        model_input["InternetService_Fiber optic"] = 1

    input_df = pd.DataFrame([model_input])

    churn_prob = model.predict_proba(input_df)[0][1]
    risk = "HIGH 🔴" if churn_prob >= 0.4 else "LOW 🟢"

    st.subheader("Prediction Result")
    st.write(f"### Churn Probability: {round(churn_prob, 3)}")
    st.write(f"### Risk Level: {risk}")
