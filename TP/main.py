# coding: utf-8

from utils.driverI2C import *
from utils.ultra import *
from utils.LED import *
from utils.poten import *
import time
import os



setText("Bienvenue dans la phase de test")
setRGB(0,128,64)
time.sleep(5)
setText("Lancement dans 3...")
time.sleep(1)
setText("2...")
time.sleep(1)
setText("1...")
time.sleep(1)
set("0 !")
setRGB(150,0,75)
time.sleep(0.5)
setRGB(0,150,200)
time.sleep(0.5)

while True: 
	try:
		print(dist_ultra())
		if dist_ultra()<50:
			setText("Proche")
			setRGB(200,0,0)
			allume()
		else:
			setText("Loin")
			setRGB(0,200,0)
			eteindre()
		time.sleep(1)	
	except KeyboardInterrupt:
		print("Leave")
		os.system('i2cset -y 1 0x3e 0x80 0x01')
		setRGB(0,0,0)
		eteindre()
		break 


#for c in range(0,200):
#	setRGB(c,200-c,0)
#	time.sleep(0.1)
#setText("Bye!")
