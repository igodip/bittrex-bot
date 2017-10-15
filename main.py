#!/usr/bin/env python

import logging

from multiprocessing import Process, freeze_support
from bittrex import Bittrex
import requests.packages.urllib3

from account import key, secret, currencies
from market_manager import markets
from worker.collector import Collector

# Really annoy warning, this library is deprecated need to switch

requests.packages.urllib3.disable_warnings()


# Yo man, the most important and cool function

def work(worker):
    worker.run()

    return


collectors = []

# Enable logging by module / class

logging.basicConfig(filename="example.log")
Collector.logger.setLevel(logging.DEBUG)


# Main function

def main():
    bittrex = Bittrex(key, secret)

    # Get all balances
    msg = bittrex.get_balances()

    if msg["success"]:

        for i in msg["result"]:
            currencies[i["Currency"]].balance.available = i["Available"]
            currencies[i["Currency"]].balance.pending = i["Pending"]
            currencies[i["Currency"]].balance.balance = i["Balance"]
            currencies[i["Currency"]].balance.crypto_address = i["CryptoAddress"]

        print("Imported balances!")

    #msg = bittrex.get_open_orders()
    #print(msg)

    for (k,i) in markets.iteritems():
        c = Collector(bittrex, i)

        freeze_support()
        p = Process(target=work, args=(c,))
        p.start()

        collectors.append((c, p))

    print("Started collectors on markets!")


if __name__ == "__main__":
    print("Starting  ...")
    main()
    print("Started!")
