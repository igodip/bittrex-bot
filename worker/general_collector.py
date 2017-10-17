import time
import logging

from market_manager import markets
from model.market import Market
from worker import Worker


class GeneralCollector(Worker):
    delay = 5
    logger = logging.getLogger(__name__)

    def __init__(self, bittrex, market):
        assert type(market), Market

        super(GeneralCollector, self).__init__(bittrex)

        self._market = market
        self._block = False

    def run(self):
        while not self._block:

            msg = self.bittrex.get_market_summaries()

            if msg["success"]:

                for i in msg["result"]:

                    if not (i['MarketName'] in markets.keys()):
                        continue
                try:

                    markets[i['MarketName']].update_price(i['Last'])

                except KeyError, e:
                    print e

            time.sleep(GeneralCollector.delay)

        pass

    def block(self):
        self._block = False
        pass
