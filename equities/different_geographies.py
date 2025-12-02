import pandas as pd
import yfinance as yf

# Download the data for Infosys from NSE exchange
# Adjust the daily price data till the current date is fetched
# Set the ticker as 'INFY', add the suffix '.NS' to specify the exchange
price_data_infosys = yf.download(
    "INFY.NS", start="2019-01-02", auto_adjust=True)

# Set the index to a datetime object
price_data_infosys.index = pd.to_datetime(price_data_infosys.index)

# Display the first 5 rows
print(price_data_infosys.tail())