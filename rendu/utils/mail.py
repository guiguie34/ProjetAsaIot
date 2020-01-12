import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def envoiMail(valeur):
	expediteur = "raspberry.tirelire@gmail.com"
	destinataire = "guillaume.dufour@etu.umontpellier.fr"
	message = MIMEMultipart()
	message['From'] = expediteur
	message['Subject'] = "Montant dans votre tirelire"
	msg = "Votre tirelire contient "+str(valeur)+" euros"
	message.attach(MIMEText(msg.encode('utf-8'),'plain','utf-8'))

	serveur = smtplib.SMTP("smtp.gmail.com", 587)
	serveur.starttls()
	serveur.login(expediteur, 'tirelire23')
	texte = message.as_string().encode('utf-8')
	serveur.sendmail(expediteur,destinataire,texte)
	serveur.quit()
