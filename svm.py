import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

plt.style.use('ggplot')

from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import OneClassSVM

# Establecer a ruta para ler o arquivo csv
data = pd.read_csv("data/data_pro.csv", delimiter=';', parse_dates=["date"], index_col="date")

# Create a scaler object
scaler = MinMaxScaler(feature_range=(0, 1))

# Fit and transform the data
data_normalized = scaler.fit_transform(data)

# Train the One-Class SVM
model = OneClassSVM(nu=0.01, kernel="rbf", gamma=0.01)
model.fit(data_normalized)

# Predict the anomalies in the data
pred = model.predict(data_normalized)

# Add new column to data with anomalies denoted by -1
data['anomaly'] = pred

# Print the data with anomalies
print(data)

# Save the data with anomalies to a new csv file
data.to_csv("anomalies_SVM.csv")

## Convertir a DataFrame
anomalies = pd.DataFrame(data_normalized, columns=data.columns[:-1], index=data.index)
anomalies['anomaly'] = pred

# Función para graficar cada variable con anomalías
def plot_anomalies(df, variable):
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df[variable], label=variable, color='blue')
    
    # Resaltar as anomalías
    anomalies = df[df['anomaly'] == -1]
    plt.scatter(anomalies.index, anomalies[variable], color='red', label='Anomalías', marker='o')
    
    plt.title(f'Anomalías do {variable}')
    plt.xlabel('Data')
    plt.ylabel(variable)
    plt.grid(True)
    plt.legend()
    plt.show()

# Graficar todas las variables
for column in data.columns[:-1]:  # Excluir a columna de anomalías
    plot_anomalies(data, column)