__author__ = 'kenhopwood'

# EWC Second Task
# 08-FEB-2016
# K.Hopwood
# Copyright (c) 2016 All rights reserved.

import time
from data_dict import data
from flow_calcs import CalcFlow
from eyeo import Eyeo
import datetime
from threading import Thread

OPEN = 1
CLOSE = 0


class Task_second(Thread):
    def __init__(self):
        Thread.__init__(self)
        print "Task_second init"
        self.ey = Eyeo()

    def run(self):
        while (True):
            # calc flow
            CalcFlow()

            # do valve control
            if (bool(data['valve_open']) == True):
                if (float(data['flow_delivered']) >= float(data['water_required'])):
                    # close valve
                    self.ey.control_valve(CLOSE)

            time.sleep(1)
        return
