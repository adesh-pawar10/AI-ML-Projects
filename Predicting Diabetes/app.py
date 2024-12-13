from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Load the model and scaler
model = joblib.load('best_model.pkl')
scaler = joblib.load('scaler.pkl')

# Initialize Flask app
app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for making predictions
@app.route('/predict', methods=['POST'])

def predict():
    try:
        # Get input features from the form
        features = [float(x) for x in request.form.values()]
        
        # Ensure the correct number of features
        if len(features) != 8:
            return jsonify({"error": "Expected 8 features, but got fewer."})
        
        # Convert input to numpy array and scale
        input_array = np.array(features).reshape(1, -1)
        scaled_data = scaler.transform(input_array)
        
        # Make predictions
        prediction = model.predict(scaled_data)[0]
        prediction_prob = model.predict_proba(scaled_data)[0, 1]
        
        # Return results to the user
        result = {
            "Prediction": "Diabetic" if prediction == 1 else "Non-Diabetic",
            "Probability": round(prediction_prob, 2)
        }
        return render_template(
            'index.html',
            prediction_text = f"Prediction: {result['Prediction']}, Probability: {result['Probability']}"
        )
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug = True)