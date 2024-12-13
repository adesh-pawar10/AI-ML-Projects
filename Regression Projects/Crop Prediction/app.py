from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load model and scalers
model = pickle.load(open('model.pkl', 'rb'))
min_max = pickle.load(open('minmaxscaler.pkl', 'rb'))
scaler = pickle.load(open('standscaler.pkl', 'rb'))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form data
        N = float(request.form.get("N"))
        P = float(request.form.get("P"))
        K = float(request.form.get("K"))
        temperature = float(request.form.get("temperature"))
        humidity = float(request.form.get("humidity"))
        ph = float(request.form.get("ph"))
        rainfall = float(request.form.get("rainfall"))

        # Preprocess features
        features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        mx_features = min_max.transform(features)
        sc_mx_features = scaler.transform(mx_features)

        # Make prediction
        prediction = model.predict(sc_mx_features)[0]

        # Crop dictionary for mapping
        crop_dict = {
            1: 'Rice', 2: 'Maize', 3: 'Jute', 4: 'Cotton', 5: 'Coconut', 6: 'Papaya',
            7: 'Orange', 8: 'Apple', 9: 'Muskmelon', 10: 'Watermelon', 11: 'Grapes',
            12: 'Mango', 13: 'Banana', 14: 'Pomegranate', 15: 'Lentil', 16: 'Blackgram',
            17: 'Mungbean', 18: 'Mothbeans', 19: 'Pigeonpeas', 20: 'Kidneybeans',
            21: 'Chickpea', 22: 'Coffee'
        }

        # Get crop name
        recommended_crop = crop_dict.get(prediction, "Unknown Crop")

        return jsonify({"recommended_crop": recommended_crop})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
