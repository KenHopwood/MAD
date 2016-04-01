__author__ = 'kenhopwood'

# EWC Flow Task
# 01-FEB-2016
# K.Hopwood
# Copyright (c) 2016 All rights reserved.

from eyeo import Eyeo
import time
from data_dict import data
from threading import Thread

HIGH = 1
LOW = 0


class Task_flow(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.ey = Eyeo()

    def run(self):
        while True:
            # detect input changes and inc count
            state = self.ey.read_flow_meter()
            self.st = bool(data['lastflowpinstate'])
            self.tm = int(data['lastflowratetimer'])
            self.ct = int(data['pulse_count'])
            if (state == self.st):
                self.tm += 1
                data['lastflowratetimer'] = self.tm
                return

            if (state == HIGH):
                # low to high transition!
                self.ct += 1
                data['pulse_count'] = self.ct

            data['lastflowpinstate'] = state
            data['lastflowratetimer'] = 0
            time.sleep(.01)
        return
