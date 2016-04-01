# EWC Water Calculations
# 01-FEB-2016
# K.Hopwood
# Copyright (c) 2016 All rights reserved.

from data_dict import data
import datetime

"""
Tc   - Canopy Temperature (MLX IR) (Deg C)
Ta   - Air Temperature (BME280) (Deg C)
Rn   - Radiation (???)
B    - Constant (wheat 0.064)
ETc  - Canopy Evapotranspiration (mm/time period)
ETo  - Reference Evapotranspiration (CIMIS) (mm/time period)
Kc   - Crop Coefficient (canopy cover as % of bed)
SDD  - Stress Degree Days (days)

ETc = Rn - B(Tc - Ta)

       n
SDD = Sigma (Tc - Ta)
       i=1

Applied Depth Inches = (GPM * hours) / (449 * acres)  # gal/acre

Surplus/Deficit = Required - Applied Depth

Kc = ETc / ETo

Water = Kc * ETo * Days Between Irrigation / Irrigation Efficiency (80-90%)  # ((mm/day)*day)/k #mm

"""


class CalcWater:
    def __init__(self):
        self.ie = 0.80  # Irrigation Efficiency
        self.b = 0.064

    def calc_water_needed(self):
        #self.ta = float(data['ambient'])
        #self.tc = float(data['canopy_temp'])
        #ToDo: test values
        self.ta = 40.0
        self.tc = 32.0
        print "b:", self.b
        print "tc:", self.tc
        print "ta:", self.ta
        self.etc = int(data['rn']) - self.b * (self.tc - self.ta)
        print "etc:", self.etc
        self.eto = float(data['eto'])
        if self.eto > 0:
            print "eto:", self.eto
            self.kc = self.etc / self.eto
            print "kc:", self.kc
        else:
            self.kc = 1

        #ToDo: add NTP client to set the time

        self.today = datetime.date.today()
        self.moment = datetime.datetime.now().time()
        self.now = datetime.datetime.combine(self.today, self.moment)
        self.epoch = datetime.datetime.utcfromtimestamp(0)
        self.delta = self.now - self.epoch
        self.days = self.delta.days
        print "days:", self.days
        print "LID:", int(data['last_irrigation_day'])
        self.dbi = self.days - int(data['last_irrigation_day'])
        # self.dbi = datetime.date.today() - datetime.timedelta(days = int(data['last_irrigation_day']))
        print "dbi:", self.dbi

        # water quantity evaporated == water needed
        # mm * 0.001 of water * m2 area = m3
        # convert to m3
        data['water_required'] = ((self.kc * self.eto * self.dbi * 0.001) * float(data['irrigation_area']) / self.ie) / 0.001
        #ToDo: mm of water; need to calc liters from mm*irrigation area (0.001m3 = 1 liter)
        print "water_required (l):", data['water_required']
        return
