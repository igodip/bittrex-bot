
import logging
from time import sleep

from bittrex import Bittrex
from strategy.strategy import Strategy

from worker import Worker


class StrategyWorker(Worker):
    logger = logging.getLogger(__name__)

    def __init__(self, bittrex, strategy):

        assert type(strategy), Strategy

        super(StrategyWorker, self).__init__(bittrex)

        self._strategy = strategy
        self._block = False

    def run(self):

        while not self._block:
            self._strategy.operate()
            sleep(3)

        pass

