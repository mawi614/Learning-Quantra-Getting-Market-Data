import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

ticker_list = ['AMZN', 'TSLA', 'NVDA', 'META']

price_data = yf.download(ticker_list, start='2019-01-01')['Close']

price_data.index = pd.to_datetime(price_data.index)

plt.figure(figsize=(10, 7))
(price_data['AMZN']/price_data['AMZN'].iloc[0]).plot()
(price_data['TSLA']/price_data['TSLA'].iloc[0]).plot()
(price_data['NVDA']/price_data['NVDA'].iloc[0]).plot()
(price_data['META']/price_data['META'].iloc[0]).plot()

plt.title('Price in Change', fontsize=14)
plt.xlabel('Year-Month', fontsize=12)
plt.ylabel('Price Change', fontsize=12)
plt.legend()

plt.show()