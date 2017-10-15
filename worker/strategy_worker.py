from bittrex import Bittrex

from model.currency import Market
from strategy.strategy import Strategy
from worker.worker import Worker


class StrategyWorker(Worker):
    def __init__(self, bittrex, strategy, currency):

        assert type(strategy), Strategy
        assert type(currency), Market

        super(StrategyWorker, self).__init__(bittrex)

        self._block = False

    def run(self):



        pass
