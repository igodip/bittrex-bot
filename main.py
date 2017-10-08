from bittrex import Bittrex
import json
import time
from datetime import datetime

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

key = "230cd2aaff354c43a3219a978ac2aebd"
secret = "fe11c3a0a7d14020bb78554ceb67de76"

bittrex = Bittrex(key,secret)

threshold_activ = 0.6 # Number between -1 and 1
threshold_off   = -0.2 # Number between -1 and 1

btc_vault = 0.0 # Btc vault
usdt_vault = 10000 # Usd tether vault

sell_pos = 0
buy_pos = 0

while True:

	results = bittrex.get_market_history('USDT-BTC',800)['result']

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

	# Strategy
	
	ratio = (buys_size - sells_size)/(buys_size+sells_size)

	# Check buy 
	if buy_pos == 0:
		if ratio > threshold_activ:
			btc_vault += usdt_vault/latest_price_ask
			usdt_vault = 0
			buy_pos = 1
	elif buy_pos == 1:
		if ratio < threshold_off:
			buy_pos = 0

	# Check sell
	if sell_pos == 0:
		if ratio < -threshold_activ:
			usdt_vault += btc_vault*latest_price_bid
			btc_vault = 0
			sell_pos = 1
	elif sell_pos == 1:
		if ratio > -threshold_off:
			sell_pos = 1



	print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
	print(" Buys   : %10d %8f" % (buys,buys_size))
	print(" Sells  : %10d %8f" % (sells,sells_size))
	print(" Ratio  : %10f" % ratio)
	print("Bitcoin price: BID:%10f ASK:%10f" % (latest_price_bid, latest_price_ask))
	print("BTC vault: %8f USDT vault: %8f Total value: %8f" %(btc_vault,usdt_vault,usdt_vault + btc_vault * latest_price_bid))
	print("")
	time.sleep(60)
