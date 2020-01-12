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

#Recuperation de la somme presente dans la tirelire ecrite dans un fichier
fichier=open("somme.txt","r")
somme=float(fichier.read())
fichier.close()


#Connexion avec l'Arduino
serialArduino=serial.Serial('/dev/ttyACM0',38400,timeout=5)

#Indication de la somme à l'ecran avec ecran de couleur verte
setRGB(0,255,0)
setText("Vous avez\n"+str(somme)+" euros")
time.sleep(2)

#Valeur permettant d'envoyer un mail, 1 veut dire qu'il faut envoyer un mail, 0 pas d'envoi
envoi_mail=0

while True:

	#Si la tirelire est pleine, ne propose pas à l'utilisateur de faire une action
	if dist_ultra_interne()>3:

		#Regarde si l'utilisateur est present devant la tirelire
		if dist_ultra_externe()<30:

			#Indication de la somme à l'ecran avec ecran de couleur verte
			setRGB(0,255,0)
			setText("Vous avez\n"+str(somme)+" euros")
			time.sleep(2)

			#Choix à faire
                        setText("Choisir : mettre ou retirer")
                        time.sleep(4)

                        if choix()==1:
                                action="Mettre"
                        else:
                                action="Retirer"

			#L'utilisateur a 5 secondes pour executer l'action qu'il a choisi
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

			#Appel de la fonction permettant de convertir le poids en valeur de piece
                        convers = conversion(serialArduino)

			#On ajoute/retire la valeur de la piece inseree/retiree
                        somme+=convers

			#Affichage de la nouvelle valeur
                        setText("Vous avez\n"+str(somme)+" euros")

			#L'utilisateur a 5 secondes pour appuyer sur le bouton pour annuler l'action
                        time.sleep(5)

			#Recuperation de la valeur du bouton
			action = actionBouton(serialArduino)

			#Si l'utilisateur a appuye, on annule la derniere action
			if action=="oui":
				somme-=convers

				#Affichage de la somme apres correction
				setText("Vous avez\n"+str(somme)+" euros")
				time.sleep(3)

			#Ecriture de la nouvelle somme dans le fichier			
			fichier=open("somme.txt","w")
			fichier.write(str(somme))
			fichier.close()
			envoi_mail=1

		#On entre dans le else si l'utilisateur n'est pas devant la tirelire
		else:
			#On assombrit l'ecran
			setRGB(0,0,0)
	                setText("")


			#Envoi de la valeur par mail si la valeur a ete modifiee depuis le dernier envoi
			if envoi_mail==1:
				envoiMail(somme)
				envoi_mail=0
	else:
		#Si la tirelire est pleine, on affichage un message sur un ecran rouge
		setRGB(255,0,0)
		setText("Votre tirelire\nest pleine")
			
