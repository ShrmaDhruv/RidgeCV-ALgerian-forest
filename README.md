# Forest Fire Prediction 🔥🌲

## 📌 Overview

This project is a **Machine Learning--powered Flask web application**
that predicts the **likelihood of forest fires** based on environmental
conditions such as temperature, humidity, wind speed, and more.\
It uses a **trained RidgeCV regression model** and a **StandardScaler**
for preprocessing, with a clean **web interface** for user interaction.

------------------------------------------------------------------------

## 🚀 Features

-   🌐 **Web App (Flask)** -- User-friendly interface for input and
    results.\
-   📊 **ML Model (RidgeCV)** -- Predicts fire risk based on multiple
    features.\
-   ⚡ **Data Preprocessing** -- StandardScaler ensures normalized
    input.\
-   🎨 **Styled Frontend** -- Clean HTML/CSS interface with **loading
    spinner**.\
-   📝 **Input Parameters**:
    -   Temperature\
    -   Relative Humidity (RH)\
    -   Wind Speed (Ws)\
    -   Rain\
    -   Fire Weather Indices (FFMC, DMC, ISI)\
    -   Classes (0/1)\
    -   Region

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   **Backend**: Python (Flask)\
-   **Frontend**: HTML, CSS, JavaScript\
-   **Machine Learning**: scikit-learn (RidgeCV, StandardScaler)\
-   **Deployment Ready**: Flask app structured for hosting

------------------------------------------------------------------------

## 📂 Project Structure

    ├── models/
    │   ├── ridgeCV.pkl         # Trained ML model
    │   ├── scaler.pkl          # Scaler for preprocessing
    ├── static/
    │   └── style.css           # Custom CSS styles
    ├── templates/
    │   ├── index.html          # Input form page
    │   ├── home.html           # Prediction result page
    ├── app.py                  # Flask application
    └── README.md               # Project documentation
