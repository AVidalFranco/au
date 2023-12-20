
import pandas as pd 
import numpy as np
import scipy.stats as stats
import os


data = pd.read_csv("data/data_pro.csv", delimiter=';', parse_dates=["date"], index_col=["date"])

zscore = data.apply(stats.zscore) 

print(zscore)

tolueno = data.iloc[:, 8].to_list()

print(tolueno)

print(type(tolueno))

# dataframes = []

# for file in files:


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


