from utils.LED import *
from utils.ultra import *

import time

while True:

	#On allume la LED si la tirelire est pleine
	if dist_ultra_interne()<3:
		allume()
	else:
		eteindre()

	time.sleep(2)
