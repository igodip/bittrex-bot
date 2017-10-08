from bittrex import Bittrex
import json
import time
from datetime import datetime

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

key = "230cd2aaff354c43a3219a978ac2aebd"
secret = "fe11c3a0a7d14020bb78554ceb67de76"

bittrex = Bittrex(key,secret)

#print(bittrex.get_currencies())

#markets = bittrex.get_markets()
#print(json.dumps(markets, indent=4, sort_keys=True))

while True:

	results = bittrex.get_market_history('USDT-BTC',100)['result']

	buys = 0
	sells = 0

	buys_size = 0
	sells_size = 0

	latest_price_bid = 0
	latest_price_ask = 0

	for i in results:

		if i['OrderType'] == 'BUY':
			buys += 1
			buys_size += i['Quantity']
			
			if latest_price_ask == 0:
				latest_price_ask = i['Price']
		else:
			sells += 1
			sells_size += i['Quantity']

			if latest_price_bid == 0:
				latest_price_bid = i['Price']		

	print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
	print(" Buys   : %10d %8f" % (buys,buys_size))
	print(" Sells  : %10d %8f" % (sells,sells_size))
	print("Bitcoin price: BID:%10f ASK:%10f" % (latest_price_bid, latest_price_ask))
	print("")
	time.sleep(60)
