
import streamlit as st
import joblib

model = joblib.load('model/model.pkl')

st.title("Model Prediction Dashboard")

input_1 = st.number_input("Feature 1")
input_2 = st.number_input("Feature 2")

if st.button("Predict"):
    pred = model.predict([[input_1, input_2]])
    st.write(f"Prediction: {pred[0]}")
