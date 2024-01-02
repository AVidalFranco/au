import pandas as pd 
import numpy as np
import scipy.stats as stats
import statsmodels.api as sm
import os
from matplotlib import pyplot as plt
from datetime import datetime
from statsmodels.tsa.seasonal import seasonal_decompose

plt.style.use("ggplot")


# Establecer a ruta para ler o arquivo csv
data = pd.read_csv("data/data_pro.csv", delimiter=';')

data["date"] = pd.to_datetime(data["date"])
data = data.set_index("date")

# Na descomposición STL hai que dividir os datos temporales en 3 partes: seasonal (estacional), trend (tendencia) e resiude (residuo)





#### BENCENO ####

stl_ben = seasonal_decompose(data["BEN"], model="additive", extrapolate_trend="freq")

print("Tendencia da serie temporal do Benceno")
print(stl_ben.trend)

print("Compoñente estacional da serie temporal do Benceno")
print(stl_ben.seasonal)

print("Residuos da descomosición da serie temporal do Benceno")
print(stl_ben.resid)

print("Serie temporal observada do Benceno")
print(stl_ben.observed)

resultados_stl_ben = pd.DataFrame({
    "Tendencia": stl_ben.trend,
    "Estacionalidade": stl_ben.seasonal,
    "Residuo": stl_ben.resid,
    "Observado": stl_ben.observed
    })

resultados_stl_ben.to_csv("descomposicion_stl_ben.csv")

# Graficamos os resultados

# fig = stl_ben.plot()
# fig.set_size_inches((10, 6))
# plt.show()



# # Tendencia
# plt.figure(figsize=(12, 4))
# plt.plot(stl_ben.trend, label='Tendencia')
# plt.title('Tendencia da Serie Temporal do Benceno')
# plt.legend()
# plt.show()

# # Estacionalidade
# plt.figure(figsize=(12, 4))
# plt.plot(stl_ben.seasonal, label='Estacionalidade')
# plt.title('Compoñente Estacional do Benceno')
# plt.legend()
# plt.show()

# # Residuo
# plt.figure(figsize=(12, 4))
# plt.plot(stl_ben.resid, label='Residuo')
# plt.title('Residuo de la Descomposición do Benceno')
# plt.legend()
# plt.show()

# # Observado
# plt.figure(figsize=(12, 4))
# plt.plot(stl_ben.observed, label='Observado')
# plt.title('Serie Temporal Observada do Benceno')
# plt.legend()
# plt.show()


## Catro gráficas nunha imaxe ##

fig, axes = plt.subplots(4, 1, figsize=(12, 9), sharex=True)


axes[0].plot(stl_ben.trend, label='Tendencia', linewidth=2, color="blue")
axes[0].legend()
axes[1].plot(stl_ben.seasonal, label='Estacionalidade', linestyle='--', linewidth=1.5, color="blue")
axes[1].legend()
axes[2].plot(stl_ben.resid, label='Residuo', linestyle=':', linewidth=1.5, color="blue")
axes[2].legend()
axes[3].plot(stl_ben.observed, label='Observado', alpha=0.7, color="blue")
axes[3].legend()


axes[3].set_xlabel('Data')
axes[3].set_ylabel('Valores')
fig.suptitle('Descomposición Estacional da Serie Temporal do Benceno')

plt.tight_layout(rect=[0, 0, 1, 0.96])

plt.show()
