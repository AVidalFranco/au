import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
plt.style.use("ggplot")

from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import OneClassSVM

# Read the data
data = pd.read_csv("data/data_pro.csv", delimiter=';', parse_dates=["date"], index_col="date")

# Create a scaler object
scaler = MinMaxScaler(feature_range=(0, 1))

# For each column in the DataFrame
for column in data.columns:
    # Reshape the data for the scaler
    data_column = np.array(data[column]).reshape(-1, 1)
    
    # Fit and transform the data
    data_normalized = scaler.fit_transform(data_column)
    
    # Train the One-Class SVM
    model = OneClassSVM(nu=0.01, kernel="rbf", gamma=0.01)
    model.fit(data_normalized)
    
    # Predict the anomalies in the data
    pred = model.predict(data_normalized)

    # Replace the -1 values with 1 and the 1 values with 0
    pred[pred == 1] = 0
    pred[pred == -1] = 1
    
    # Create a new DataFrame with the date, the original data, and the SVM classification
    new_data = pd.DataFrame({
        'date': data.index,
        column: data[column],
        'svm_' + column: pred
    })
    
    # Save the new DataFrame to a CSV file
    new_data.to_csv(f"results/{column}_SVM.csv", sep=";", index=False)

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(new_data['date'], new_data[column], label=column, color='royalblue')
    
    # Mark the anomalous days with a red dot
    anomalies = new_data[new_data['svm_' + column] == 1]
    plt.plot(anomalies['date'], anomalies[column], 'o', label='Anomalía', color='tomato')

    # Add labels and title
    plt.xlabel('Data')
    plt.ylabel(column)
    plt.title(f'Anomalías SVM {column}')
    plt.legend()

    # Show the plot
    # plt.show()

    # Save the plot to a PNG file
    plt.savefig(f"results/{column}_SVM.png", dpi=300)