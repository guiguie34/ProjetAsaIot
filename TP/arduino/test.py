import serial
from driverI2C import *
import time
import os

serialArduino= serial.Serial('/dev/ttyACM0', 38400)
os.system('i2cset -y 1 0x3e 0x80 0x01')
while True:
	setRGB(0,0,255)
	valeur=float(serialArduino.readline()[:-2])

	if valeur < 8:
		print("salut")
	else:
		print("fvnzkjgvnk")

