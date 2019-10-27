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
	rep=0
	if piece<100:
		rep=0.01
		return rep
	elif piece>99 and piece<200:
		rep=0.02
		return rep
	elif piece>199 and piece<300:
		rep=0.05
		return rep
	elif piece>299 and piece<400:
		rep=0.1
		return rep
	elif piece>399 and piece<500:
		rep=0.2
		return rep
	elif piece>499 and piece<600:
		rep=0.5
		return rep
	elif piece>599 and piece<700:
		rep=1.0
		return rep
	else:
		rep=2.0
		return rep


