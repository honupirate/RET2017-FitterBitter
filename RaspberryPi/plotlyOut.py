#!/usr/bin/python

import plotly.plotly as py
from plotly.graph_objs import Scatter, Layout, Figure

trace = []
stream = []
numdata = 0
datalabels = []

def initOutput(labels):
	global trace, stream, numdata, datalabels

	username = 'hsiy'
	api_key = 'y1YXzt7TIsc7RRY2TMAb'
	stream_token = ['2xc6yk9l09', 'euxrawpca5', 'ekbgwm6lcd']
	py.sign_in(username, api_key)

	linecolor = ['rgb(0,0,255)', 'rgb(255,0,0)', 'rgb(255,255,0)']
	datalabels = labels
	numdata = min(3, len(labels))
	for i in range(numdata):
		trace.append(Scatter(
			name=labels[i],
			x=[],
			y=[],
			stream=dict(
				token=stream_token[i],
				maxpoints=200
			), 
			marker=dict(
				color=linecolor[i]
			)
		)) 

	layout = Layout(
		title='Raspberry Pi Streaming Sensor Data'
	)
	fig = Figure(data=trace, layout=layout)
	print py.plot(fig, filename='Raspberry Pi Streaming Example Values')


	for i in range(numdata):
		stream.append(py.Stream(stream_token[i]))
		stream[i].open()


t = 0

def displayValues(data):
	global t, stream, numdata, datalabels
	if len(data) != len(datalabels):
		print 'Length of data and labels do not match'
		return

	for i in range(numdata):
		stream[i].write({'x': t, 'y': data[i]})
	t += 1


