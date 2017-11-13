import logging
import time

from model.market import Market
from worker import Worker


class Collector(Worker):

    delay = 60
    logger = logging.getLogger(__name__)

    def __init__(self, bittrex, market):

        assert type(market), Market

        super(Collector, self).__init__(bittrex)

        self._market = market
        self._block = False

    def run(self):
        while not self._block:

            Collector.logger.debug(self.bittrex.get_ticker(self._market.name))
            time.sleep(Collector.delay)

        pass

    def block(self):
        self._block = False
        pass
