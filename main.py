from bittrex import Bittrex

key = "230cd2aaff354c43a3219a978ac2aebd"
secret = "fe11c3a0a7d14020bb78554ceb67de76"

bittrex = Bittrex(key,secret)

print(bittrex.get_currencies())