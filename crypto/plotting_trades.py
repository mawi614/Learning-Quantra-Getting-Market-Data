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
limit = 100000

try:
    # 3. Fetch the public trades (transactions are referred to as trades in CCXT)
    # The 'limit' parameter requests a specific number of the most recent trades
    trades = exchange.fetch_trades(symbol, limit=limit)

    # 4. Print the results in a readable format
    print(f"Fetched {len(trades)} recent trades for {symbol} on {exchange.id}:")

except ccxt.DDoSProtection as e:
    print(f"DDoS Protection: {e}")
except ccxt.ExchangeNotAvailable as e:
    print(f"Exchange Not Available: {e}")
except ccxt.ExchangeError as e:
    print(f"Exchange Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

price_data = pd.DataFrame.from_dict(trades)
price_data.set_index("datetime", inplace=True)
price_data.index = pd.to_datetime(price_data.index)

#print(price_data.head())

# Plot the close price
(price_data['price']).plot(figsize=(15, 7))

# Set title and labels for the plot
plt.title('BTC Trade Price', fontsize=14)
plt.xlabel('Time', fontsize=12)
plt.ylabel('Price', fontsize=12)
plt.show()