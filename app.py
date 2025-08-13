import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model
# Make sure the model file is in the same directory as this script
try:
    model = joblib.load('rainwater_harvesting_model.pkl')
except FileNotFoundError:
    st.error("Error: The model file 'rainwater_harvesting_model.pkl' was not found.")
    st.stop()

# Set up the Streamlit page
st.set_page_config(page_title="Rainwater Harvesting Predictor", layout="centered")

st.title("💧 Rainwater Harvesting Prediction Model")
st.markdown("""
This model helps predict the amount of rainwater you can capture based on key factors.
Fill in the details below to get a prediction in liters.
""")

st.header("Input Features")

# Create input widgets for the user
roof_area = st.number_input(
    'Roof Area ($m^2$)',
    min_value=20.0,
    max_value=300.0,
    value=150.0,
    step=10.0
)
st.markdown("---")

rainfall = st.number_input(
    'Average Annual Rainfall (mm)',
    min_value=10.0,
    max_value=400.0,
    value=200.0,
    step=5.0
)
st.markdown("---")

runoff_coefficient = st.number_input(
    'Runoff Coefficient (0.6 - 0.95)',
    min_value=0.6,
    max_value=0.95,
    value=0.8,
    step=0.01,
    format="%f"
)
st.markdown("---")

tank_size = st.number_input(
    'Tank Size (Liters)',
    min_value=1000,
    max_value=15000,
    value=5000,
    step=500
)
st.markdown("---")

# Make a prediction when the button is clicked
if st.button('Predict Captured Water Volume'):
    # Prepare the input data for the model
    input_data = np.array([[
        roof_area,
        rainfall,
        runoff_coefficient,
        tank_size
    ]])

    # Make the prediction
    prediction = model.predict(input_data)[0]
    
    st.header("Prediction Result")
    st.success(f"The predicted amount of rainwater captured is approximately: **{int(prediction)} Liters**")
    
    st.subheader("Model Insights")
    st.markdown("""
    * **Roof Area & Rainfall:** Our model shows these are the most significant factors. A larger roof and more rainfall lead to a higher volume of captured water.
    * **Runoff Coefficient:** This value, which depends on your roof material, also has a major impact. A higher coefficient (e.g., a metal roof) allows for more water collection.
    """)

# To run this app, save it as `app.py` and run the command:
# `streamlit run app.py`