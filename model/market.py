import logging

from model.candle import Candle
from model.currency import Currency
from model.market_history import MarketHistory
from model.order_book import OrderBook

import time


class Market(object):
    intervals = [60, 300, 1800, 3600, 14400, 86400]  # Intervals in seconds
    logger = logging.getLogger(__name__)

    def __init__(self, market_name, market_currency, base_currency):

        assert type(market_currency), Currency
        assert type(base_currency), Currency

        self.name = market_name

        self.minTradeSize = 0
        self.isActive = 0

        self.market_history = MarketHistory()
        self.order_book = OrderBook()

        self._candles = {}
        self._temporaryCandles = {}

        for i in Market.intervals:
            self._candles[i] = []
            self._temporaryCandles[i] = Candle()
            self._temporaryCandles[i].timestamp = time.time()

        pass

    def update_price(self, last):
        # Update all the candles
        # What the fuck can we do with bid and ask?

        # Market.logger.debug("Updating candles")

        for i in self._temporaryCandles.iterkeys():
            # if the candle is ready, store this one and create a new one
            # if
            # Market.logger.debug(i)

            if time.time() - self._temporaryCandles[i].timestamp > i:
                self._temporaryCandles[i].close = last

                # Push the old candle and create a new one!
                self._candles[i].append(self._temporaryCandles[i])
                self._temporaryCandles[i] = Candle()

                self._temporaryCandles[i].timestamp = time.time()
                self._temporaryCandles[i].open = last
                self._temporaryCandles[i].low = last
                self._temporaryCandles[i].high = last

            if self._temporaryCandles[i].low > last or self._temporaryCandles[i].low == 0.0:
                self._temporaryCandles[i].low = last

            if self._temporaryCandles[i].high < last or self._temporaryCandles[i].high == 0.0:
                self._temporaryCandles[i].high = last

            Market.logger.debug("%4d %10s %13f %13f %13f %13f %13f %d" % (i, self.name, last,
                                                                       self._temporaryCandles[i].open,
                                                                       self._temporaryCandles[i].high,
                                                                       self._temporaryCandles[i].low,
                                                                       self._temporaryCandles[i].close,
                                                                       self._temporaryCandles[i].timestamp))
