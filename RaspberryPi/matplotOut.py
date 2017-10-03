# based on sample code from https://hardsoftlucid.wordpress.com/various-stuff/realtime-plotting/

#!/usr/bin/python

import pylab
from pylab import *

xshow = 200 # window of data points

xAchse=pylab.arange(0,xshow,1)
yAchse=pylab.array([0]*xshow)

fig=pylab.figure(1)
ax = fig.add_subplot(111)
lines = []
manager = pylab.get_current_fig_manager()


datalabels=[]
x=[]
ys=[]
numdata = 0

def initOutput(labels):
	global datalabels, ax, lines, xAchse, yAchse, ys, numdata
	ax.set_title("Realtime Plot")
	ax.set_xlabel("Time")
	ax.set_ylabel("Accelerometer")
	ax.axis([0,xshow,-1.5,1.5])

	datalabels = labels
	numdata = len(labels)
	for l in labels:
		line, = ax.plot(xAchse, yAchse, '-', label=l)
		lines.append(line)
		ys.append([])
	plt.legend(handles=lines)


t = 0
ymin = 1000000
ymax = -1000000

def displayValues(data):
	global t, x, ys, lines, xshow, numdata, ymin, ymax
	if len(data) != len(datalabels):
		print 'Length of data and labels do not match'
		return

	x.append(t)
	ymin = 1000000
	ymax = -1000000
	for i in range(numdata):
		ys[i].append(data[i])
		lines[i].set_data(x[-xshow:],ys[i][-xshow:])
		if min(ys[i][-xshow:]) < ymin:
			ymin = min(ys[i][-xshow:])
		if max(ys[i][-xshow:]) > ymax:
			ymax = max(ys[i][-xshow:])
		#if data[i] < ymin:
		#	ymin = data[i]
		#if data[i] > ymax:
		#	ymax = data[i]

	ax.axis([t-xshow,t,ymin,ymax])
	t += 1
	#plt.draw()
	manager.canvas.draw()
	plt.pause(0.0001)


