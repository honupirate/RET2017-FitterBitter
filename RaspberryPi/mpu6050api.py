#!/usr/bin/python

# based on 32_mpu6050.py from https://www.sunfounder.com/learn/category/sensor-kit-v2-0-for-raspberry-pi-b-plus.html

import smbus
import math


# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c


def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val



bus = 0
address = 0

def initSensor():
	global bus, address
	bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
	address = 0x68       # This is the address value read via the i2cdetect command

	# Now wake the 6050 up as it starts in sleep mode
	bus.write_byte_data(address, power_mgmt_1, 0)


def readAccelX():
	return read_word_2c(0x3b)

def readAccelY():
	return read_word_2c(0x3d)

def readAccelZ():
	return read_word_2c(0x3f)

def readAccel():
	return readAccelX(), readAccelY(), readAccelZ()

def readScaledAccel():
	ax, ay, az = readAccel()
	scale = 16384.0
	return ax/scale, ay/scale, az/scale


def readGyroX():
	return read_word_2c(0x43)


def readGyroY():
	return read_word_2c(0x45)


def readGyroZ():
	return read_word_2c(0x47)

	
def readGyro():
	return readGyroX(), readGyroY(), readGyroZ()

	
def readScaledGyro():
	ax, ay, az = readGyro()
	scale = 131.0
	return ax/scale, ay/scale, az/scale

