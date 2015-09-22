__author__ = 'kenhopwood'

# Batch Processor
# 15-SEP-2015
# K.Hopwood

# run batch processes on the clock

import weather
import time
import json


if __name__=='__main__':


# Every Hour

    while 1:
        # Get Weather Current
        # Call API
        print 'getting current weather...'
        response = weather.getWeatherCurrent('5325738', '9ea94521b367fd81b60f91b526bc9fee')
        # parse JSON response
        weather_current = json.loads(response)
        print(json.dumps(weather_current))
        # Store Results
        # Get Weather Forecast
        # Call API
        print 'getting weather forecast...'
        response = weather.getWeatherForecast('5325738', '9ea94521b367fd81b60f91b526bc9fee')
        # parse JSON response
        weather_forecast = json.loads(response)
        print(json.dumps(weather_forecast))
        # Store Results
        time.sleep(3600)

