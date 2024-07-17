import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the dataset
file_path = 'Fish.csv'  # Update this with the correct path if needed
fish_data = pd.read_csv(file_path)

# Data Preprocessing
# Encode the target variable 'Species'
le = LabelEncoder()
fish_data['Species'] = le.fit_transform(fish_data['Species'])

# Selecting features and target variable
X = fish_data[['Weight', 'Length1', 'Length2', 'Length3', 'Height', 'Width']]
y = fish_data['Species']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Building
# Initializing and training the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model and the LabelEncoder
joblib.dump(model, 'fish_species_predictor.pkl')
joblib.dump(le, 'label_encoder.pkl')
print("Model and LabelEncoder saved.")
