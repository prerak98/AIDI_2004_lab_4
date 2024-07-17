from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the pre-trained model and LabelEncoder
model = joblib.load('fish_species_predictor.pkl')
le = joblib.load('label_encoder.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.form.to_dict()
    features = [float(data['Weight']), float(data['Length1']), float(data['Length2']), 
                float(data['Length3']), float(data['Height']), float(data['Width'])]
    final_features = np.array(features).reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(final_features)
    prediction_label = le.inverse_transform(prediction)
    
    # Return the result
    return render_template('index.html', prediction_text=f'The predicted fish species is: {prediction_label[0]}')

if __name__ == "__main__":
    app.run(debug=True)
