import serial

def actionBouton(serialArduino):

	action=serialArduino.readline()[:-2]

	return action
