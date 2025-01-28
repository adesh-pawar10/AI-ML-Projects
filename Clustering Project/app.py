import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from flask import Flask, request, render_template

app = Flask(__name__)

# Function to handle predictions from different models
def predict_cluster(new_data, model_type):
    if model_type == 'kmeans':
        # Reshape and scale data
        new_data_reshaped = np.array(new_data).reshape(1, -1)
        scaler = joblib.load('scaler.pkl')
        new_data_scaled = scaler.transform(new_data_reshaped)

        # Load the KMeans model and predict
        kmeans_model = joblib.load('kmeans_model.pkl')
        cluster = kmeans_model.predict(new_data_scaled)

    elif model_type == 'dbscan':
        # Reshape and scale data
        new_data_reshaped = np.array(new_data).reshape(1, -1)
        scaler = joblib.load('scaler.pkl')
        new_data_scaled = scaler.transform(new_data_reshaped)

        # Load the DBSCAN model and predict
        dbscan_model = joblib.load('dbscan_model.pkl')
        cluster = dbscan_model.fit_predict(new_data_scaled)  # DBSCAN doesn't have 'predict', it uses 'fit_predict'

    elif model_type == 'hierarchical':
        # Reshape and scale data
        new_data_reshaped = np.array(new_data).reshape(1, -1)
        scaler = joblib.load('scaler.pkl')
        new_data_scaled = scaler.transform(new_data_reshaped)

        # Load the Hierarchical model and predict using fit_predict
        hierarchical_model = joblib.load('hierarchical_model.pkl')

        # Since AgglomerativeClustering doesn't have predict, use fit_predict to cluster the new data
        # Note: this approach works if you're clustering the new data point along with the dataset
        cluster = hierarchical_model.fit_predict(new_data_scaled)

    else:
        return "Model type not supported."

    return cluster

# Flask route to handle the prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the form
        overall = float(request.form['overall'])
        potential = float(request.form['potential'])
        pace = float(request.form['pace'])
        shooting = float(request.form['shooting'])
        passing = float(request.form['passing'])
        dribbling = float(request.form['dribbling'])
        
        # Compile the new data into a list
        new_data = [overall, potential, pace, shooting, passing, dribbling]
        
        # Get the selected model type from the form
        model_type = request.form['model_type']
        
        # Get the cluster prediction from the appropriate model
        cluster_prediction = predict_cluster(new_data, model_type)
        
        return f"Cluster Prediction: {cluster_prediction}"

    except Exception as e:
        return f"Error: {str(e)}"

# Home route to render the form
@app.route('/')
def home():
    return render_template('index.html')  # Make sure you have an 'index.html' in the 'templates' folder

if __name__ == "__main__":
    app.run(debug=True)