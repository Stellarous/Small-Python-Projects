import requests

def get_weather(city):
    # You would normally use an API key for the service you're using
    api_key = "your_api_key"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(base_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        wind = data["wind"]

        # Collecting and formatting the data
        current_temperature = main["temp"]
        current_humidity = main["humidity"]
        wind_speed = wind["speed"]
        weather_description = data["weather"][0]["description"]

        print(f"Temperature: {current_temperature}")
        print(f"Humidity: {current_humidity}%")
        print(f"Wind speed: {wind_speed} m/s")
        print(f"Weather description: {weather_description}")
    else:
        print("City not found.")

city = input("Enter city name: ")
get_weather(city)