# 📊 Customer Churn Prediction System

A full end-to-end **Machine Learning web application** that predicts customer churn probability using **XGBoost**, deployed as a **live Streamlit web app**.

This project demonstrates real-world ML practices including **data preprocessing, feature engineering, model training, evaluation, and cloud deployment**.

---

## 🚀 Live Application

👉 Live Demo:  
https://your-app-name.streamlit.app

*(Replace this with your actual Streamlit Cloud URL)*

---

## 🧠 Problem Statement

Customer churn is a critical issue in the telecom industry, where retaining existing customers is more cost-effective than acquiring new ones.

The goal of this project is to **predict whether a customer is likely to churn** based on their usage, billing, and service details, enabling proactive customer retention strategies.

---

## 🎯 Solution Overview

This application:
- Accepts **user-friendly inputs** based on original Excel data
- Internally performs **feature engineering and encoding**
- Uses a trained **XGBoost classification model**
- Outputs **churn probability** and **risk level**

---

## 🏗️ System Architecture

```
User Input / Excel Data
          ↓
Streamlit Web Application
          ↓
Feature Engineering & Encoding
          ↓
Trained XGBoost Model
          ↓
Churn Probability & Risk Level
```

---

## 📂 Project Structure

```
customer-churn-streamlit-app/
│
├── streamlit_app.py        # Streamlit UI and prediction logic
├── churn_model.pkl         # Trained XGBoost model
├── feature_columns.pkl    # Model feature schema
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 📥 Input Features

| Feature Name | Description |
|--------------|------------|
| Tenure | Number of months the customer has stayed |
| Monthly Charges | Monthly billing amount |
| Total Charges | Total amount billed |
| Contract Type | Month-to-month / One year / Two year |
| Payment Method | Electronic check / Credit card / Bank transfer |
| Internet Service | Fiber optic / DSL |

---

## 📤 Output

- **Churn Probability** (0 to 1)
- **Risk Level**
  - 🔴 HIGH: Probability ≥ 0.4
  - 🟢 LOW: Probability < 0.4

---

## 🧪 Model Details

- Algorithm: XGBoost Classifier
- Task: Binary Classification
- Metric: ROC-AUC
- Threshold optimized for churn recall

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Joblib

---

## 🌐 Deployment

Deployed using **Streamlit Cloud** via GitHub integration.

---

## 👤 Author

Your Name  
Aspiring Machine Learning Engineer

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
