import pandas as pd
import yfinance as yf

# Downloading 5 days worth of 1 minute frequency data
minute_data = yf.download('TSLA', period='5d', interval= '1m', auto_adjust=True, multi_level_index=False)

# Resampling the data (i.e constructing 15 minute data from the 1 minute data for example)
ohlv_dict = {
    'Open': 'first',
    'High': 'max',
    'Low': 'min',
    'Close': 'last',
    'Volume': 'sum'
}

resampled_15m_data = minute_data.resample('15min').agg(ohlv_dict)
resampled_15m_data.dropna(inplace=True) # Drop missing values

resampled_1h_data = minute_data.resample('1h').agg(ohlv_dict)
resampled_1h_data.dropna(inplace=True)

resampled_4h_data = minute_data.resample('4h').agg(ohlv_dict)
resampled_4h_data.dropna(inplace=True)

print(resampled_15m_data.head())
print(resampled_1h_data.head())
print(resampled_4h_data.head())