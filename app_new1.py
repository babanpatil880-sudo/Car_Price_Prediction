import streamlit as st
import pandas as pd
import pickle
import os

st.title("Car Price Prediction Project")

# Load dataset
df = pd.read_csv("final.csv")

# Check model file
if not os.path.exists("model.pkl"):
    st.error("model.pkl not found")
    st.stop()

# Load model safely
try:
    with open("model.pkl", "rb") as f:
        pipe = pickle.load(f)
except Exception as e:
    st.error(f"Error loading model.pkl: {e}")
    st.stop()

# Dropdowns
companies = sorted(df["company"].unique())
fuel_types = sorted(df["fuel_type"].unique())

company = st.selectbox("Select company", companies)

names = sorted(df[df["company"] == company]["name"].unique())
name = st.selectbox("Select name", names)

year = st.number_input(
    "Enter year",
    min_value=1990,
    max_value=2025,
    value=2020,
    step=1
)

kms_driven = st.number_input(
    "Enter kilometers driven",
    min_value=10000,
    value=50000,
    step=5000
)

fuel_type = st.selectbox("Select fuel type", fuel_types)

# Predict button
if st.button("Predict Price"):

    input_df = pd.DataFrame([[
        company,
        name,
        year,
        kms_driven,
        fuel_type
    ]], columns=["company", "name", "year", "kms_driven", "fuel_type"])

    prediction = pipe.predict(input_df)

    st.success(f"Predicted Price: ₹ {round(prediction[0])}")