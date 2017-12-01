#! /usr/bin/python


import notify2
import rates
import time

def notify():
	ICON_PATH = "/Home/Scripts/Btcalert/btcalert/btcusd.jpg"

	#create D-Bus connection
	notify2.init("Cryptocurrency rates notifier")

	#create notification object
	n = notify2.Notification("Crypto Notifier", icon = ICON_PATH)

	#set notification level
	n.set_urgency(notify2.URGENCY_NORMAL)

	while True:

		#get current course
        	bitcoin = rates.toTheMoon()

		#set timeout
		n.set_timeout(1000)

		#update data
		n.update("Current rate BTC | USD", str(bitcoin))

		#show notification
		n.show()

		#delay
		time.sleep(600)

if __name__ == "__main__":
	notify()
