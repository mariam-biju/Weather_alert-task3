# 🔥 Summer Heatwave Alert System

A machine learning-based alert system that predicts the likelihood of heatwaves based on live weather data.  
It fetches real-time weather from **OpenWeatherMap**, predicts using a **Random Forest classifier**, and sends alerts via **Firebase Cloud Messaging**.

---

## 🚀 Key Features

- 📊 **ML Model** trained on historical weather data (temperature, humidity, wind speed, pressure)  
- ☁️ **Live weather data** pulled via OpenWeatherMap API  
- 🔥 **Predicts heatwaves** using a trained `RandomForestClassifier`  
- 📱 **Sends alerts** using Firebase push notifications  
- 💾 Model saved and loaded via `joblib`  
- 📈 Feature importance visualization included

---

## 🧠 Tech Stack

- `Python`, `pandas`, `scikit-learn`, `joblib`  
- `matplotlib` for feature analysis  
- `OpenWeatherMap API` for real-time weather  
- `Firebase Cloud Messaging` for push alerts  
- `requests`, `json`, `time` for system control

---

## 🗃️ Dataset

- File: `heatwave_data.csv`  
- Example columns:
  ```
  Temperature, Humidity, WindSpeed, Pressure, HeatWave
  38.1, 60, 3.2, 1012, 1
  32.5, 70, 1.8, 1009, 0
  ...
  ```
- Target: `HeatWave` (1 for heatwave, 0 for no heatwave)

---

## 📈 Model Training

```
Model        : RandomForestClassifier (n_estimators=100)
Preprocessing: StandardScaler
Split Ratio  : 80% train / 20% test
Accuracy     : ~95% (varies with data)
```

Model is saved as:

```
heatwave_model.pkl
```

---

## 📦 Required Libraries

Install via pip:

```
pip install pandas numpy matplotlib scikit-learn joblib requests
```

If using notifications:

```
Firebase Cloud Messaging key (FCM Server Key required)
```

---

## 🔑 Required Keys

- 🔐 **OpenWeatherMap API Key**  
- 🔐 **Firebase Server Key**  
- 🔐 **User Device Token** (to receive notifications)

---

## ▶️ How to Run

1. Train the model:

```python
python train_model.py  # Or run the training block in your notebook
```

2. Add API keys in `main()`:
   ```python
   api_key = "YOUR_OPENWEATHERMAP_API_KEY"
   user_token = "USER_DEVICE_FCM_TOKEN"
   ```

3. Replace the Firebase `Authorization` key:
   ```python
   'Authorization': 'key=YOUR_FIREBASE_SERVER_KEY'
   ```

4. Run the system:

```bash
python heatwave_alert.py
```

It will fetch live data and run predictions hourly.

---

## 🔁 Real-Time Prediction Flow

```
OpenWeatherMap API ➝ Extract Features ➝ Load ML Model ➝ Predict ➝ If Heatwave ➝ Send Notification via FCM
```

---

## 📊 Example Output

```
Weather Data: {'temp': 38.7, 'humidity': 55, 'wind_speed': 3.1, 'pressure': 1008}
Heatwave detected!
Notification sent successfully!
```

---

## 📈 Visualization

Bar plot shows feature importance for heatwave detection:

- Temperature (most important)
- Humidity
- WindSpeed
- Pressure

---

## 🧪 Future Enhancements

- ⏰ Schedule with CRON instead of `time.sleep()`  
- 🌍 Extend to multiple cities / regions  
- 📉 Improve model with more historical data  
- 🧭 Build frontend using Streamlit or Flutter  
- 💬 Add voice alerts or SMS integration

---

Real-time Systems • Weather Analytics • Firebase Integration
