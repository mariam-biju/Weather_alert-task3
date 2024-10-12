import requests
import json
import joblib
import time

# Function to get live weather data from OpenWeatherMap
def get_live_weather_data(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"  # "units=metric" for Celsius
    response = requests.get(url)
    data = response.json()
    
    if data['cod'] == 200:
        return {
            'temp': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'pressure': data['main']['pressure']
        }
    else:
        print("Error fetching weather data.")
        return None

# Load the trained heatwave prediction model
start_time = time.time()
model = joblib.load('heatwave_model.pkl')  # Make sure your model is saved in the same folder as the script or provide the correct path
print(f"Model loaded in {time.time() - start_time:.2f} seconds")

# Function to make prediction using the loaded model
def make_prediction(features):
    return model.predict([features])

def send_firebase_notification(token, title, message):
    url = "https://fcm.googleapis.com/fcm/send"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'key=YOUR_SERVER_KEY'  # Replace with your Firebase server key
    }
    payload = {
        "to": token,
        "notification": {
            "title": title,
            "body": message,
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        print("Notification sent successfully!")
    else:
        print("Failed to send notification.")
        print(response.content)

# Main function
def main():
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    city = "London"  # Replace with the city you want to test
    user_token = "USER_DEVICE_TOKEN"  # Replace with the real device token
    
    # Fetch live weather data
    weather_data = get_live_weather_data(api_key, city)
    if weather_data:
        print("Weather Data:", weather_data)
        # Extract features from weather data
        features = [weather_data['temp'], weather_data['humidity'], weather_data['wind_speed'], weather_data['pressure']]
        
        # Predict heatwave
        prediction = make_prediction(features)
        if prediction == 1:  # If model predicts a heatwave
            print("Heatwave detected!")
            # Send Firebase notification
            send_firebase_notification(user_token, "Heatwave Alert!", "A heatwave is predicted for your location. Stay hydrated!")
        else:
            print("No heatwave detected.")
    else:
        print("Failed to retrieve weather data.")

# Run the main function periodically (every 1 hour for example)
if __name__ == "__main__":
    while True:
        main()
        time.sleep(3600)  # Wait for 1 hour before running the next prediction
