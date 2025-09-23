from fastapi import APIRouter, HTTPException
from app.models.weather import WeatherResponse
from app.services.weather_service import WeatherService

router = APIRouter()
weather_service = WeatherService()

@router.get("/{city}", response_model=WeatherResponse)
async def read_weather(city: str):
    try:
        weather_data = weather_service.get_weather(city)
        if not weather_data:
            raise HTTPException(status_code=404, detail=f"No weather data found for city: {city}")
        return WeatherResponse(**weather_data)
    except Exception as e:
        print(f"Error fetching weather for {city}: {e}")
        raise HTTPException(status_code=500, detail=f"Error fetching weather for city: {city}")
