import streamlit as st
import pandas as pd
import pickle
import os
import joblib

st.title("Car Price Prediction Project")

df = pd.read_csv("final.csv")

pipe =joblib.load("car_model.pkl")

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
    step=1,
)

kms_driven = st.number_input(
    "Enter kilometers driven",
    min_value=10000,
    value=50000,
    step=5000,
)

fuel_type = st.selectbox("Select fuel type", fuel_types)

if st.button("Predict Price"):
    columns = ["company", "name", "year", "kms_driven", "fuel_type"]
    data = [[company, name, year, kms_driven, fuel_type]]
    myinput = pd.DataFrame(data, columns=columns)

    price = pipe.predict(myinput)

    st.success(f"Predicted price: ₹{round(price[0][0])}")