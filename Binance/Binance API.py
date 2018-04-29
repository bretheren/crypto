# INSTRUCTIONS
# 1. Install Python package python-binance
# 2. Set environmemt variables to securely store API Info as below
# OSX
# Set environment variabales as below using terminal in Linux/OSX
# export Binance_API_Key='PLACE YOUR API KEY HERE'
# export Binance_API_Secret='PLACE YOUR API SECRET HERE'

# WINDOWS
# set Binance_API_Key='PLACE YOUR API KEY HERE'
# set Binance_API_Secret='PLACE YOUR API SECRET HERE'

import os
from binance.client import Client

# Set variables for script
crypto_symbol = "BNBBTC"
stop_price = "0.00160000"
stop_limit_price = "0.00160000"
stop_quantity = "10"
profit_price = "0.00161000"
profit_limit_price = "0.00161000"
profit_quantity = "10"

# Get your environment keys
API_KEY = os.environ['Binance_API_Key']
API_SECRET = os.environ['Binance_API_Secret']
client = Client(API_KEY, API_SECRET)

# get ticker to obtain last Price
ticker = client.get_ticker(symbol=crypto_symbol)

# check if price is below stop price or above profit price
if ticker['lastPrice'] <= stop_price or ticker['lastPrice'] >= profit_price:
    if ticker['lastPrice'] <= stop_price:
# set stop loss parameters
        order_limit_price = stop_limit_price
        order_quantity = stop_quantity
    else:
# set profit take parameters
        order_limit_price = profit_limit_price
        order_quantity = profit_quantity
# place order        
    order = client.create_order(
        symbol=crypto_symbol,
        side=client.SIDE_SELL,
        type=client.ORDER_TYPE_LIMIT,
        timeInForce=client.TIME_IN_FORCE_GTC,
        quantity=order_quantity,
        price=order_limit_price
        )