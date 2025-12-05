import simfin as sf
from simfin.names import *
from datetime import timedelta
import pandas as pd
import matplotlib.pyplot as plt

from . my_functions import get_fundamental_data
aapl_income_data,\
    aapl_balance_sheet_data,\
        aapl_cash_flow_data  = get_fundamental_data('AAPL')

# Calculating the currrent ratio, ROE
aapl_current_ratio = \
    round((aapl_balance_sheet_data['Total Current Assets']) / (aapl_balance_sheet_data['Total Current Liabilities']).astype(float), 2)

aapl_roe = \
    round((aapl_income_data['Net Income']) / (aapl_balance_sheet_data['Total Equity']).astype(float), 2) * 100

aapl_der = \
    round((aapl_balance_sheet_data['Long Term Debt']) / (aapl_balance_sheet_data['Total Equity'])) * 100
# Plotting the current ratio
curr_data_to_plot = aapl_current_ratio.tail(12)
roe_data_to_plot = aapl_roe.tail(12)
der_data_to_plot = aapl_der.tail(12)
X = curr_data_to_plot.index

# Plot the bar charts
plt.figure(figsize=(15, 7))
plt.bar(X, curr_data_to_plot, color='purple', width=10, label="Current Ratio")
plt.bar(X + timedelta(20), roe_data_to_plot, color='blue', width=10, label="Return on Equity")
plt.bar(X + timedelta(40), der_data_to_plot, color='yellow', width=10, label="Debt/Equity")

# Set title and labels for the plot
plt.title('Current Ratio, ROE', fontsize=14)
plt.xlabel('Year-Month', fontsize=12)
plt.ylabel('Current Ratio | ROE | DE', fontsize=12)

plt.legend()
plt.show()