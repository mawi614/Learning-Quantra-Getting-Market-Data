import wbdata
import pandas as pd
import datetime as datetime
import matplotlib.pyplot as plt

# Defining indicators, countries and dates
indicators = {'SP.POP.TOTL': 'Total Population', 'NY.GDP.MKTP.CD': 'GDP (current US$)'}
countries = {'USA', 'TUN'}

# Gettting the data
df = wbdata.get_dataframe(indicators=indicators, country=countries, date=("01/01/2000","01/01/2020"))
df_unstacked = df.unstack(level=0)

# Debug Output
#print(df_unstacked.head())

# Plotting the data

plt.figure(figsize=(15,7))
(((df_unstacked['GDP (current US$)'])['United States'])/ 1000000000).plot()
plt.title('US GDP', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Billions of Dollars', fontsize=12)

plt.show()