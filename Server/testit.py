__author__ = 'kenhopwood'

import weather
import json

if __name__=='__main__':
    #5341704
    response = weather.getWeatherCurrent('5325738', '9ea94521b367fd81b60f91b526bc9fee')
    print response
    weather_current = json.loads(response)
    print(json.dumps(weather_current))

    response = weather.getWeatherForecast('5325738', '9ea94521b367fd81b60f91b526bc9fee')
    #response = weather.getWeatherForecast('5341704', '9ea94521b367fd81b60f91b526bc9fee')
    print response
    weather_forecast = json.loads(response)
    print(json.dumps(weather_forecast))
