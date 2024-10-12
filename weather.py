import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset (replace with actual file or API call)
data = pd.read_csv('heatwave_data.csv')

# Check for missing values
print(data.isnull().sum())

# Handle missing values (you can fill with mean/median or drop)
data.fillna(data.mean(), inplace=True)

# Feature selection (for heat wave prediction, consider temperature, humidity, etc.)
X = data[['Temperature', 'Humidity', 'WindSpeed', 'Pressure']]  # Adjust based on dataset
y = data['HeatWave']  # Target variable (1 for heatwave, 0 for no heatwave)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model: Random Forest for heatwave classification
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions and accuracy
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Feature importance (optional)
feature_importances = model.feature_importances_
features = ['Temperature', 'Humidity', 'WindSpeed', 'Pressure']
plt.bar(features, feature_importances)
plt.title("Feature Importance for Heat Wave Prediction")
plt.show()
joblib.dump(model, 'heatwave_model.pkl')

print("Model saved as 'heatwave_model.pkl'")