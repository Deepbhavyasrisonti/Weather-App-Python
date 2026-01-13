import requests

API_KEY = "your_api_key_here"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "weather": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
    else:
        return None

# MAIN PROGRAM (THIS LINE IS VERY IMPORTANT)
city_name = input("Enter city name: ")
weather = get_weather(city_name)

if weather:
    print("\n🌍 Weather Details")
    print(f"City: {weather['city']}")
    print(f"🌡️ Temperature: {weather['temperature']}°C")
    print(f"🌤️ Condition: {weather['weather'].title()}")
    print(f"💧 Humidity: {weather['humidity']}%")
    print(f"🌬️ Wind Speed: {weather['wind_speed']} m/s")
else:
    print("❌ City not found or API key not active")
