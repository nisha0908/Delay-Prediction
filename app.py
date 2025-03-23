#writefile app.py
import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("./best_order_delay_model.pkl")

# Function to make predictions
def predict_delay(distance_km, same_state, order_day_of_week, order_month):
    features = np.array([[distance_km, same_state, order_day_of_week, order_month]])
    prediction = model.predict(features)[0]
    return "Delayed" if prediction == 1 else "On Time"

# Streamlit UI
st.title("📦 Order Delay Prediction App")

distance_km = st.number_input("Distance (km)", min_value=0.0, step=0.1)
same_state = st.selectbox("Same State?", [1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
order_day_of_week = st.slider("Order Day of Week (0=Monday, 6=Sunday)", 0, 6)
order_month = st.slider("Order Month (1=Jan, 12=Dec)", 1, 12)

if st.button("Predict"):
    result = predict_delay(distance_km, same_state, order_day_of_week, order_month)
    st.success(f"Prediction: {result}")

