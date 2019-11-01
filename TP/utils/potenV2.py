import time
import grovepi

# Connect the Grove Rotary Angle Sensor to analog port A0
# SIG,NC,VCC,GND
potentiometer = 0

grovepi.pinMode(potentiometer,"INPUT")
time.sleep(1)

# Reference voltage of ADC is 5v
adc_ref = 5

# Vcc of the grove interface is normally 5v
grove_vcc = 5

# Full value of the rotary angle is 300 degrees, as per it's specs (0 to 300)
full_angle = 300

def pot():
	return  grovepi.analogRead(potentiometer)

def conversion():

	piece=grovepi.analogRead(potentiometer)
	print (piece)
	rep=0
	if piece<125:
		rep=0.01
		return rep
	elif piece>124 and piece<250:
		rep=0.02
		return rep
	elif piece>249 and piece<375:
		rep=0.05
		return rep
	elif piece>374 and piece<500:
		rep=0.1
		return rep
	elif piece>499 and piece<625:
		rep=0.2
		return rep
	elif piece>624 and piece<750:
		rep=0.5
		return rep
	elif piece>749 and piece<875:
		rep=1.0
		return rep
	else:
		rep=2.0
		return rep


