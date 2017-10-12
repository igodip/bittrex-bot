from bittrex import Bittrex
import json
import time
from datetime import datetime

import requests.packages.urllib3
import sqlite3

requests.packages.urllib3.disable_warnings()

conn = sqlite3.connect("bitcoin.db", check_same_thread = False)
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS history
             (time INTEGER, bid REAL,ask REAL,bought REAL,sold REAL,buys INTEGER,sells INTEGER)''')

key = "230cd2aaff354c43a3219a978ac2aebd"
secret = "fe11c3a0a7d14020bb78554ceb67de76"

bittrex = Bittrex(key, secret)

threshold_activ = 0.5  # Number between -1 and 1
threshold_off = -0.5  # Number between -1 and 1

btc_vault = 0  # Btc vault
usdt_vault = 10000  # Usd tether vault

max_spread = 20

sell_pos = 0
buy_pos = 0

while True:

    results = bittrex.get_market_history('USDT-BTC', 800)['result']

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

    ratio = (buys_size - sells_size) / (buys_size + sells_size)
    reasonable_spread = (latest_price_ask - latest_price_bid) < max_spread

    # Check buy
    if ratio > threshold_activ and reasonable_spread:
        btc_vault += usdt_vault / latest_price_ask
        usdt_vault = 0
        buy_pos = 1

    # Check sell
    if ratio < threshold_off and reasonable_spread:
        usdt_vault += btc_vault * latest_price_bid
        btc_vault = 0
        sell_pos = 1

    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print(" Buys   : %10d %8f" % (buys, buys_size))
    print(" Sells  : %10d %8f" % (sells, sells_size))
    print(" Ratio  : %10f" % ratio)
    print("Bitcoin price: BID:%10f ASK:%10f" % (latest_price_bid, latest_price_ask))
    print("BTC vault: %8f USDT vault: %8f Total value: %8f" % (
        btc_vault, usdt_vault, usdt_vault + btc_vault * latest_price_bid))
    print("")
    
    c.execute("INSERT INTO history (time,bid,ask,bought,sold,buys,sells) VALUES (%u, %f, %f, %f, %f, %d, %d)" % (time.time(),latest_price_bid,latest_price_ask,buys_size,sells_size,buys,sells ))
    conn.commit()

    time.sleep(30)

conn.close()

