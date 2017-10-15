import logging

from model.currency import Currency
from model.market_history import MarketHistory
from model.order_book import OrderBook


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

        pass

    def update_candles(self, bid, ask, last):
        # Update all the candles
        # What the fuck can we do with bid and ask?

        Market.logger.info("Updating candles")

        for i in self._temporaryCandles.iterkeys():
            # if the candle is ready, store this one and create a new one
            # if
            Market.logger.info(i)
