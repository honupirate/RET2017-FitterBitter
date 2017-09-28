import random

def initSensor():
	print "Initialization Successful"


def readAccel():
	return random.uniform(0,1), random.uniform(0,1), random.uniform(0,1)


def readScaledAccel():
	return readAccel()


def readGyro():
	return random.uniform(0,1), random.uniform(0,1), random.uniform(0,1)

def readScaledGyro():
	return readGyro()
