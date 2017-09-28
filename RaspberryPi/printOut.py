
datalabels = []

def initOutput(labels):
	global datalabels
	datalabels = labels


def displayValues(data):
	global datalabels
	if len(data) != len(datalabels):
		print 'Length of data and labels do not match'
		return

	for l,d in zip(datalabels, data):
		print l + ': ' + str(d), 
	print

