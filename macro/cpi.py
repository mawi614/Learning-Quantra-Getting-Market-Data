import wbgapi as wb
import pandas as pd
import matplotlib.pyplot as plt

try:
    # Get data as a pandas Series with two indices (economy, time)
    plt.figure(figsize=(15,7))
    cpi_data = (wb.data.DataFrame(series='FP.CPI.TOTL.ZG', economy='USA', mrv=30))

    df_unstacked = cpi_data.unstack(level=0) 
    plottable_data = df_unstacked.transpose()   
    # Plot the CPI
    plottable_data.plot(ax=plt.gca(), color="brown")

    # Set the title and axis label
    plt.title('CPI Inflation', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Percent', fontsize=12)
    # Show the plot
    plt.show()

except Exception as e:
    print(f'The following error occurred:\n{e}')
