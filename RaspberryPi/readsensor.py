#!/usr/bin/python

import math
import time
import sys

if len(sys.argv) < 2:
	print 'Usage: ' + sys.argv[0] + ' mpu|lsm [print|plotly|matplot]'
	sys.exit()

if sys.argv[1] == 'mpu':
	from mpu6050api import *
elif sys.argv[1] == 'lsm':
	from lsm9ds0api import *
else:
	from dummysensor import *

if len(sys.argv) > 2:
	if sys.argv[2] == 'plotly':
		from plotlyOut import *
	elif sys.argv[2] == 'matplot':
		from matplotOut import *
	else:
		from printOut import *
else:
	from printOut import *


initOutput(["Accelerometer x", "Accelerometer y", "Accelerometer z"])
initSensor()

while True:
	ax, ay, az = readAccel()
	displayValues([ax, ay, az])
	time.sleep(0.01)






