import logging
import time
from model.market import Market

from market_manager import markets
from worker import Worker


class GeneralCollector(Worker):
    delay = 5
    logger = logging.getLogger(__name__)

    def __init__(self, bittrex):

        super(GeneralCollector, self).__init__(bittrex)

        self._block = False

    def run(self):
        while not self._block:

            msg = self.bittrex.get_market_summaries()

            if msg["success"]:

                for i in msg["result"]:

                    if not (i['MarketName'] in markets.keys()):
                        #print i["MarketName"]
                        continue

                    markets[i['MarketName']].update_price(i['Last'])

            time.sleep(GeneralCollector.delay)

        pass

    def block(self):
        self._block = False
        pass
