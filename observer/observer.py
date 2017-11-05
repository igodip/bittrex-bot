import logging
import time

from model.market import Market


class Observer(object):
    logger = logging.getLogger(__name__)

    def __init__(self, market):
        assert type(market), Marketal

        self._block = False
        self.market = Market

    def observe(self):
        while not self._block:
            time.sleep()

    def block(self):
        self._block = True
        pass
