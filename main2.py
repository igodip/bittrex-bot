from bittrex import Bittrex
import json
import time
from datetime import datetime

import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()

import sqlite3

conn = sqlite3.connect('bitcoin.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS history
             (time INTEGER, bid REAL,ask REAL,bought REAL,sold REAL,buys INTEGER,sells INTEGER)''')

key = "230cd2aaff354c43a3219a978ac2aebd"
secret = "fe11c3a0a7d14020bb78554ceb67de76"

bittrex = Bittrex(key, secret)

print(bittrex.get_balances())
