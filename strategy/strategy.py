from model.currency import Market


class Strategy:

    def __init__(self, currency):

        assert type(currency),Market

        self._currency = currency

        pass

    def operate(self):

        raise NotImplementedError



