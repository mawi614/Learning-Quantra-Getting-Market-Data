import ccxt
import pandas as pd
import datetime as datetime

# First you choose an exchange, list of supported exchanges can be found at ccxt.exchanges
exchange_id = "binance"
exchange_class = getattr(ccxt, exchange_id)

exchange = exchange_class({
    'enableRateLimit': True,# Enables rate limiting to avoid exceeding API limits
})

# Load markets (currency pairs) from the exchange
exchange.load_markets()

# Fetch the latest ticker data for a specific symbol (e.g., Bitcoin/USDT)
symbol = 'BTC/USDT'
try:
    ticker = exchange.fetch_ticker(symbol)
    print(f"Ticker for {symbol} on {exchange_id}:")
    print(f"  Last Price: {ticker['last']}")
    print(f"  Bid Price: {ticker['bid']}")
    print(f"  Ask Price: {ticker['ask']}")
    print(f"  Volume (24h): {ticker['quoteVolume']}")
except ccxt.NetworkError as e:
    print(f"Network error: {e}")
except ccxt.ExchangeError as e:
    print(f"Exchange error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")