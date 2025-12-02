import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Formats the x-labels of the graph
def format_xlabels(data, ax):
    num_x_values = data.shape[0]
    step_size = num_x_values//4

    ax.set_xticks(np.arange(num_x_values))
    ax.set_xticklabels(data.index.values, rotation=45)

    for i, label in enumerate(ax.get_xticklabels()):
        if not i%step_size==0:
            label.set_visible(False)
    label.set_visible(True)


eurusd_data = yf.download('EURTND=X', period='5d', interval='1d')

eurusd_data.index = pd.to_datetime(eurusd_data.index)

x_values = eurusd_data['Close'].shape[0]

# Plotting the series
fig, ax = plt.subplots(figsize=(10, 7))
ax.plot(range(x_values), eurusd_data['Close'])

# Set title and axis label
plt.title('EUR/TND Data', fontsize=14)
plt.xlabel('Time', fontsize=12)
plt.ylabel('Price', fontsize=12)

# Format the xlabel
format_xlabels(eurusd_data['Close'], ax)

plt.show()