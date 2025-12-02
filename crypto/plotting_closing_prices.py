import ccxt
import json
import pandas as pd
import matplotlib.pyplot as plt

# First you choose an exchange, list of supported exchanges can be found at ccxt.exchanges
exchange_id = "binance"
exchange_class = getattr(ccxt, exchange_id)

exchange = exchange_class({
    'enableRateLimit': True,# Enables rate limiting to avoid exceeding API limits
})
# 2. Specify the trading pair and the limit
symbol = 'BTC/USDT'
timeframe = '1h'

seven_days_ago = exchange.milliseconds() - (7 * 24 * 60 * 60 * 1000)

try:
    # 3. Fetch the public trades (transactions are referred to as trades in CCXT)
    # The 'limit' parameter requests a specific number of the most recent trades
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since=seven_days_ago, limit=1000)

    # 4. Print the results in a readable format
    print(f"Fetched {len(ohlcv)} recent trades for {symbol} on {exchange.id}:")

except ccxt.DDoSProtection as e:
    print(f"DDoS Protection: {e}")
except ccxt.ExchangeNotAvailable as e:
    print(f"Exchange Not Available: {e}")
except ccxt.ExchangeError as e:
    print(f"Exchange Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

if ohlcv:
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)

    (df['close']).plot(figsize=(12, 7))
    # Set title and labels for the plot
    plt.title('BTC Trade Price', fontsize=14)
    plt.xlabel('Time', fontsize=12)
    plt.ylabel('Price', fontsize=12)
    plt.show()
else:
    print(f"No OHLCV data found for {symbol} on {exchange.id} with timeframe {timeframe}.")


