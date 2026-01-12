'''
https://open-meteo.com/
'''
from unittest import case

import openmeteo_requests
import pandas as pd
import requests
import requests_cache
from retry_requests import retry
import time

def get_city_coordinates(city):
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name"      : city,
        "count"     : 1,
        "language"  : "en",
        "format"    : "json"
    }
    response = requests.get(geo_url, params=params)
    results = response.json().get("results")

    if not results:
        return None
    return {
        "lat" : results[0]["latitude"],
        "lon" : results[0]["longitude"],
        "name": f"{results[0]['name']}, {results[0].get('country','')}"
    }
def convert_time(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))
def convert_weather_code(weather_code, is_day):
    match weather_code:
        case 0.0:
            if is_day == 1:
                return "Sunny"
            else:
                return "Clear"
        case 1.0:
            if is_day == 1:
                return "Mainly Sunny"
            else:
                return "Mainly Clear"
        case 2.0:
            return "Partly Cloudy"
        case 3.0:
            return "Cloudy"
        case 45:
            return "Foggy"
        case 48:
            return "Rime Fog"
        case 51:
            return "Light Drizzle"
        case 53:
            return "Drizzle"
        case 55:
            return "Heavy Drizzle"
        case 56:
            return "Light Freezing Drizzle"
        case 57:
            return "Freezing Drizzle"
        case 61:
             return "Light Rain"
        case 63:
            return "Rain"
        case 65:
            return "Heavy Rain"
        case 66:
            return "Light Freezing Rain"
        case 67:
            return "Freezing Rain"
        case 71:
            return "Light Snow"
        case 73:
            return "Snow"
        case 75:
            return "Heavy Snow"
        case 77:
            return "Snow Grains"
        case 80:
            return "Light Showers"
        case 81:
            return "Showers"
        case 82:
            return "Heavy Showers"
        case 85:
            return "Light Snow Showers"
        case 86:
            return "Snow Showers"
        case 95:
            return "Thunderstorm"
        case 96:
            return "Light Thunderstorm with hail"
        case 99:
            return "Thunderstorm with Hail"
def get_weather(city):

    loc = get_city_coordinates(city)

    # Setup the Open-Meteo API with Cache and rety on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    # Make sure all required weather variables are listed here
    # The order of the variables in hourly or daily is important to assign them correctly
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude" : loc["lat"],
        "longitude" : loc["lon"],
        "current" : ["temperature_2m", "is_day", "precipitation", "wind_speed_10m", "wind_direction_10m", "weather_code"],
        "wind_speed_unit": "mph",
    }
    responses = openmeteo.weather_api(url, params = params)

    #Process first location. Add a for-loop for multiple locations or models
    response = responses[0]
    print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
    print(f"Elevation: {response.Elevation()} m asl")
    print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")

    #Process Current Data. The order of the variable needs to be the same as requested
    current = response.Current()
    current_temperature = current.Variables(0).Value()
    current_is_day = current.Variables(1).Value()
    current_precipitation = current.Variables(2).Value()
    current_wind_speed = current.Variables(3).Value()
    current_wind_direction = current.Variables(4).Value()
    current_weather_code = current.Variables(5).Value()
    return {
        "time": convert_time(current.Time()),
        "temperature": current_temperature,
        "is_day": current_is_day,
        "precipitation": current_precipitation,
        "wind_speed": current_wind_speed,
        "wind_direction": current_wind_direction,
        "weather_code": convert_weather_code(current_weather_code, current_is_day)
    }
    '''
    print(f"\nCurrent time: {convert_time(current.Time())}")
    print(f"Current temperature: {current_temperature:.2f}°C")
    if current_is_day == 1:
        print(f"Currently There is daylight")
    else:
        print(f"Currently There is no daylight")
    print(f"Current precipitation: {current_precipitation}")
    print(f"Current wind_speed: {current_wind_speed:.2f}")
    print(f"Current wind_direction: {current_wind_direction:.2f}")
    print(f"Current weather_code: {current_weather_code}")
    print(f"Current weather_code: {convert_weather_code(current_weather_code, current_is_day)}")
    '''
if __name__ == '__main__':
    get_weather(input)