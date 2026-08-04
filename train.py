import streamlit as st
import pandas as pd
import joblib

# Load the trained pipeline
pipeline = joblib.load("models/house_price_pipeline.pkl")

st.set_page_config(
    page_title="California House Price Predictor",
    page_icon="🏠",
)

st.title("🏠 California House Price Predictor")
st.write("Enter the house details below.")

longitude = st.number_input("Longitude", value=-118.0)
latitude = st.number_input("Latitude", value=34.0)
housing_median_age = st.number_input("Housing Median Age", value=20)
total_rooms = st.number_input("Total Rooms", value=2000)
total_bedrooms = st.number_input("Total Bedrooms", value=400)
population = st.number_input("Population", value=1000)
households = st.number_input("Households", value=350)
median_income = st.number_input("Median Income", value=4.0)

ocean_proximity = st.selectbox(
    "Ocean Proximity",
    [
        "<1H OCEAN",
        "INLAND",
        "NEAR OCEAN",
        "NEAR BAY",
        "ISLAND"
    ]
)

if st.button("Predict House Price"):

    input_df = pd.DataFrame({
        "longitude": [longitude],
        "latitude": [latitude],
        "housing_median_age": [housing_median_age],
        "total_rooms": [total_rooms],
        "total_bedrooms": [total_bedrooms],
        "population": [population],
        "households": [households],
        "median_income": [median_income],
        "ocean_proximity": [ocean_proximity]
    })

    prediction = pipeline.predict(input_df)

    st.success(f"🏡 Estimated House Price: ${prediction[0]:,.2f}")