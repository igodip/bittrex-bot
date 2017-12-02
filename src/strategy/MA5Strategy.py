import logging
from threading import Lock

from strategy import Strategy


class MA5Strategy(Strategy):
    logger = logging.getLogger(__name__)

    period1 = 5
    period2 = 8
    period3 = 14
    period4 = 20
    period5 = 25

    interval = 300

    lock = Lock()

    def __init__(self, market):
        Strategy.__init__(self, market)

        pass

    def operate(self):

        candles = self._market.get_candles(MA5Strategy.interval, MA5Strategy.period5)

        if len(candles) != MA5Strategy.period5:
            MA5Strategy.lock.acquire()
            print "Still not enough candles %d" % (len(candles))
            MA5Strategy.lock.release()
            return

        firstMA = 0
        secondMA = 0
        thirdMA = 0
        fourthMA = 0
        fifthMA = 0

        # Get First period candles and calculate moving average
        for i in candles[-MA5Strategy.period1:]:
            firstMA += i.close

        # Get Second period candles and calculate moving average
        for i in candles[-MA5Strategy.period2:]:
            secondMA += i.close

        # Get Third period candles and calculate moving average
        for i in candles[-MA5Strategy.period3:]:
            thirdMA += i.close

        for i in candles[-MA5Strategy.period4:]:
            fourthMA += i.close

        for i in candles[-MA5Strategy.period5:]:
            fifthMA += i.close

        firstMA /= MA5Strategy.period1
        secondMA /= MA5Strategy.period2
        thirdMA /= MA5Strategy.period3
        fourthMA /= MA5Strategy.period4
        fifthMA /= MA5Strategy.period5

        comment = ""

        if firstMA < secondMA < thirdMA < fourthMA < fifthMA:
            comment = "Strong sell"

        if firstMA > secondMA > thirdMA > fourthMA > fifthMA:
            comment = "Strong buy"

        if comment != "":
            MA5Strategy.lock.acquire()
            print "%10s: %6f %6f %6f %6f %6f : %12s" % (self._market.name,firstMA,secondMA,thirdMA,fourthMA,fifthMA,comment)
            MA5Strategy.lock.release()



        pass
