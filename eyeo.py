__author__ = 'kenhopwood'

# EWC eyeo (io)
# 05-FEB-2016
# K.Hopwood
# Copyright (c) 2016 All rights reserved.
# inspired by sample code at http://developer.toradex.com/knowledge-base/python-in-linux

from data_dict import data
import os.path
import datetime

OPEN = 1
CLOSE = 0


class Eyeo:
    def __init__(self):
        self.GPIO_RESET = False  # Whether GPIOs should be re-exported
        self.GPIO_PATH = "/sys/class/gpio"
        self.GPIO_DIR_IN = "in"
        self.GPIO_DIR_OUT = "out"
        self.GPIO_VAL_HI = "1"
        self.GPIO_VAL_LO = "0"
        self.GPIO_VALVE_CHAN_NUM = "122"  # Valve Control Output
        self.GPIO_FLOW_CHAN_NUM = "123"  # Flow Meter Input

        # def init_io():
        # Open GPIO export & unexport files
        exportFile = open(self.GPIO_PATH + '/export', 'w')
        unexportFile = open(self.GPIO_PATH + '/unexport', 'w')

        # Valve Control Output
        # Unexport GPIO if it exists and GPIO_RESET is enabled
        exportExists = os.path.isdir(self.GPIO_PATH + '/gpio' + self.GPIO_VALVE_CHAN_NUM)
        if exportExists and self.GPIO_RESET:
            unexportFile.write(self.GPIO_VALVE_CHAN_NUM)
            unexportFile.flush()

        # Export GPIO
        if not exportExists or self.GPIO_RESET:
            exportFile.write(self.GPIO_VALVE_CHAN_NUM)
            exportFile.flush()

        # Open GPIO direction file to set direction
        directionFile = open(self.GPIO_PATH + '/gpio' + self.GPIO_VALVE_CHAN_NUM + '/direction', 'w')

        # Set GPIO direction to "out"
        directionFile.write(self.GPIO_DIR_OUT)
        directionFile.flush()

        # Open GPIO value file to set value
        self.fv = open(self.GPIO_PATH + '/gpio' + self.GPIO_VALVE_CHAN_NUM + '/value', 'w')
        print "fv:", self.fv

        # Flow Meter Input
        # Unexport GPIO if it exists and GPIO_RESET is enabled
        exportExists = os.path.isdir(self.GPIO_PATH + '/gpio' + self.GPIO_FLOW_CHAN_NUM)
        if exportExists and self.GPIO_RESET:
            unexportFile.write(self.GPIO_FLOW_CHAN_NUM)
            unexportFile.flush()

        # Export GPIO
        if not exportExists or self.GPIO_RESET:
            exportFile.write(self.GPIO_FLOW_CHAN_NUM)
            exportFile.flush()

        # Open GPIO direction file to set direction
        directionFile = open(self.GPIO_PATH + '/gpio' + self.GPIO_FLOW_CHAN_NUM + '/direction', 'w')

        # Set GPIO direction to "in"
        directionFile.write(self.GPIO_DIR_IN)
        directionFile.flush()

        # Open GPIO value file to set value
        self.ff = open(self.GPIO_PATH + '/gpio' + self.GPIO_FLOW_CHAN_NUM + '/value', 'r')
        print "ff:", self.ff
        return

    def control_valve(self, state):
        if (state == OPEN):
            # open valve solenoid
            self.fv.write(str(OPEN))
            data['valve_open'] = True
            today = datetime.date.today()
            moment = datetime.datetime.now().time()
            now = datetime.datetime.combine(today, moment)
            epoch = datetime.datetime.utcfromtimestamp(0)
            delta = now - epoch
            days = delta.days
            data['last_irrigation_day'] = days

        else:
            # close valve solenoid
            data['valve_open'] = False
            self.fv.write(str(CLOSE))
        return

    def read_flow_meter(self):
        val = self.ff.read()
        return val
