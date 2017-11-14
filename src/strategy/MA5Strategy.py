import logging

from src.strategy.strategy import Strategy


class MA5Strategy(Strategy):
    logger = logging.getLogger(__name__)

    period1 = 5
    period2 = 8
    period3 = 14
    period4 = 20
    period5 = 30

    def __init__(self, market):
        Strategy.__init__(self, market)

        pass

    def operate(self):

            self._market.operate()

        pass