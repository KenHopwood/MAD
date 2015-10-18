__author__ = 'kenhopwood'

import json

from weather import weather

if __name__=='__main__':

    response = weather.get_weather_current('5325738', 'key')
    print response
    weather_current = json.loads(response)
    print(json.dumps(weather_current))

    response = weather.get_weather_forecast('5325738', 'key')
    print response
    weather_forecast = json.loads(response)
    print(json.dumps(weather_forecast))
