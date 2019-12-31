import serial

oldVal = 0

def conversion(serialArduino):

	global oldVal

	diff=float(serialArduino.readline()[:-2])

	if 2.1<=diff and diff<=2.3:
		piece=0.01
	elif 2.8<=diff and diff<=3.0:
		piece=0.02
	elif 3.6<=diff and diff<=3.8:
		piece=0.05
	elif 3.8<diff and diff<=4:
		piece=0.1
	elif 5.4<=diff and diff<=5.6:
		piece=0.2
	elif 7.25<=diff and diff<=7.45:
		piece=0.5
	elif 7<=diff and diff<=7.2:
		piece=1
	elif 7.8<=diff and diff<=8.1:
		piece=2
	else:
		piece=diff

	return piece

