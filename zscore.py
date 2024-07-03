
import pandas as pd 
import scipy.stats as stats
from matplotlib import pyplot as plt
plt.style.use("ggplot")

# Calcular z-score de cada día e variable
data = pd.read_csv("data/data_pro.csv", delimiter=';', parse_dates=["date"], index_col=["date"])

zscore = data.apply(stats.zscore)

# Define the thresholds
umbral_sup = 2

# For each column in the DataFrame
for column in data.columns:
    # Create a new DataFrame with the date, the original data, and the z-score > 0 indicator
    new_data = pd.DataFrame({
        'date': data.index,
        column: data[column],
        'zscore_' + column: ((zscore[column] > umbral_sup)).astype(int)
    })
    
    # Save the new DataFrame to a CSV file
    new_data.to_csv(f"results/{column}_zscore.csv", sep=";", index=False)

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(new_data['date'], new_data[column], label=column, color='royalblue')
    
    # Mark the anomalous days with a red dot
    anomalies = new_data[new_data['zscore_' + column] == 1]
    plt.plot(anomalies['date'], anomalies[column], 'o', label='Anomalía', color='tomato')
    
    # Add labels and title
    plt.xlabel('Data')
    plt.ylabel(column)
    plt.title(f'Anomalías Z-Score {column}')
    plt.legend()
    
    # Show the plot
    # plt.show()

    # Save the plot to a PNG file
    plt.savefig(f"results/{column}_zscore.png", dpi=300)
