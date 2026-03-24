import wbgapi as wb
import matplotlib.pyplot as plt
import numpy as np

# wbgapi is also a world bank api
# mrv = most recent values
ny_gdp = wb.data.DataFrame(['ny.gdp.mktp.cd'], mrv=1, labels=True).dropna().sort_values(by="NY.GDP.MKTP.CD", ascending=False)[:10]

print(ny_gdp)

# Filtering the dataframe by country
# GDP of 6 countries in Trillions USD
GDP = wb.data.DataFrame(['ny.gdp.mktp.cd'], 
                        ['USA','CHN','JPN','DEU','IND','GBR']).T.dropna()/(10**12)

# Convert GDP data to numpy arrays
GDP_values = GDP.values
xtick = np.array([int(x[-4:]) for x in GDP.index.tolist()])

# Plot the GDP
fig, ax = plt.subplots(figsize=(15,7))

# Plot the series 
for country_index in range(GDP_values.shape[1]):
    ax.plot(xtick, GDP_values[:, country_index], label=GDP.columns[country_index])

# Set the title and axis label
plt.title('GDP', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Trillions of Dollars', fontsize=12)
plt.legend()

# Show the plot
plt.show()