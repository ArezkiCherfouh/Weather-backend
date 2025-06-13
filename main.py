import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://arezkicherfouh.github.io"], 
    allow_credentials=True,
    allow_methods=["*"],   
    allow_headers=["*"],
)
WEATHER_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
@app.get("/weather")
def get_weather(city: str): 
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    res = requests.get(url) 
    data = res.json()  
    if res.status_code == 200:
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "feels_like" : data["main"]["feels_like"],
            "min_temp" : data["main"]["temp_min"],
            "max_temp" : data["main"]["temp_max"],
            "description": data["weather"][0]["description"].title()
        }
    else:
        return {"error": f"{res.status_code} City not found"}
