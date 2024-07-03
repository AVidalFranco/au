import pandas as pd 
import scipy.stats as stats
from matplotlib import pyplot as plt
plt.style.use("ggplot")

# Calcular z-score de cada día e variable - BEN
data = pd.read_csv("results/BEN_zscore.csv", delimiter=';', parse_dates=["date"], index_col=["date"])

# Contar el número de 1 en la columna 'zscore_BEN'
num_ones = data['zscore_BEN'].sum()

print(f"Número de 1 en la columna 'zscore_BEN': {num_ones}")


# Calcular z-score de cada día e variable - CO
data = pd.read_csv("results/CO_zscore.csv", delimiter=';', parse_dates=["date"], index_col=["date"])

# Contar el número de 1 en la columna 'zscore_CO'
num_ones = data['zscore_CO'].sum()

print(f"Número de 1 en la columna 'zscore_CO': {num_ones}")


# Calcular z-score de cada día e variable - MXIL
data = pd.read_csv("results/MXIL_zscore.csv", delimiter=';', parse_dates=["date"], index_col=["date"])

# Contar el número de 1 en la columna 'zscore_MXIL'
num_ones = data['zscore_MXIL'].sum()

print(f"Número de 1 en la columna 'zscore_MXIL': {num_ones}")


# Calcular z-score de cada día e variable - O3
data = pd.read_csv("results/O3_zscore.csv", delimiter=';', parse_dates=["date"], index_col=["date"])

# Contar el número de 1 en la columna 'zscore_O3'
num_ones = data['zscore_O3'].sum()

print(f"Número de 1 en la columna 'zscore_O3': {num_ones}")


# Calcular z-score de cada día e variable - NO2
data = pd.read_csv("results/NO2_zscore.csv", delimiter=';', parse_dates=["date"], index_col=["date"])

# Contar el número de 1 en la columna 'zscore_NO2'
num_ones = data['zscore_NO2'].sum()

print(f"Número de 1 en la columna 'zscore_NO2': {num_ones}")


# Calcular z-score de cada día e variable - NO
data = pd.read_csv("results/NO_zscore.csv", delimiter=';', parse_dates=["date"], index_col=["date"])

# Contar el número de 1 en la columna 'zscore_NO'
num_ones = data['zscore_NO'].sum()

print(f"Número de 1 en la columna 'zscore_NO': {num_ones}")


# Calcular z-score de cada día e variable - NO
data = pd.read_csv("results/PM2_5_zscore.csv", delimiter=';', parse_dates=["date"], index_col=["date"])

# Contar el número de 1 en la columna 'zscore_NO'
num_ones = data['zscore_PM2_5'].sum()

print(f"Número de 1 en la columna 'zscore_PM2_5': {num_ones}")


# Calcular z-score de cada día e variable - NO
data = pd.read_csv("results/SO2_zscore.csv", delimiter=';', parse_dates=["date"], index_col=["date"])

# Contar el número de 1 en la columna 'zscore_NO'
num_ones = data['zscore_SO2'].sum()

print(f"Número de 1 en la columna 'zscore_SO2': {num_ones}")


# Calcular z-score de cada día e variable - NO
data = pd.read_csv("results/TOL_zscore.csv", delimiter=';', parse_dates=["date"], index_col=["date"])

# Contar el número de 1 en la columna 'zscore_NO'
num_ones = data['zscore_TOL'].sum()

print(f"Número de 1 en la columna 'zscore_TOL': {num_ones}")