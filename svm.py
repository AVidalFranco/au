import pandas as pd

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
