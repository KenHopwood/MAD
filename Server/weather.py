__author__ = 'kenhopwood'

# Get Current Weather
# 13-SEP-2015
# K.Hopwood

import socket
import urllib
import urllib2

def getWeatherCurrent(stationid, key):

    # timeout in seconds
    timeout = 10
    socket.setdefaulttimeout(timeout)

    query_args = { 'id':stationid, ',us&APPID':key } # you have to pass in a dictionary

    encoded_args = urllib.urlencode(query_args)

    print 'Encoded:', encoded_args

    url = 'http://api.openweathermap.org/data/2.5/weather?' + encoded_args

    response = urllib2.urlopen(url).read()
    return response


# Get Weather Forecast

def getWeatherForecast(stationid, key):

    # timeout in seconds
    timeout = 10
    socket.setdefaulttimeout(timeout)

    query_args = { 'id':stationid, ',us&APPID':key } # you have to pass in a dictionary

    encoded_args = urllib.urlencode(query_args)

    print 'Encoded:', encoded_args

    url = 'http://api.openweathermap.org/data/2.5/forecast?' + encoded_args

    response = urllib2.urlopen(url).read()
    return response
