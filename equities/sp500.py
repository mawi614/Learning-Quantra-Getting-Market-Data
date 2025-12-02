import pandas as pd, requests
import yfinance as yf
import matplotlib.pyplot as plt
import io

# Getting the tickers in the S&P 500 from url
url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
html = requests.get(url, headers=headers, timeout=30).text

html_file = io.StringIO(html)
tables = pd.read_html(html_file)
tickers = next(df for df in tables if {"Symbol", "Security"}.issubset(df.columns))

# Extracting the Ticker column
ticker_symbol = tickers["Symbol"].tolist()

# Cleaning the ticker_symbol data
ticker_symbol = [ticker.replace(".", "-") for ticker in ticker_symbol]

# Getting the price data for the first 50 tickers
data = yf.download(ticker_symbol[0:50], '2025-01-01', auto_adjust=True)['Close']

plt.figure(figsize=(16, 10))

for ticker in ticker_symbol[0:50]:
    (data[ticker]/data[ticker].iloc[0]).plot()

plt.title('Price in Change', fontsize=14)
plt.xlabel('Year-Month', fontsize=12)
plt.ylabel('Price Change', fontsize=12)
plt.legend()

plt.show()