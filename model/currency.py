import logging

from model.balance import Balance
from model.candle import Candle


class Currency(object):

    def __init__(self, value):
        self._value = value

        self.lastPrice = 0
        self.bidPrice = 0
        self.askPrice = 0

        self.balance = Balance()


