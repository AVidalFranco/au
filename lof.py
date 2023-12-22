import numpy as np
import pandas as pd
from sklearn.neighbors import LocalOutlierFactor
from matplotlib import pyplot as plt
from matplotlib.legend_handler import HandlerPathCollection

# Establecer a ruta para ler o arquivo csv
data = pd.read_csv("data/data_pro.csv", delimiter=';', parse_dates=["date"], index_col=["date"])

# Seleccionar as variables nas que queremos detectar as anomalías
variables = ["BEN", "CO", "MXIL", "NO2", "NO", "O3", "PM2_5", "SO2", "TOL"]
x = data[variables]

# Establecemos o número de "veciños"
lof = LocalOutlierFactor(n_neighbors=20, contamination=0.1)


# Calculamos os valores anómalos
y_pred = lof.fit_predict(x)
x_scores = lof.negative_outlier_factor_

print(x_scores)


# Graficamos os resultados
# plt.scatter(data.index, x["TOL"], c=x_scores, label='Anomalías')

def update_legend_maker_size(handle, orig):
    "Personalizando o tamaño da lenda"
    handle.update_from(orig)
    handle.set_sizes([20])

    
plt.scatter(x[:, 8], color="k", s=0.3, label="Puntos")
radius = (x_scores.max() - x_scores)/(x_scores.max() - x_scores.min())
scatter = plt.scatter(
    x[:, 0]
    x[:, 1]
    s= 1000 * radius,
    edgecolors="r",
    facecolors="none",
    label="Outlier scores",
)
plt.axis("tight")
plt.xlim((-5, 5))
plt.ylim((-5, 5))
plt.xlabel("aaaa")
plt.legend(
    handler_map = {scatter: HandlerPathCollection(update_func=update_legend_maker_size)}
)
plt.title("LOF")
plt.show()

# plt.title("Local Outlier Factor (LOF) do Tolueno")
# plt.xlabel("Data")
# plt.ylabel("Tolueno")


# plt.legend()
# plt.show()