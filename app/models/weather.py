from pydantic import BaseModel

class Location(BaseModel):
    lat: float
    lon: float
    name: str
    type: str

class WeatherResponse(BaseModel):
    city: str
    temperature: float
    feels_like: float
    humidity: float
    wind_speed: float
    uvindex: int
    rain_intensity: int
    location: Location  # expects a Location dict
