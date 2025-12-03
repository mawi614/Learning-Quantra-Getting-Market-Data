import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Getting Bitcoin futures data from Yahoo Finance
tesla_futures_data = yf.download('BTC=F', start='2022-01-01', end='2025-01-01')
tesla_futures_data.index = pd.to_datetime(tesla_futures_data.index)

# Plotting the close price
(tesla_futures_data['Close'].plot(figsize=(12,7)))

# Setting plot title and labels
plt.title('Bitcoin Continuous Futures Adjusted Close Price', fontsize=14)
plt.xlabel('Year-Month', fontsize=12)
plt.ylabel('Price', fontsize=12)

plt.show()
