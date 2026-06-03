import requests

API_KEY = "YOUR_API_KEY"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            print("❌ City not found!")
            return

        # Extract data
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        weather_desc = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        # Display nicely
        print("\n🌍 Weather Report")
        print("----------------------")
        print(f"City        : {city}")
        print(f"Temperature : {temp} °C")
        print(f"Feels Like  : {feels_like} °C")
        print(f"Humidity    : {humidity} %")
        print(f"Condition   : {weather_desc}")
        print(f"Wind Speed  : {wind_speed} m/s")
        print("----------------------\n")

    except Exception as e:
        print("⚠️ Error:", e)


# Main loop
while True:
    print("===== WEATHER APP =====")
    city = input("Enter city name (or 'exit'): ")

    if city.lower() == "exit":
        print("👋 Goodbye!")
        break

    get_weather(city)