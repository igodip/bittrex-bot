#!/usr/bin/env python

import logging

from multiprocessing import Process, freeze_support
from bittrex import Bittrex
import requests.packages.urllib3

from account import key, secret, currencies
from market_manager import markets
from model.currency import Currency
from model.market import Market
from worker.collector import Collector

# Really annoy warning, this library is deprecated need to switch
from worker.general_collector import GeneralCollector

requests.packages.urllib3.disable_warnings()


# Yo man, the most important and cool function

def work(worker):
    worker.run()

    return


collectors = []

# Enable logging by module / class

logging.basicConfig()

Market.logger.setLevel(logging.DEBUG)


# Main function

def main():
    bittrex = Bittrex(key, secret)

    # Loading all the currencies
    msg = bittrex.get_currencies()

    if msg["success"]:

        for i in msg["result"]:
            currencies[i["Currency"]] = Currency([i["Currency"]])

    # Getting all the markets
    msg = bittrex.get_markets()

    if msg["success"]:

        for i in msg["result"]:
            markets[i["MarketName"]] = Market(i["MarketName"], i["MarketCurrency"], i["BaseCurrency"])

    # Get all balances
    msg = bittrex.get_balances()

    if msg["success"]:

        for i in msg["result"]:
            currencies[i["Currency"]].balance.available = i["Available"]
            currencies[i["Currency"]].balance.pending = i["Pending"]
            currencies[i["Currency"]].balance.balance = i["Balance"]
            currencies[i["Currency"]].balance.crypto_address = i["CryptoAddress"]

        print("Imported balances!")

    c = GeneralCollector(bittrex, i)

    p = Process(target=work, args=(c,))
    p.start()

    print("Started collector on markets!")


if __name__ == "__main__":
    print("Starting  ...")
    main()
    print("Started!")
