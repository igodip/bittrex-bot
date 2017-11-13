import logging

from src.strategy.strategy import Strategy


class MAStrategy(Strategy):
    logger = logging.getLogger(__name__)

    def __init__(self, currency):
        Strategy.__init__(self, currency)

        pass

    def operate(self):

        pass