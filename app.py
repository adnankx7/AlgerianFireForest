from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Initialize the Flask app
app = Flask(__name__)

# Load pre-trained models
scaler = pickle.load(open('scaler.pkl', 'rb'))
ridge = pickle.load(open('ridge.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user input from the form, these 9 columns are expected from the form
        input_data = [float(request.form['Temperature']),
                      float(request.form['RH']),
                      float(request.form['Ws']),
                      float(request.form['Rain']),
                      float(request.form['FFMC']),
                      float(request.form['ISI']),
                      float(request.form['BUI']),
                      int(request.form['Classes']),    # Assuming binary (1/0) or multi-class
                      int(request.form['Region'])]     # Assuming region is categorical (converted to int)
        
        # Convert input data into a DataFrame
        df = pd.DataFrame([input_data], columns=['Temperature', 'RH', 'Ws', 'Rain', 'FFMC', 'ISI', 'BUI', 'Classes', 'Region'])
        
        # Preprocess the data using the loaded scaler
        scaled_data = scaler.transform(df)

        # Make prediction using the Ridge model
        prediction = ridge.predict(scaled_data)

        # Return the result
        return render_template('index.html', prediction_text=f'Predicted Fire Risk: {prediction[0]:.2f}')
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
