__author__ = 'kenhopwood'

# ET0 Service
# 18-OCT-2015
# K.Hopwood

from cimiset0 import get_cimis_eto_daily

def etosvc(key, targets, start_date, end_date):
    return get_cimis_eto_daily(key, targets, start_date, end_date)
