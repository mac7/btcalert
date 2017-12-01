from bs4 import BeautifulSoup
import requests

def toTheMoon():

	#url with current course
	url = "http://ratesbtc.com/BTC/USD"
	headers = {'User-Agent':'Mozilla/5.0'}
	bitcoin_file = requests.get(url)

	#create soup object
	soup = BeautifulSoup(bitcoin_file.text, "html.parser")

	return round(float(str(soup.find_all("input", attrs={"id":"curPrice"})).split('"')[7]), 2)

