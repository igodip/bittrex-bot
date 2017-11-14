from bittrex import Bittrex
from model.currency import Market
from strategy.strategy import Strategy

from src.worker.worker import Worker


class StrategyWorker(Worker):
    def __init__(self, bittrex, strategy):

        assert type(strategy), Strategy

        super(StrategyWorker, self).__init__(bittrex)

        self._strategy = strategy
        self._block = False

    def run(self):

        self._strategy.operate()

        pass
