import logging
from model.candle import Candle

from src.model.balance import Balance


class Currency(object):

    def __init__(self, value):
        self._value = value

        self.lastPrice = 0
        self.bidPrice = 0
        self.askPrice = 0

        self.balance = Balance()


