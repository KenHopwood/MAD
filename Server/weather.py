__author__ = 'kenhopwood'

# Get Current Weather
# 13-SEP-2015
# K.Hopwood

import socket
import urllib2

def getWeatherCurrent(stationid, key):

    # timeout in seconds
    timeout = 10
    socket.setdefaulttimeout(timeout)

    req = urllib2.Request('api.openweathermap.org/data/2.5/weather?id='+stationid+',us'+ '&APPID=' +key)
    try:
        response = urllib2.urlopen(req)
    except urllib2.URLError as e:
        if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
        elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
    else:
        # everything is fine
        return response

# Get Weather Forecast

def getWeatherForecast(stationid, key):

    # timeout in seconds
    timeout = 10
    socket.setdefaulttimeout(timeout)

    req = urllib2.Request('api.openweathermap.org/data/2.5/weather?forecast?id='+stationid+ '&APPID=' +key)
    try:
        response = urllib2.urlopen(req)
    except urllib2.URLError as e:
        if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
        elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
    else:
        # everything is fine
        return response

