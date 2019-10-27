import serial 

serialArduino= serial.Serial('/dev/ttyACM0', 9600)

while True:
	print(serialArduino.readline())
