import simfin as sf
from simfin.names import *
from datetime import timedelta
import pandas as pd
import matplotlib.pyplot as plt

from . my_functions import get_fundamental_data

# We try our function to fetch fundamentals for MSFT
msft_income_data,\
    msft_balance_sheet_data,\
        msft_cash_flow_data = get_fundamental_data("MSFT")

# Next we plot the net income and revenue for the last 3 years of MSFT
income_statement_data_to_plot = msft_income_data.tail(12)
balance_sheet_data_to_plot = msft_balance_sheet_data.tail(12)
cash_flow_statement_data_to_plot = msft_cash_flow_data.tail(12)
data = [
    income_statement_data_to_plot['Net Income'],
      income_statement_data_to_plot['Revenue'],
        balance_sheet_data_to_plot['Retained Earnings'],
          cash_flow_statement_data_to_plot['Net Cash from Operating Activities']
          ]

X = income_statement_data_to_plot.index
plt.figure(figsize=(18, 7))

# We plot the bar chart
plt.bar(X + timedelta(-10), data[0], color='blue', width=10, label='Net Income')
plt.bar(X + timedelta(10), data[1], color='orange', width=10, label='Revenue')
plt.bar(X + timedelta(30), data[2], color='green', width=10, label='Retained Earnings')
plt.bar(X + timedelta(50), data[3], color='red', width=10, label='Net Cash from Operating Activities')

# Set title and labels for the plot
plt.title('Net Income, Revenue, Retained Earnings and Net Cash from Operating Activities', fontsize=14)
plt.xlabel('Year-Month', fontsize=12)
plt.ylabel('Value ($)', fontsize=12)
plt.legend()

plt.show()
