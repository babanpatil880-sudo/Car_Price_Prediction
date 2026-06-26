import streamlit as st
import pandas as pd
import pickle as pkl

st.title("Car Price Prediction Project")
df = pd.read_csv("final.csv")
pipe = pkl.load(open("car-price-predictor.pkl", "rb"))

companies = sorted(df["company"].unique())
fuel_types = sorted(df["fuel_type"].unique())

company = st.selectbox("Select company", companies)
names = sorted(df["name"][df["company"] == company].unique())
name = st.selectbox("Select name", names)
year = st.number_input("Enter year", min_value=1990, max_value=2025, value=2020, step=1)
kms_driven = st.number_input("Enter kilometers driven", min_value=10000, value=50000, step=5000)
fuel_type = st.selectbox("Select fuel type", fuel_types)

if st.button("Predict Price"):
    st.write("Your company:", company)
    st.write("Your name:", name)
    st.write("Your year:", str(year))
    st.write("Your kilometers driven:", str(kms_driven))
    st.write("Your fuel type:", fuel_type)

    columns = ['company', 'name', 'year', 'kms_driven', 'fuel_type']
    data = [[company, name, year, kms_driven, fuel_type]]
    myinput = pd.DataFrame(data, columns=columns)
    price = pipe.predict(myinput)

    st.success("Predicted price: ₹" + str(round(price[0,0])))
