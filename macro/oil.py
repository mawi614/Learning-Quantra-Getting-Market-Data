# Import libraries
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import date
import matplotlib.pyplot as plt

# Get the US Brent Crude price
# Series ID for US Brent Crude price: POILBREUSDM
us_brent_crude = yf.download("BZ=F", start='2020-01-01', end='2025-01-01', auto_adjust=True)
# Store the last value in 'macro_data'
#macro_data['US Brent Crude'] = "{} USD per barrel".format(us_brent_crude[-1])

# Plot the Crude price
plt.figure(figsize=(15,7))
# Set the title and axis label
plt.title('US Brent Crude $ per barrel', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('USD per barrel', fontsize=12)
# Show the plot
us_brent_crude.plot(color="purple")
plt.show()