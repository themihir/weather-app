from typing import Dict, Any
import requests
import os
from dotenv import load_dotenv

load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

class WeatherService:
    def __init__(self, api_key: str=WEATHER_API_KEY, base_url: str = "https://api.tomorrow.io/v4/weather/realtime"):
        if not api_key:
            raise ValueError("Missing WEATHER_API_KEY in environment variables")
        self.api_key = api_key
        self.base_url = base_url

    def get_weather(self, city: str) -> Dict[str, Any]:
        url = f"{self.base_url}?location={city}&apikey={self.api_key}"
        headers = {
            "accept": "application/json",
            "accept-encoding": "deflate, gzip, br",
            "user-agent": "fastapi-weather-app"
        }
        response = requests.get(url, headers=headers)
        print(f"Request URL: {url}")
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")  # <--- Add this
        response.raise_for_status()
        data = response.json()

        # if "data" not in data:
        #     raise ValueError(f"No weather data found for city: {city}")

        values = data["data"]["values"]


        return {
            "city": city.title(),
            "temperature": values.get("temperature"),
            "feels_like": values.get("temperatureApparent"),
            "humidity": values.get("humidity"),
            "wind_speed": values.get("windSpeed"),
            "uvindex": values.get("uvIndex"),
            "rain_intensity": values.get("rainIntensity"),
            "location": data.get("location"),  # full dict, not just name
        }
