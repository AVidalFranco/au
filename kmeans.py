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
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

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


    # Xeramos as gráficas da curva
    plt.figure(figsize=(10,6))  
    plt.plot(n_clusters, scores_column, marker='o')
    plt.xlabel('Número de "Clusters"')
    plt.ylabel('Valores (SSE)')
    plt.title(f'"Elbow Curve" do {column}')
 


plt.tight_layout()
plt.show()

