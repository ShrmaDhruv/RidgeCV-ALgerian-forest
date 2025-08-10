import pickle
import streamlit as st
import numpy as np

ridgecv_model = pickle.load(open('./models/ridgeCV.pkl', 'rb'))
standard_scaler = pickle.load(open('./models/scaler.pkl', 'rb'))

st.title(" Fire Weather Prediction (Streamlit Version)")


st.sidebar.header("Input Parameters")

Temperature = st.sidebar.slider("Temperature (°C)", min_value=-10.0, max_value=50.0, step=0.1)
RH = st.sidebar.slider("Relative Humidity (%)", min_value=0.0, max_value=100.0, step=0.1)
Ws = st.sidebar.slider("Wind Speed (m/s)", min_value=0.0, max_value=20.0, step=0.1)
Rain = st.sidebar.slider("Rain (mm)", min_value=0.0, max_value=50.0, step=0.1)
FFMC = st.sidebar.slider("FFMC Index", min_value=0.0, max_value=101.0, step=0.1)
DMC = st.sidebar.slider("DMC Index", min_value=0.0, max_value=300.0, step=0.1)
ISI = st.sidebar.slider("ISI Index", min_value=0.0, max_value=50.0, step=0.1)

# Classes and Region as 0/1 inputs
Classes = st.sidebar.selectbox("Classes", options=[0, 1])
Region = st.sidebar.selectbox("Region", options=[0, 1])

# Prepare input
input_data = [[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]]

# Scale input
scaled_data = standard_scaler.transform(input_data)

# Prediction button
if st.sidebar.button("Predict"):
    prediction = ridgecv_model.predict(scaled_data)
    st.success(f" Predicted Output: {prediction[0]:.2f}")
