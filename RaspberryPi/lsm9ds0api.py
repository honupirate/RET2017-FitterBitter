#!/usr/bin/python

# based on berryIMU-simple.py from https://github.com/mwilliams03/BerryIMU

import smbus
import math
from LSM9DS0 import *


RAD_TO_DEG = 57.29578
M_PI = 3.14159265358979323846
G_GAIN = 0.070  # [deg/s/LSB]  If you change the dps for gyro, you need to update this value accordingly
AA =  0.40      # Complementary filter constant



def writeACC(register,value):
	bus.write_byte_data(ACC_ADDRESS , register, value)
	return -1


def readACCx():
	acc_l = bus.read_byte_data(ACC_ADDRESS, OUT_X_L_A)
	acc_h = bus.read_byte_data(ACC_ADDRESS, OUT_X_H_A)
	acc_combined = (acc_l | acc_h <<8)
	return acc_combined  if acc_combined < 32768 else acc_combined - 65536

def readACCy():
	acc_l = bus.read_byte_data(ACC_ADDRESS, OUT_Y_L_A)
	acc_h = bus.read_byte_data(ACC_ADDRESS, OUT_Y_H_A)
	acc_combined = (acc_l | acc_h <<8)
	return acc_combined  if acc_combined < 32768 else acc_combined - 65536

def readACCz():
	acc_l = bus.read_byte_data(ACC_ADDRESS, OUT_Z_L_A)
	acc_h = bus.read_byte_data(ACC_ADDRESS, OUT_Z_H_A)
	acc_combined = (acc_l | acc_h <<8)
	return acc_combined  if acc_combined < 32768 else acc_combined - 65536


	
def readMAGx():
	mag_l = bus.read_byte_data(MAG_ADDRESS, OUT_X_L_M)
	mag_h = bus.read_byte_data(MAG_ADDRESS, OUT_X_H_M)
	mag_combined = (mag_l | mag_h <<8)
	return mag_combined  if mag_combined < 32768 else mag_combined - 65536

def readMAGy():
	mag_l = bus.read_byte_data(MAG_ADDRESS, OUT_Y_L_M)
	mag_h = bus.read_byte_data(MAG_ADDRESS, OUT_Y_H_M)
	mag_combined = (mag_l | mag_h <<8)
	return mag_combined  if mag_combined < 32768 else mag_combined - 65536

def readMAGz():
	mag_l = bus.read_byte_data(MAG_ADDRESS, OUT_Z_L_M)
	mag_h = bus.read_byte_data(MAG_ADDRESS, OUT_Z_H_M)
	mag_combined = (mag_l | mag_h <<8)
	return mag_combined  if mag_combined < 32768 else mag_combined - 65536



def readGYRx():
	gyr_l = bus.read_byte_data(GYR_ADDRESS, OUT_X_L_G)
	gyr_h = bus.read_byte_data(GYR_ADDRESS, OUT_X_H_G)
	gyr_combined = (gyr_l | gyr_h <<8)
	return gyr_combined  if gyr_combined < 32768 else gyr_combined - 65536

def readGYRy():
	gyr_l = bus.read_byte_data(GYR_ADDRESS, OUT_Y_L_G)
	gyr_h = bus.read_byte_data(GYR_ADDRESS, OUT_Y_H_G)
	gyr_combined = (gyr_l | gyr_h <<8)
	return gyr_combined  if gyr_combined < 32768 else gyr_combined - 65536

def readGYRz():
	gyr_l = bus.read_byte_data(GYR_ADDRESS, OUT_Z_L_G)
	gyr_h = bus.read_byte_data(GYR_ADDRESS, OUT_Z_H_G)
	gyr_combined = (gyr_l | gyr_h <<8)
	return gyr_combined  if gyr_combined < 32768 else gyr_combined - 65536




bus = 0

def initSensor():
	global bus
	bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards

	#initialise the accelerometer
	writeACC(CTRL_REG1_XM, 0b01100111) #z,y,x axis enabled, continuos update,  100Hz data rate
	writeACC(CTRL_REG2_XM, 0b00100000) #+/- 16G full scale


def readAccelX():
	return readACCx()

def readAccelY():
	return readACCy()

def readAccelZ():
	return readACCz()

def readAccel():
	return readAccelX(), readAccelY(), readAccelZ()

def readScaledAccel():
	ax, ay, az = readAccel()
	scale = math.sqrt(ax * ax + ay * ay + az * az)
	return ax/scale, ay/scale, az/scale


def readGyroX():
	return readGYRx()

def readGyroY():
	return readGYRy()

def readGyroZ():
	return readGYRy()
	
def readGyro():
	return readGyroX(), readGyroY(), readGyroZ()
	
def readScaledGyro():
	ax, ay, az = readGyro()
	scale = G_GAIN
	return ax*scale, ay*scale, az*scale


def readMagX():
	return readMAGx()

def readMagY():
	return readMAGy()

def readMagZ():
	return readMAGz()

def readMag():
	return readMagX(), readMagY(), readMagZ()

def readScaledMag():
	return readMag()

