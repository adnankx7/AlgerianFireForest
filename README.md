# Algerian Forest Fire Prediction Web Application

This project is a web application built using Flask that predicts the risk of forest fires in Algeria based on several weather and environmental factors. The model is trained using a Ridge regression model, and the app provides an interactive and animated user interface to input data and generate predictions.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Model Information](#model-information)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Project Overview

This web application allows users to predict the likelihood of forest fires in Algeria by inputting specific weather and environmental parameters. The prediction is made using a Ridge regression model that has been trained on historical data. The user-friendly interface, styled with animations, makes it easy for anyone to interact with the model and obtain predictions.

## Features

- **Interactive Web Interface**: The app allows users to input values such as temperature, wind speed, humidity, and other environmental factors.
- **Real-Time Prediction**: Based on user input, the Ridge regression model predicts the fire risk and displays the result instantly.
- **Advanced Animations**: The UI includes smooth animations to enhance user experience.
- **Error Handling**: The app includes robust error handling to ensure that invalid inputs are properly managed.
- **Model Scalability**: The model can be updated or replaced easily by retraining with new data.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS (with animations), JavaScript
- **Machine Learning**: Scikit-learn (Ridge Regression, StandardScaler)
- **Model Serialization**: Pickle

## Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Pip (Python package installer)
- Virtual environment (optional but recommended)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/algerian-forest-fire-prediction.git
   cd algerian-forest-fire-prediction


### Create and activate a virtual environment (optional):

python3 -m venv env
source env/bin/activate   # For MacOS/Linux
env\Scripts\activate      # For Windows
Install the required packages:

pip install -r requirements.txt
Place your pre-trained model and scaler files (ridge.pkl and scaler.pkl) in the root directory of the project.

### Running the Application
Start the Flask application:

python app.py
Open your browser and go to http://127.0.0.1:5000/ to access the app.

## Usage
On the home page, enter the following data into the form:

Temperature: The temperature in degrees Celsius.
Relative Humidity (RH): The relative humidity as a percentage.
Wind Speed (Ws): The wind speed in km/h.
Rain: The rainfall in mm.
FFMC: Fine Fuel Moisture Code.
ISI: Initial Spread Index.
BUI: Build-Up Index.
Classes: Binary value (0 or 1) indicating forest class.
Region: Binary value (0 or 1) indicating the region in Algeria.
Click on the "Predict" button to see the predicted fire risk.

The result will appear on the page after the prediction is made.

### File Structure
/flask_app
├── app.py            # Main Flask application
├── templates
│   └── index.html     # HTML page for user interface
├── static
│   ├── style.css      # CSS for styling
│   └── script.js      # JavaScript for animations
├── scaler.pkl         # Pre-trained scaler model
└── ridge.pkl          # Pre-trained Ridge model

app.py: The main Flask app that handles routes, form submissions, and predictions.
templates/index.html: The HTML file that structures the form and the results page.
static/style.css: The CSS file for styling and animations.
static/script.js: JavaScript file for enhancing user interaction and button animations.
scaler.pkl: The serialized StandardScaler used to preprocess input data.
ridge.pkl: The pre-trained Ridge regression model.
## Model Information
### Input Features
The model uses the following 9 features to make predictions:

Temperature: Temperature in degrees Celsius.
RH: Relative Humidity as a percentage.
Ws: Wind Speed in km/h.
Rain: Rainfall in mm.
FFMC: Fine Fuel Moisture Code.
ISI: Initial Spread Index.
BUI: Build-Up Index.
Classes: Forest class (binary).
Region: Region in Algeria (binary).

## Model Pipeline
The input features are scaled using StandardScaler.
The Ridge regression model makes predictions based on the scaled inputs.
Both the scaler and the model are loaded from scaler.pkl and ridge.pkl files, respectively.

## Prediction Result

MAE:  0.5192048325844728
R2 Score:  0.9801058063273602