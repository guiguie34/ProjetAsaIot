from utils.driverI2C import *
from utils.ultra import *
from utils.LED import *
from utils.poten import *
import time
import os
rep="oui"
montant=0.0
while True:
	try:
		setRGB(200,0,0)
		os.system('i2cset -y 0x3e 0x80 0x01')
		texte=str(conversion())
		setText("Ajouter " + texte + " euros?")
		rep=str(input())
		if rep=="oui":
			montant=montant+conversion()
			setText("Ajout de " + texte)
			time.sleep(2)
			setText("Montant total: " + str(montant)) 
		

		time.sleep(5)
	except KeyboardInterrupt:
		print(montant)
		os.system('i2cset -y 1 0x3e 0x80 0x01')
		break


