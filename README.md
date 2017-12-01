setup: 

	sudo apt-get install git python-pip && git clone https://github.com/mac7/btcalert.git && sudo pip install notify2 requests beautifulsoup4 

run: 

	python btcalert/btcalert.py
