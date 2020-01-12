import serial

def conversion(serialArduino):

        try:
                val=float(serialArduino.readline()[:-2])
        except:
                return 0

	diff=abs(val)
	print("Envoi : " +str(val))

	if val<0:
		signe=-1
	else:
		signe=1

	if 1.9<=diff and diff<=2.3:
		piece=0.01
	elif 2.6<=diff and diff<=3.0:
		piece=0.02
	elif 3.4<=diff and diff<=3.7:
		piece=0.05
	elif 3.72<diff and diff<=4:
		piece=0.1
	elif 5<=diff and diff<=5.6:
		piece=0.2
	elif 7.01<=diff and diff<=7.4:
		piece=0.5
	elif 6.7<=diff and diff<=7:
		piece=1
	elif 7.6<=diff and diff<=8.1:
		piece=2
	else:
		piece=0

	return piece*signe

