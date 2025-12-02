import ccxt
import pandas as pd
import datetime as datetime

# First you choose an exchange, list of supported exchanges can be found at ccxt.exchanges
exchange_id = "binance"
exchange_class = getattr(ccxt, exchange_id)

exchange = exchange_class({
    'enableRateLimit': True,# Enables rate limiting to avoid exceeding API limits
})
try:
    exchange.load_markets()
    
    tickers = exchange.fetch_tickers()

    print(f"Fetched {len(tickers)} tickers from {exchange.id}.")

    count = 0
    for symbol, ticker in tickers.items():
        print(f"Symbol: {symbol}, Last Price: {ticker['last']}, Volume (Quote): {ticker['quoteVolume']}")
        count += 1
        if count >= 10: # Print only first 10 for brevity
            break

except ccxt.NetworkError as e:
    print(f"Network error: {e}")
except ccxt.ExchangeError as e:
    print(f"Exchange error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")