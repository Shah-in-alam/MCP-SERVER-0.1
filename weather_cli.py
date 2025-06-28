import requests
import os
import argparse
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('OPENWEATHER_API_KEY')
API_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city, api_key):
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description'].capitalize()
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        print(f"\nWeather in {city}:")
        print(f"  {weather}")
        print(f"  Temperature: {temp}°C (feels like {feels_like}°C)")
        print(f"  Humidity: {humidity}%\n")
    else:
        print(f"Could not get weather for {city}. Error: {response.status_code} - {response.text}")

def main():
    global API_KEY
    parser = argparse.ArgumentParser(description="Check the current weather for a city.")
    parser.add_argument('--city', type=str, help='City name to check the weather for.')
    args = parser.parse_args()

    if not API_KEY:
        API_KEY = input("Enter your OpenWeatherMap API key: ").strip()
    city = args.city or input("Enter city name: ").strip()
    get_weather(city, API_KEY)

if __name__ == "__main__":
    main() 