from account import currencies
from model.market import Market

markets = {"USDT-BTC": Market("USDT-BTC", currencies['USDT'], currencies['BTC']),
           "USDT-ETH": Market("USDT-ETH", currencies['USDT'], currencies['ETH']),
           "BTC-SNT": Market("BTC-SNT", currencies['BTC'], currencies['SNT']), }

# TODO: Still thinking about this part
strategies = {}
