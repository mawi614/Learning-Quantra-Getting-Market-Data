import yfinance as yf
import matplotlib.pyplot as plt
stock_ticker_symbol = 'AAPL'

# Getting earnings calendar
ticker_data = yf.Ticker(stock_ticker_symbol)
earnings_dates = ticker_data.get_earnings_dates(limit=20)
earnings_dates.dropna(inplace=True)# Drop NaN values

print("Last 5 earnings dates of AAPL:")
print(earnings_dates.head(5))

# Corporate Actions
corporate_actions = ticker_data.get_actions()
print(f"Last 12 corporate actions \n{corporate_actions.tail(12)}")

data_to_plot = corporate_actions.tail(12)# Income and Revenue data for the last 3 years

# Defining the figure and plots
fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
width = 0.2

# Plotting
(data_to_plot['Dividends'] * 100).plot(kind='bar', color='blue', ax=ax1, width=width, position=1)
data_to_plot['Stock Splits'].plot(kind='bar', color='red', ax=ax2, width=width, position=0)

# Setting title and labels for the figure
ax1.set_ylabel('Dividends (%)', fontsize=12)
ax2.set_ylabel('Stock Splits (Ratio)', fontsize=12)
ax1.set_title('Dividends', fontsize=14)
ax2.set_title('Stock Splits', fontsize=14)
ax1.legend(loc=2)
ax2.legend(loc=2)
plt.tight_layout()

plt.show()