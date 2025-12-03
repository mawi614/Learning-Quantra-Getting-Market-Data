import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Csv data directory
project_path = 'D:/Python/quantra-getting-data/'
data_path = project_path + 'futures/data/'

# Read the data
first_contract_data = pd.read_csv(data_path + 'HEV20.csv', index_col=0, parse_dates=True)
second_contract_data = pd.read_csv(data_path + 'HEZ20.csv', index_col=0, parse_dates=True)

# Setting plot title and labels
plt.figure(figsize=(12, 7))
plt.title('Unadjusted Futures Contracts', fontsize=14)
plt.xlabel('Year-Month', fontsize=12)
plt.ylabel('Price', fontsize=12)

# Plotting the first futures
plt.plot(first_contract_data.Settle, label='HEV20', color='orange')

# Plotting the second futures right after
first_contract_expiry = first_contract_data.index.max()
plt.plot(second_contract_data.Settle.loc[first_contract_expiry:], label='HEZ20', color='green')

# Adding legend
plt.legend()

plt.show()
