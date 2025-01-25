import requests
import datetime
import geocoder
from config import OPENWEATHER_API_KEY

class WeatherService:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    @staticmethod
    def get_current_location():
        try:
            g = geocoder.ip('me')
            return g.city if g.city else None
        except Exception as e:
            print(f"Location detection error: {e}")
            return None

    @classmethod
    def fetch_weather(cls, location, units='metric'):
        try:
            params = {
                'q': location,
                'appid': OPENWEATHER_API_KEY,
                'units': units
            }
            response = requests.get(cls.BASE_URL, params=params)
            data = response.json()
            
            if response.status_code != 200:
                return {"error": data.get("message", "Unknown error")}

            return {
                "name": data["name"],
                "description": data["weather"][0]["description"],
                "temp": round(data["main"]["temp"], 1),
                "feels_like": round(data["main"]["feels_like"], 1),
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "wind_speed": data["wind"]["speed"],
                "visibility": round(data.get("visibility", 0) / 1000, 1),
                "sunrise": datetime.datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%I:%M %p'),
                "sunset": datetime.datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%I:%M %p')
            }
        except Exception as e:
            return {"error": str(e)}