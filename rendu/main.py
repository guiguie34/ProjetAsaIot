from utils.LED import *
from utils.ultra import *
from utils.driverI2C import *
from utils.balance import *
from utils.poten import *
from utils.bouton import *
from utils.mail import *

import os
import time
import serial

fichier=open("somme.txt","r")
somme=float(fichier.read())
fichier.close()


serialArduino=serial.Serial('/dev/ttyACM0',38400,timeout=5)

setRGB(0,255,0)
setText("Vous avez\n"+str(somme)+" euros")
time.sleep(2)

envoi_mail=0

while True:

	if dist_ultra_interne()>3:

		if dist_ultra_externe()<30:

			setRGB(0,255,0)
			setText("Vous avez\n"+str(somme)+" euros")
			time.sleep(2)

                        setText("Choisir : mettre ou retirer")
                        time.sleep(4)

                        if choix()==1:
                                action="Mettre"
                        else:
                                action="Retirer"

                        setText(action+" une piece 5")
                        time.sleep(1)
                        setText(action+" une piece 4")
                        time.sleep(1)
                        setText(action+" une piece 3")
                        time.sleep(1)
                        setText(action+" une piece 2")
                        time.sleep(1)
                        setText(action+" une piece 1")
                        time.sleep(1)

                        setText("Calcul en cours")

                        convers = conversion(serialArduino)
                        print("conv="+str(convers))
                        somme+=convers			
                        setText("Vous avez\n"+str(somme)+" euros")
                        time.sleep(5)
			action = actionBouton(serialArduino)
			print(action)
			if action=="oui":
				somme-=convers
				setText("Vous avez\n"+str(somme)+" euros")
				time.sleep(3)
			
			fichier=open("somme.txt","w")
			fichier.write(str(somme))
			fichier.close()
			envoi_mail=1
		else:
			setRGB(0,0,0)
	                setText("")

			if envoi_mail==1:
				envoiMail(somme)
				envoi_mail=0
	else:
		setRGB(255,0,0)
		setText("Votre tirelire\nest pleine")
			
