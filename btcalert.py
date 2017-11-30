import notify2
import rates

def notify():
	ICON_PATH = "/Home/Scripts/Btcalert/btcalert/btcusd.jpg"

	#get current course
	bitcoin = rates.toTheMoon()

	#create D-Bus connection
	notify2.init("Cryptocurrency rates notifier")

	#create notification object
	n = notify2.Notification("Crypto Notifier", icon = ICON_PATH)

	#set notification level
	n.set_urgency(notify2.URGENCY_NORMAL)

	#set timeout
	n.set_timeout(1000)

	#update data
	n.update("Current rate BTC | USD", str(bitcoin))

	#show notification
	n.show()

if __name__ == "__main__":
	notify()
