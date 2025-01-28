from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the model and preprocessing objects
model = joblib.load("personalized_medicine_model.pkl")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("encoder.pkl")

# Home route to render the frontend
@app.route("/")
def index():
    return render_template("index.html")

# Prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Parse input data
        genetics = request.form.get("genetics")
        age = float(request.form.get("age"))
        weight = float(request.form.get("weight"))

        # Preprocess the inputs
        genetics_encoded = encoder.transform([[genetics]])  # Encode genetics (2D array)
        age_weight_scaled = scaler.transform([[age, weight]])  # Scale age and weight (2D array)

        # Combine features (ensure both are 2D arrays)
        features = np.hstack((genetics_encoded, age_weight_scaled))

        # Perform prediction
        prediction = model.predict(features)[0]

        # Return result
        return jsonify({"predicted_dosage": round(prediction, 2)})

    except Exception as e:
        return jsonify({"error": str(e)})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
