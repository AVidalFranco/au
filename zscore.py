
import pandas as pd 
import numpy as np
import scipy.stats as zscore
import os


files=["BEN_full.csv", "CO_full.csv", "MXIL_full.csv", "NO_full.csv", "NO2_full.csv", "O3_full.csv", "PM2.5_full.csv", "SO2_full.csv", "TOL_full.csv"]

# dataframes = []

# for file in files:

#     nome = os.path.splitext(file)[0].replace("_full", "")

#     df = pd.read_csv(file)
#     dataframes.append(df)

# data = np.array([files])
# stats.zscore(data)

# for i, df in enumerate(dataframes):
#     df_zscore = df.apply(zscore)

#     umbral = 1

#     anomalias = df[(df_zscore.abs() > umbral).any(axis=1)]

#     print(f"Anomalías en {nome}")
#     print(anomalias)
#     print()

