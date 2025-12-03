import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Csv data directory
project_path = 'D:/Python/quantra-getting-data/'
data_path = project_path + 'futures/data/'

# Read the data
first_contract_data = pd.read_csv(data_path + 'HEV20.csv', index_col=0, parse_dates=True)
second_contract_data = pd.read_csv(data_path + 'HEZ20.csv', index_col=0, parse_dates=True)

# Adjustment factor
first_contract_expiry = first_contract_data.index.max()
factor = second_contract_data.loc[first_contract_expiry].Settle / first_contract_data.loc[first_contract_expiry].Settle

# Adjusting the first contract
continuous_futures_proportional = first_contract_data.loc[:first_contract_expiry].Settle.copy()
continuous_futures_proportional *= factor

# Concatenating the data of the two contracts
continuous_futures_proportional = pd.concat([continuous_futures_proportional, second_contract_data.loc[first_contract_expiry:].Settle])

# Setting plot title and labels
plt.figure(figsize=(12, 7))
plt.title('Adjusted Futures Contracts', fontsize=14)
plt.xlabel('Year-Month', fontsize=12)
plt.ylabel('Price', fontsize=12)

# Plotting the first futures
plt.plot(continuous_futures_proportional)

# Adding legend
plt.legend()

plt.show()
