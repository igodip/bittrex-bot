from bittrex import Bittrex


class Worker(object):

    def __init__(self, bittrex):

        assert Bittrex is type(bittrex)
        self.bittrex = bittrex

        pass

    def run(self):

        raise NotImplementedError


