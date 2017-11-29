import notify2
import rates

def notify():
	ICON_PATH = "btcusd.jpg"

	#get current course
	bitcoin = rates.fetch_bitcoin()

	#create D-Bus connection
	notify2.init("Cryptocurrency rates notifier")

	#create notification object
	n = notify2.Notification("Crypto Notifier", icon = ICON_PATH)

	#set notification level
	n.set_urgency(notify2.URGENCY_NORMAL)

	#set timeout
	n.set_timeout(1000)

	result = '{0}-{1}'.format(*bitcoin)

	#update data
	n.update("BTC2USD", result)

	#show notification
	n.show()

if __name__ == "__main__":
	notify()
