from bs4 import BeautifulSoup
import requests

def fetch_bitcoin():

	#url with current course
	url = "https://www.coingecko.com/en/price_charts/bitcoin/usd"
	headers = {'User-Agent':'Mozilla/5.0'}
	bitcoin_file = requests.get(url)
	
	#debug
	file = open('debug.txt','w')
	file.write(bitcoin_file.text)
	file.close()

	#create soup object
	soup = BeautifulSoup(bitcoin_file.text, "html.parser")
	bitcoin_li = []

	#get data from tegs
	for table in soup.find_all("table", attrs={"class":"table table-responsive mt-2"}):
		for td in table.find_all("td"):
			bitcoin_li.append(td.text)
	del bitcoin_li[3:]

	#deleting useless chars
	bitcoin_li = map(lambda s : s.strip(), bitcoin_li)
	return bitcoin_li
