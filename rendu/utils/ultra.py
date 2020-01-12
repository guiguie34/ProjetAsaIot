# GrovePi + Grove Ultrasonic Ranger

from grovepi import *

# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND

ultrasonic_interne = 6
ultrasonic_externe = 4

def dist_ultra_interne():
  
        return ultrasonicRead(ultrasonic_interne)

def dist_ultra_externe():
	
	return ultrasonicRead(ultrasonic_externe)



