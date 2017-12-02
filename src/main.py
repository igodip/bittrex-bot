#!/usr/bin/env python

import logging
import threading

from multiprocessing import Process, freeze_support

import thread
from bittrex import Bittrex
import requests.packages.urllib3

from account import key, secret, currencies
from market_manager import markets
from model.currency import Currency
from model.market import Market
from strategy.MA5Strategy import MA5Strategy
from worker.strategy_worker import StrategyWorker
# from strategy.MA5Strategy import MA5Strategy
# from worker.collector import Collector

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

#Market.logger.setLevel(logging.DEBUG)


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
            print i["MarketName"]

    # Get all balances
    msg = bittrex.get_balances()

    if msg["success"]:

        for i in msg["result"]:
            currencies[i["Currency"]].balance.available = i["Available"]
            currencies[i["Currency"]].balance.pending = i["Pending"]
            currencies[i["Currency"]].balance.balance = i["Balance"]
            currencies[i["Currency"]].balance.crypto_address = i["CryptoAddress"]

        print("Imported balances!")

    c = GeneralCollector(bittrex)

    p = threading.Thread(target=work, args=(c,))

    print("Started collector on markets!")

    s = MA5Strategy(markets['USDT-BTC'])
    sw = StrategyWorker(bittrex,s)

    p1 = threading.Thread(target=work, args=(sw,))

    print("Started strategy on USDT/BTC")

    s = MA5Strategy(markets['USDT-LTC'])
    sw = StrategyWorker(bittrex,s)

    p2 = threading.Thread(target=work, args=(sw,))

    print("Started strategy on USDT/LTC")

    s = MA5Strategy(markets['USDT-ETH'])
    sw = StrategyWorker(bittrex,s)

    p3 = threading.Thread(target=work, args=(sw,))

    print("Started strategy on USDT/ETH")

    s = MA5Strategy(markets['USDT-DASH'])
    sw = StrategyWorker(bittrex,s)

    p4 = threading.Thread(target=work, args=(sw,))

    print("Started strategy on USDT/DASH")

    p.start()
    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p.join()
    p1.join()
    p2.join()
    p3.join()
    p4.join()


if __name__ == "__main__":
    print("Starting  ...")
    main()
    print("Started!")
