# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reading data from a csv file with pandas
data_path = "./data_modules/AAPL.csv"

apple_price_data = pd.read_csv(data_path, index_col=0)

# Converting the index to date time format
apple_price_data.index = pd.to_datetime(apple_price_data.index)

# Exploring the data
print(apple_price_data.tail())

print(apple_price_data.info())

# Checking for null values
null_values =  apple_price_data.isna().sum()
print(f"#Null Values = \n {null_values}")

# Dropping null values
apple_price_data.dropna(inplace=True)
    # Print the number of rows in the dataframe
print('Number of rows: ', apple_price_data.shape[0])
    # Checking for null values again
null_values =  apple_price_data.isna().sum()
print(f"#Null Values = \n {null_values}")

# Display the count of duplicate values
print(apple_price_data.duplicated().value_counts())
print('Proportion of duplicate values is {}.'.format( 
      round(apple_price_data.duplicated().value_counts()[1]/apple_price_data.shape[0], 4)))

# Drop the consecutive duplicate values
apple_price_data = apple_price_data.loc[(apple_price_data['close'].diff() != 0) | 
                                        (apple_price_data['open'].diff() != 0) |
                                        (apple_price_data['high'].diff() != 0) |
                                        (apple_price_data['low'].diff() != 0)]

# Check the number of rows
print("Number of rows: ", apple_price_data.shape[0])

# Calculate the percentage change
apple_price_data['returns'] = apple_price_data['close'].pct_change()

# Plot the percentage change
plt.figure(figsize=(10,7))
apple_price_data['returns'].plot()
# Set the title and axes label
plt.title('Returns', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Percentage Change', fontsize=12)
# Show the plot
plt.show()