from model.market import Market


class Strategy:

    def __init__(self, market):

        assert type(market), Market

        self._market = market

        pass

    def operate(self):

        raise NotImplementedError



