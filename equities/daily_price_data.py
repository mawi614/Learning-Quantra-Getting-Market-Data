import pandas as pd # For working with data
import yfinance as yf # For working with financial data from the Yahoo Finance API
import matplotlib.pyplot as plt

aapl_data = yf.download('AAPL', start='2020-01-01', end='2025-01-01', auto_adjust=True)
nvda_data = yf.download('NVDA', start='2020-01-01', end='2025-01-01', auto_adjust=True)
jpm_data = yf.download('JPM', start='2020-01-01', end='2025-01-01', auto_adjust=True)
meta_data = yf.download('META', start='2020-01-01', end='2025-01-01', auto_adjust=True)

fig, axes = plt.subplots(2, 2, figsize=(16,6))

axes[0, 0].plot(aapl_data['Close'])
axes[0, 0].set_xlabel('Year-Month', fontsize=12)
axes[0, 0].set_ylabel('Price', fontsize=12)
axes[0, 0].set_title('Apple Price')

axes[0, 1].plot(nvda_data['Close'])
axes[0, 1].set_xlabel('Year-Month', fontsize=12)
axes[0, 1].set_ylabel('Price', fontsize=12)
axes[0, 1].set_title('Nvidia Price')

axes[1, 0].plot(jpm_data['Close'])
axes[1, 0].set_xlabel('Year-Month', fontsize=12)
axes[1, 0].set_ylabel('Price', fontsize=12)
axes[1, 0].set_title('JPMorgan Price')

axes[1, 1].plot(meta_data['Close'])
axes[1, 1].set_xlabel('Year-Month', fontsize=12)
axes[1, 1].set_ylabel('Price', fontsize=12)
axes[1, 1].set_title('Meta Price')

fig.suptitle('Stock Price by Ticker')

plt.tight_layout()
plt.show()