import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

msft = yf.Ticker('MSFT')

# We get the option chain for the first expiration date
option_chain = msft.option_chain(date=msft.options[0])

# We print the first five calls
print(option_chain.calls.head())

# We convert the call and put data to numpy arrays
call_strikes = np.array(option_chain.calls.strike)
call_last_prices = np.array(option_chain.calls.lastPrice)

put_strikes = np.array(option_chain.puts.strike)
put_last_prices = np.array(option_chain.puts.lastPrice)

fig, axes = plt.subplots(1, 2, figsize=(16,10))

axes[0].plot(call_strikes, call_last_prices, color='g')
axes[0].set_xlabel('Strike Price', fontsize=12)
axes[0].set_ylabel('Last Price', fontsize=12)
axes[0].set_title('Microsoft Call Options Last Price for Different Strike')

axes[1].plot(put_strikes, put_last_prices, color='r')
axes[1].set_xlabel('Strike Price', fontsize=12)
axes[1].set_ylabel('Last Price', fontsize=12)
axes[1].set_title('Microsoft Put Options Last Price for Different Strike')

plt.show()
