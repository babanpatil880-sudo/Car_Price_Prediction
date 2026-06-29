import streamlit as st
import pandas as pd
import pickle
import os
import joblib

st.title("Car Price Prediction Project")

# Load dataset
df = pd.read_csv("final.csv")

model = joblib.load("linear_model.pkl")

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
