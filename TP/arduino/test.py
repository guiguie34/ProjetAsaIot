import serial
from driverI2C import *
import time
import os

serialArduino= serial.Serial('/dev/ttyACM0', 38400)
#os.system('i2cset -y 1 0x3e 0x80 0x01')
while True:
	setRGB(255,255,0)
	setText(serialArduino.readline())

