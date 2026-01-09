'''
https://open-meteo.com/
'''
import openmeteo_requests
import pandas as pd
import requests
import requests_cache
from retry_requests import retry
import time

def convert_time(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))
def convert_weather_code(weather_code):
    return weather_code
# Setup the Open-Meteo API with Cache and rety on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of the variables in hourly or daily is important to assign them correctly
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude" : 51.5085,
    "longitude" : -0.1257,
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
