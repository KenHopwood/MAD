__author__ = 'kenhopwood'

# EWC Canopy Temperature
# 01-FEB-2016
# K.Hopwood
# Copyright (c) 2016 All rights reserved.
#
# Inspired by MLX90614.CPP by J. F. Fitter https://github.com/jfitter/MLX90614.git

from periphery import I2C
import time


class Canopy_temp:
    def __init__(self):
        self.AMB = 0x06
        self.SRC1 = 0x07
        self.SRC2 = 0x08
        self.addr = 0x62
        # self.addr = 0x5a
        # self.addr = 0x00

        self.bus = 0
        self.device = 1  # 0, 1, 3, 7

        self.bus = I2C("/dev/i2c-%s" % self.device)  # Opens /dev/i2c-{dev}
        msgs = [I2C.Message([0x00, self.AMB], read=True)]
        self.bus.transfer(self.addr, msgs)
        print "read i2c:", msgs[0].data[1], msgs[0].data[0]
        return

    def read_temp_ambient(self):
        self.bus = I2C("/dev/i2c-%s" % self.device)  # Opens /dev/i2c-{dev}
        print "bus", self.bus
        # msgs = [I2C.Message([0x00, self.AMB]), I2C.Message([0x00, 0x00], read=True)]
        msgs = [I2C.Message([0x00, self.AMB], read=True)]
        self.bus.transfer(self.addr, msgs)
        temp = msgs[0].data[0]
        temp1 = msgs[0].data[1]
        print "Ambient raw: ", temp, temp1
        temp2 = (temp << 8) | temp1
        print "Ambient: ", temp2
        temp2 *= 0.02
        print "Ambient scaled: ", temp2
        return temp2 - 273.15

    def read_temp_source1(self):
        self.bus = I2C("/dev/i2c-%s" % self.device)  # Opens /dev/i2c-{dev}
        # msgs = [I2C.Message([0x00, self.SRC1]), I2C.Message([0x00, 0x00], read=True)]
        msgs = [I2C.Message([0x00, self.SRC1], read=True)]
        self.bus.transfer(self.addr, msgs)
        temp = msgs[0].data[0]
        temp1 = msgs[0].data[1]
        print "Source1 raw: ", temp, temp1
        temp2 = (temp << 8) | temp1
        print "Source1: ", temp2
        temp2 *= 0.02
        print "Source1 scaled: ", temp2
        return temp2 - 273.15

    def read_temp_source2(self):
        self.bus = I2C("/dev/i2c-%s" % self.device)  # Opens /dev/i2c-{dev}
        msgs = [I2C.Message([0x00, self.SRC2]), I2C.Message([0x00, 0x00], read=True)]
        self.bus.transfer(self.addr, msgs)
        temp = msgs[1].data[0]
        temp1 = msgs[1].data[1]
        print "Source2 raw: ", temp, temp1
        temp2 = (temp << 8) | temp1
        print "Source2: ", temp2
        temp2 *= 0.02
        print "Source2 scaled: ", temp2
        return temp2 - 273.15

    def close(self):
        self.bus = I2C("/dev/i2c-%s" % self.device)  # Opens /dev/i2c-{dev}
        self.bus.close()

    def read_eeprom(self):
        self.bus = I2C("/dev/i2c-%s" % self.device)  # Opens /dev/i2c-{dev}

        for offset in range(0x20, 0x24):
            msgs = [I2C.Message([0x00, offset]), I2C.Message([0x00, 0x00], read=True)]
            self.bus.transfer(self.addr, msgs)
            temp = msgs[1].data[0]
            temp1 = msgs[1].data[1]
            print offset, ":", temp, temp1
            temp2 = (temp << 8) | temp1
            print offset, ":", temp2
        return


"""

/**
 *  \brief            Return a 16 bit value read from RAM or EEPROM.
 *  \param [in] cmd   Command to send (register to read from).
 *  \return           Value read from memory.
 */
uint16_t MLX90614::read16(uint8_t cmd) {
    uint16_t val;
    CRC8 crc(MLX90614_CRC8POLY);
-----------
    // send the slave address then the command and set any
    // error status bits returned by the write
    Wire.beginTransmission(_addr);
    Wire.write(cmd);
    _rwError |= (1 << Wire.endTransmission(false)) >> 1;

    // experimentally determined delay to prevent read errors
    // (manufacturer's data sheet has left something out)
    delayMicroseconds(MLX90614_XDLY);

    // resend slave address then get the 3 returned bytes
    Wire.requestFrom(_addr, (uint8_t)3);

-----------

    // data is returned as 2 bytes little endian
    val = Wire.read();
    val |= Wire.read() << 8;

    // read the PEC (CRC-8 of all bytes)
    _pec = Wire.read();

    // build our own CRC-8 of all received bytes
    crc.crc8(_addr << 1);
    crc.crc8(cmd);
    crc.crc8((_addr << 1) + 1);
    crc.crc8(lowByte(val));
    _crc8 = crc.crc8(highByte(val));

    // set error status bit if CRC mismatch
    if(_crc8 != _pec) _rwError |= MLX90614_RXCRC;

    return val;
}





def init(dev):
    print "SMBus Init device ", dev
    bus = smbus.SMBus(dev)  # Opens /dev/i2c-{dev}
    print bus
    bus.write_byte_data(I2C_ADDR, 0x13, 0xff)
    return bus


def read_temp_source1(bus):
    temp = bus.read_byte_data(I2C_ADDR, SRC1)
    temp *= 0.02
    print "Source1: ", temp - 273.15
    return temp - 273.15


def read_temp_source2(bus):
    temp = bus.read_byte_data(I2C_ADDR, SRC2)
    temp *= 0.02
    print "Source2: ", temp - 273.15
    return temp - 273.15


def read_temp_ambient(bus):
    temp = bus.read_byte_data(I2C_ADDR, AMB)
    temp *= 0.02
    print "Ambient: ", temp - 273.15
    return temp - 273.15
"""
