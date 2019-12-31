from utils.LED import *
from utils.ultra import *
from utils.driverI2C import *
from utils.balance import *
from utils.poten import *

import os
import time
import serial

fichier=open("somme.txt","r")
somme=float(fichier.read())
fichier.close()

setText("Vous avez "+str(somme)+" euros")
time.sleep(2)

while True:

	serialArduino=serial.Serial('/dev/ttyACM0',38400)
	print("guillaume")

	#Cas LED
	if dist_ultra_interne()<10:
		allume()
	else:
		eteindre()

	if dist_ultra_externe()<50:
		setText("Inserer\nRetirer")
		time.sleep(4)
		ch=choix()
		
		if ch==1:
			setText("Inserez une piece")
			time.sleep(5)
			print("coucou")
			
			convers = conversion(serialArduino)
			print("conv="+str(convers))
			somme+=float(convers)
			print("la")
			setText("Vous avez "+str(somme)+" euros")
			print("ici")
	time.sleep(2)
