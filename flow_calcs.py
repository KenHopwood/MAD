# EWC Flow Measurement
# 17-FEB-2016
# K.Hopwood
# Copyright (c) 2016 All rights reserved.

from data_dict import data


class CalcFlow:
    liters = 0

    def __init__(self):
        self.liters = data['pulse_count']

    def run(self):
        self.liters /= 7.5
        self.liters /= 60.0
        data['flow_delivered'] = self.liters
        return
