import numpy as np
import pandas as pd
from sklearn.neighbors import LocalOutlierFactor
from matplotlib import pyplot as plt
from matplotlib.legend_handler import HandlerPathCollection
import scipy.stats as stats
import os

plt.style.use("ggplot")

# Establecer a ruta para ler o arquivo csv
data = pd.read_csv("data/data_pro.csv", delimiter=';', parse_dates=["date"], index_col=["date"])


# Creamos un modelo LOF para cada variable
lof_variables = {}
anomalias_variables_lof = {}

for column in data.columns:
    variables = data[column].values.reshape(-1, 1)
    lof_variables[column] = LocalOutlierFactor(n_neighbors=20, contamination=0.1)
    lof_variables[column].fit_predict(variables) 
    anomalias_variables_lof[column] = lof_variables[column].negative_outlier_factor_

print(anomalias_variables_lof)


# Calculamos as anomalías individualmente 
anomalias_ben = anomalias_variables_lof["BEN"]
anomalias_co = anomalias_variables_lof["CO"]
anomalias_mxil = anomalias_variables_lof["MXIL"]
anomalias_no2 = anomalias_variables_lof["NO2"]
anomalias_no = anomalias_variables_lof["NO"]
anomalias_o3 = anomalias_variables_lof["O3"]
anomalias_pm25 = anomalias_variables_lof["PM2_5"]
anomalias_so2 = anomalias_variables_lof["SO2"]
anomalias_tol = anomalias_variables_lof["TOL"]





#### BENCENO ####

## Porcentaxe de datos que son anómalos
umbral_ben = -2

cantidade_anomalias_ben = sum(anomalias_ben < umbral_ben)
porcentaxe_anomalias_ben_lof = (cantidade_anomalias_ben/len(anomalias_ben))*100

print(f"Porcentaxe de anomalías no Benceno : {porcentaxe_anomalias_ben_lof:.2f}%")

print(anomalias_ben)

#### GRÁFICA BENCENO ####

plt.figure(figsize=(10, 6))

# # Gráfica de puntos normal
# plt.scatter(data.index, data["BEN"], label='Datos', color="blue")
# plt.scatter(data.index[anomalias_ben < umbral_ben], data["BEN"][anomalias_ben < umbral_ben], color='red', label='Anomalías')

# plt.scatter(data.index, data["BEN"], color="k", s=3., label="Datos")
# radio_ben = (anomalias_ben.max() - anomalias_ben) / (anomalias_ben.max() - anomalias_ben.min())
# plt.scatter(data.index, data["BEN"], s=1000 * radio_ben, edgecolors="r", facecolors="none", label="Anomalías Benceno")

# # Gráfica de dispersión de puntos
# fig, ax = plt.subplots()
# ax.scatter(data.index, data["BEN"], color="k", s=3., label="Datos")
# radio_ben = (anomalias_ben.max() - anomalias_ben) / (anomalias_ben.max() - anomalias_ben.min())
# ax.scatter(data.index, data["BEN"], s=1000 * radio_ben, edgecolors="r", facecolors="none", label="Anomalías Benceno")

# plt.scatter(data["BEN"], anomalias_ben, color="k", s=3., label="Datos")
# radio_ben = (anomalias_ben.max() - anomalias_ben) / (anomalias_ben.max() - anomalias_ben.min())
# plt.scatter(data["BEN"], anomalias_ben, s=1000 * radio_ben, edgecolors="r", facecolors="none", label="Anomalías")
# plt.axis('tight')
# plt.xlim((-5, 5))
# plt.ylim((-5, 5))


plt.axhline(y=umbral_ben, color="blue", linestyle="--", label="Umbral LOF")
plt.title(f'Valores anómalos do Benceno')
# plt.xlabel("Data")
# plt.ylabel("Benceno")
plt.legend()


plt.show()




#### CO ####

## Porcentaxe de datos que son anómalos
umbral_co = -1.5

cantidade_anomalias_co = sum(anomalias_co < umbral_co)
porcentaxe_anomalias_co_lof = (cantidade_anomalias_co/len(anomalias_co))*100

print(f"Porcentaxe de anomalías no CO : {porcentaxe_anomalias_co_lof:.2f}%")

print(anomalias_co)




#### MXILENO ####

## Porcentaxe de datos que son anómalos
umbral_mxil = -1.1

cantidade_anomalias_mxil = sum(anomalias_mxil < umbral_mxil)
porcentaxe_anomalias_mxil_lof = (cantidade_anomalias_mxil/len(anomalias_mxil))*100

print(f"Porcentaxe de anomalías no MXileno : {porcentaxe_anomalias_mxil_lof:.2f}%")

print(anomalias_mxil)




#### NO2 ####

## Porcentaxe de datos que son anómalos
umbral_no2 = -6.5

cantidade_anomalias_no2 = sum(anomalias_no2 < umbral_no2)
porcentaxe_anomalias_no2_lof = (cantidade_anomalias_no2/len(anomalias_no2))*100

print(f"Porcentaxe de anomalías no NO2 : {porcentaxe_anomalias_no2_lof:.2f}%")

print(anomalias_no2)




#### NO ####

## Porcentaxe de datos que son anómalos
umbral_no = -6.5

cantidade_anomalias_no = sum(anomalias_no < umbral_no)
porcentaxe_anomalias_no_lof = (cantidade_anomalias_no/len(anomalias_no))*100

print(f"Porcentaxe de anomalías no NO : {porcentaxe_anomalias_no_lof:.2f}%")

print(anomalias_no)




#### O3 ####

## Porcentaxe de datos que son anómalos
umbral_o3 = -5.5

cantidade_anomalias_o3 = sum(anomalias_o3 < umbral_o3)
porcentaxe_anomalias_o3_lof = (cantidade_anomalias_o3/len(anomalias_o3))*100

print(f"Porcentaxe de anomalías no O3 : {porcentaxe_anomalias_o3_lof:.2f}%")

print(anomalias_o3)




#### PM2.5 ####

## Porcentaxe de datos que son anómalos
umbral_pm25 = -3.5

cantidade_anomalias_pm25 = sum(anomalias_pm25 < umbral_pm25)
porcentaxe_anomalias_pm25_lof = (cantidade_anomalias_pm25/len(anomalias_pm25))*100

print(f"Porcentaxe de anomalías no PM2.5 : {porcentaxe_anomalias_pm25_lof:.2f}%")

print(anomalias_pm25)




#### SO2 ####

## Porcentaxe de datos que son anómalos
umbral_so2 = - 5.5

cantidade_anomalias_so2 = sum(anomalias_so2 < umbral_so2)
porcentaxe_anomalias_so2_lof = (cantidade_anomalias_so2/len(anomalias_so2))*100

print(f"Porcentaxe de anomalías no SO2 : {porcentaxe_anomalias_so2_lof:.2f}%")

print(anomalias_so2)





#### TOL ####

## Porcentaxe de datos que son anómalos
umbral_tol = - 4.5

cantidade_anomalias_tol = sum(anomalias_tol < umbral_tol)
porcentaxe_anomalias_tol_lof = (cantidade_anomalias_tol/len(anomalias_tol))*100

print(f"Porcentaxe de anomalías no Tolueno : {porcentaxe_anomalias_tol_lof:.2f}%")

print(anomalias_tol)


#### Estes resultados son un pouco extraños, non teño moi claro se están ben, e as gráficas non teñen moito sentido