import time
from grovepi import *

# Connect the Grove LED to digital port D5
led = 4

def allume():
	return digitalWrite(led,1)

def eteindre():
	return digitalWrite(led,0)


