import ccxt
import json

# First you choose an exchange, list of supported exchanges can be found at ccxt.exchanges
exchange_id = "binance"
exchange_class = getattr(ccxt, exchange_id)

exchange = exchange_class({
    'enableRateLimit': True,# Enables rate limiting to avoid exceeding API limits
})
# 2. Specify the trading pair and the limit
symbol = 'BTC/USDT'
limit = 10

try:
    # 3. Fetch the public trades (transactions are referred to as trades in CCXT)
    # The 'limit' parameter requests a specific number of the most recent trades
    trades = exchange.fetch_trades(symbol, limit=limit)

    # 4. Print the results in a readable format
    print(f"Fetched {len(trades)} recent trades for {symbol} on {exchange.id}:")
    for trade in trades:
        # Pretty print each trade object
        print(json.dumps(trade, indent=2))

except ccxt.DDoSProtection as e:
    print(f"DDoS Protection: {e}")
except ccxt.ExchangeNotAvailable as e:
    print(f"Exchange Not Available: {e}")
except ccxt.ExchangeError as e:
    print(f"Exchange Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

