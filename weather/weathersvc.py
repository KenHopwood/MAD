__author__ = 'kenhopwood'

# Weather Service
# 15-SEP-2015
# K.Hopwood

import time
import json

from weather import weather

def weathersvc(stationid, key):
    # Get Weather Current
    # Call API
    response = weather.get_weather_current(stationid, key)
    # parse JSON response
    weather_current = json.loads(response)

    # Get Weather Forecast
    # Call API
    response = weather.get_weather_forecast(stationid, key)
    # parse JSON response
    weather_forecast = json.loads(response)

    return weather_current, weather_forecast

