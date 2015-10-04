__author__ = 'kenhopwood'

# Get Current Weather
# 13-SEP-2015
# K.Hopwood

import socket
import urllib
import urllib2

# OpenWeatherMap API http://openweathermap.org/api
def get_weather_current(stationid, key):

    # timeout in seconds
    timeout = 20
    socket.setdefaulttimeout(timeout)

    query_args = { 'id':stationid, ',us&APPID':key } # you have to pass in a dictionary

    encoded_args = urllib.urlencode(query_args)

    print 'Encoded:', encoded_args

    url = 'http://api.openweathermap.org/data/2.5/weather?' + encoded_args

    response = urllib2.urlopen(url).read()
    return response


# Get Weather Forecast

def get_weather_forecast(stationid, key):

    # timeout in seconds
    timeout = 20
    socket.setdefaulttimeout(timeout)

    query_args = { 'id':stationid, ',us&APPID':key } # you have to pass in a dictionary

    encoded_args = urllib.urlencode(query_args)

    print 'Encoded:', encoded_args

    url = 'http://api.openweathermap.org/data/2.5/forecast?' + encoded_args

    response = urllib2.urlopen(url).read()
    return response
