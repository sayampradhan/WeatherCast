import datetime as dt
import requests

# Accessing API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key', 'r').read()

while True:
    # Input from user asking city name
    CITY = input("City: ")

    # Create the API URL
    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

    # Send a GET request to the API and retrieve the response
    response = requests.get(url).json()

    # Extract relevant weather data from the response
    weather_data = {
        'temperature': response['main']['temp'] - 273.15,
        'feels_like': response['main']['feels_like'] - 273.15,
        'wind_speed': response['wind']['speed'],
        'humidity': response['main']['humidity'],
        'description': response['weather'][0]['description'],
        'sunrise_time': dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone']),
        'sunset_time': dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
    }

    # Display the weather information to the user
    print(f"Temperature in {CITY}: {weather_data['temperature']:.2f}℃")
    print(f"Temperature in {CITY} feels like: {weather_data['feels_like']:.2f}℃")
    print(f"Humidity in {CITY}: {weather_data['humidity']}%")
    print(f"Wind Speed in {CITY}: {weather_data['wind_speed']} m/s")
    print(f"General Weather in {CITY}: {weather_data['description']}")
    print(f"Sunrise in {CITY}: {weather_data['sunrise_time']} local time.")
    print(f"Sunset in {CITY}: {weather_data['sunset_time']} local time.")

    # Ask the user if they want to continue
    a = input("Continue? (y/n) \n")
    if a == 'n':
        break
    elif a != 'y':
        print("Invalid Input")

    print("\n\n\n")
