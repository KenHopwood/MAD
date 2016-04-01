__author__ = 'kenhopwood'

# Get CIMIS ET0 Data
# 04-OCT-2015
# K.Hopwood
# Copyright (c) 2016 All rights reserved.

import socket
import urllib
import urllib2
import datetime
import json
from data_dict import data


# station 005 Shafter
# Example: http://et.water.ca.gov/api/data?appKey=YOUR-APP-KEY&targets=2,8,127&startDate=2010-01-01&endDate=2010-01-05
def get_cimis_eto_daily(key, targets, start_date, end_date):
    # timeout in seconds
    timeout = 20
    socket.setdefaulttimeout(timeout)

    query_args = {'appKey': key, 'targets': targets, 'startDate': start_date,
                  'endDate': end_date, 'unitOfMeasure': "M"}  # you have to pass in a dictionary

    encoded_args = urllib.urlencode(query_args)

    # print 'Encoded:', encoded_args

    url = 'http://et.water.ca.gov/api/data?' + encoded_args
    # print url
    response = urllib2.urlopen(url).read()
    print "Fetch CIMIS data"
    return response


def process_cimis():
    # convert to yyyy-mm-dd for use in get_cimis_eto_daily
    start_date = datetime.datetime.now().strftime("%Y-%m-%d")
    end_date = start_date

    # read API key from file
    f = open('keyfile', 'r')
    key = f.read(36)

    resp_json = get_cimis_eto_daily(key, "005", start_date, end_date)
    # load data from JSON response
    cimis_data = json.loads(resp_json)
    data['eto'] = cimis_data['Data']['Providers'][0]['Records'][0]['DayAsceEto']['Value']
    print "data['eto']:", data['eto']
    return


"""
JSON output:
{u'Data':
    {u'Providers': [
        {u'Owner': u'water.ca.gov',
        u'Records': [
            {
                u'DayPrecip': {u'Qc': u'M', u'Unit': u'(in)', u'Value': None},
                u'DayWindSpdAvg': {u'Qc': u'M', u'Unit': u'(MPH)', u'Value': None},
                u'ZipCodes': u'93263, 93280, 93388',
                u'DayAirTmpMin': {u'Qc': u'M', u'Unit': u'(F)', u'Value': None},
                u'DayRelHumMin': {u'Qc': u'M', u'Unit': u'(%)', u'Value': None},
                u'Julian': u'59',
                u'DayAsceEto': {u'Qc': u'A', u'Unit': u'(in)', u'Value': u'0.09'},
                u'DaySolRadAvg': {u'Qc': u'M', u'Unit': u'(Ly/day)', u'Value': None},
                u'DayAirTmpMax': {u'Qc': u'M', u'Unit': u'(F)', u'Value': None},
                u'Standard': u'english',
                u'DayDewPnt': {u'Qc': u'M', u'Unit': u'(F)', u'Value': None},
                u'Station': u'5',
                u'DayWindRun': {u'Qc': u'M', u'Unit': u'(MPH)', u'Value': None},
                u'DayVapPresAvg': {u'Qc': u'M', u'Unit': u'(mBars)', u'Value': None},
                u'Date': u'2016-02-28',
                u'Scope': u'daily',
                u'DayRelHumMax': {u'Qc': u'M', u'Unit': u'(%)', u'Value': None},
                u'DaySoilTmpAvg': {u'Qc': u'M', u'Unit': u'(F)', u'Value': None},
                u'DayAirTmpAvg': {u'Qc': u'M', u'Unit': u'(F)', u'Value': None},
                u'DayRelHumAvg': {u'Qc': u'M', u'Unit': u'(%)', u'Value': None}}],
            u'Type': u'station',
            u'Name': u'cimis'}]}}
"""
