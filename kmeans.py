import numpy as np
import pandas as pd
import seaborn as sns
import tarfile
import urllib
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score, adjusted_rand_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler
from mpl_toolkits.mplot3d import Axes3D

plt.style.use("ggplot")

# Establecer a ruta para ler o arquivo csv
data = pd.read_csv("data/data_pro.csv", delimiter=';', parse_dates=["date"], index_col=["date"])


# Normalizamos os datos
data_normalizados = data.copy()
for column in data.columns:
    data_normalizados[column]= MinMaxScaler().fit_transform(data[[column]])

    # print(data_normalizados[column])


# Visualizamos a Elbow Curve para cada variable 
fig, axs = plt.subplots(len(data.columns) - 1, 1, figsize=(10, 6 * (len(data.columns) - 1)))

for i, column in enumerate(data.columns[0:]):
    data_kmeans_column = data_normalizados[column]


     # Asegurarse de que la entrada sea 2D
    if len(data_kmeans_column.shape) == 1:
        data_kmeans_column = data_kmeans_column.values.reshape(-1, 1)


    # K-Means para distintos clusters (buscamos o número óptimo de clusters para os datos)
    n_clusters = range(1, 20)
    kmeans_modelo_column = [KMeans(n_clusters=j).fit(data_kmeans_column) for j in n_clusters]


    # Cálculo de SSE (Sum of Squared Errors / É a suma das distancias ao cadrado de cada punto ao centroide máis próximo no clustering)
    scores_column = [modelo.inertia_ for modelo in kmeans_modelo_column]


    # # Xeramos as gráficas da curva
#     plt.figure(figsize=(10,6))  
#     plt.plot(n_clusters, scores_column, marker='o')
#     plt.xlabel('Número de "Clusters"')
#     plt.ylabel('Valores (SSE)')
#     plt.title(f'"Elbow Curve" do {column}')
 


# plt.tight_layout()
# plt.show()


# Número óptimo de "clusters"
n_clusters_op = 4
kmeans_op = KMeans(n_clusters=n_clusters_op).fit(data)

 


## Non sei que fixen :) 
centroides = kmeans_op.cluster_centers_
print(centroides)
labels = kmeans_op.predict(data)

# # C = kmeans_op.cluster_centers_
# cores = ["red", "green", "blue", "cyan"]
# asignar = []
# for row in labels:
#     asignar.append(cores[row])

# fig = plt.figure(figsize=(10, 6))
# ax = fig.add_subplot(111, projection='3d')
# # ax = Axes3D(fig)
# ax.scatter(data["BEN"], data["CO"], data["MXIL"], c=asignar, s=60)
# ax.scatter(centroides[:, 0], centroides[:, 1], centroides[:, 2], marker="*", c=cores, s=1000)

# ax.set_xlabel('BEN')
# ax.set_ylabel('CO')
# ax.set_zlabel('MXIL')

# plt.title("K-Means")
# plt.legend()
# plt.show()





# # Etiquetas
# data["cluster_etiqueta"] = kmeans_op.labels_
# # titulos = data.columns[:-1]
# # print("Títulos", titulos)


# # print("Dimensións de k.means_op.cluster_centers_", kmeans_op.cluster_centers_)
# # print("Columnas seleccionadas", data.columns[:-1])


# # Coordenadas dos centroides dos clusters
# centroide = pd.DataFrame(kmeans_op.cluster_centers_, columns = data.columns[:-1])


# # Distancia de cada punto ao centroide do seu cluster
# data["distancia_centroide"] = np.linalg.norm(data.iloc[:, 1:].values - centroide.values[data["cluster_etiqueta"]], axis=1)


# # Umbral das anomalías
# umbral_kmeans = data["distancia_centroide"].quantile(0.90)


# # Identificar anomalías de cada variable
# anomalias_variables_kmeans = {}
# porcentaxes_anomalias_variables_kmeans = {}

# for column in data.columns[:-2]:
#     variable_data = data[[column, "distancia_centroide"]]
#     variable_data_anomalias = variable_data[variable_data["distancia_centroide"] > umbral_kmeans]

#     anomalias_variables_kmeans[column] = variable_data_anomalias
#     porcentaxes_anomalias_kmeans = len(variable_data_anomalias) / len(variable_data) *100
#     porcentaxes_anomalias_variables_kmeans[column] = porcentaxes_anomalias_kmeans


# # Comprobar a % de anomallías presentes en cada conxunto de datos
# for column, porcentaxe in porcentaxes_anomalias_variables_kmeans.items():
#     print(f"Porcentaxe de anomalías en {column}: {porcentaxe:.2f}")


# # Gardo nun csv as anomalías
# anomalias_kmeans = data[data["distancia_centroide"] > umbral_kmeans]

# filas_anomalias = []

# for variable in anomalias_variables_kmeans.keys():
#     filas_variables_anomalias = anomalias_kmeans[anomalias_kmeans[variable] > umbral_kmeans][["date", variable, "distancia_centroide"]]
#     filas_anomalias.append(filas_variables_anomalias)

# anomalias_semana = pd.concat(filas_anomalias, axis=0)

# anomalias_semana = anomalias_semana[["date"] + anomalias_semana.columns.difference(["date"]).tolist()]

# anomalias_semana.to_csv("taboa_valores_anomalos_kmeans", sep=";", index=False)


