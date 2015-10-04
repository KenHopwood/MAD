__author__ = 'kenhopwood'

# Get CIMIS ET0 Data
# 04-OCT-2015
# K.Hopwood

import socket
import urllib
import urllib2

# Example: http://et.water.ca.gov/api/data?appKey=YOUR-APP-KEY&targets=2,8,127&startDate=2010-01-01&endDate=2010-01-05
def get_cimis_eto_daily(key, targets, start_date, end_date):

    # timeout in seconds
    timeout = 20
    socket.setdefaulttimeout(timeout)

    query_args = { 'appKey':key , '&targets' :targets, '&startDate' :start_date, '&endDate' :end_date } # you have to pass in a dictionary

    encoded_args = urllib.urlencode(query_args)

    print 'Encoded:', encoded_args

    url = 'http://et.water.ca.gov/api/data?' + encoded_args

    response = urllib2.urlopen(url).read()
    return response
