
import os
import numpy as np
import pandas as pd 
import scipy.stats as stats
from matplotlib import pyplot as plt
plt.style.use("ggplot")
from PIL import Image, ImageDraw

# Calcular z-score de cada día e variable
data = pd.read_csv("data/data_pro.csv", delimiter=';', parse_dates=["date"], index_col=["date"])

zscore = data.apply(stats.zscore) 

print(zscore)



#### TOLUENO ####

# tolueno = data.iloc[:, 8].to_list()

# # print(tolueno)

# # print(type(tolueno))


# tolzscore = zscore.iloc[:, 8]

# print(tolzscore)

# umbral_tol = 2

# outliers_tol = tolzscore[abs(tolzscore) > umbral_tol]

# print("Anomalías no Tolueno")
# print(outliers_tol)

# # plt.figure(figsize=(10, 6))
# # plt.scatter(data.index, data["TOL"], label='Datos', color="blue")
# # plt.scatter(outliers_tol.index, data["TOL"][outliers_tol.index], color='red', label='Anomalías')

# # plt.title(f'Valores anómalos do Tolueno')
# # plt.xlabel("Data")
# # plt.ylabel("Tolueno")
# # plt.legend()

# # # # plt.hist(tolzscore, bins=20, edgecolor='blue')
# # # # plt.title('Histograma de z-scores do Tolueno')
# # # # plt.xlabel("Z-Scores")
# # # # plt.ylabel("Frecuencia")

# # plt.show()


# # porcentaxe_anomalias_tol = (abs(tolzscore) > umbral_tol).mean() * 100
# # print(f"Porcentaxe de valores anómalos en '{tolzscore}': {porcentaxe_anomalias_tol:.2f}%")


# # # ### Gráfica TOL ###

# # # plt.figure(figsize=(10, 6))
# # # plt.plot(tolzscore.index, tolzscore, color="blue", label="Z-Scores do Tolueno")
# # # plt.title("Evolución dos Z-Scores do Tolueno no tempo")




# # #### SO2 ####

# so2zscore = zscore.iloc[:, 7]

# print(so2zscore)



# umbral_so2 = 2

# outliers_so2 = so2zscore[abs(so2zscore) > umbral_so2]

# print("Anomalías no SO2")
# print(outliers_so2)


# # plt.figure(figsize=(10, 6))
# # plt.scatter(data.index, data["SO2"], label='Datos', color="blue")
# # plt.scatter(outliers_so2.index, data["SO2"][outliers_so2.index], color='red', label='Anomalías')
# # plt.title(f'Valores anómalos do SO2')
# # plt.xlabel("Data")
# # plt.ylabel("SO2")
# # plt.legend()


# # plt.show()


# # porcentaxe_anomalias_so2 = (abs(so2zscore) > umbral_so2).mean() * 100
# # print(f"Porcentaxe de valores anómalos en '{so2zscore}': {porcentaxe_anomalias_so2:.2f}%")



# ### Gráfica SO2 ###

# # # plt.figure(figsize=(10, 6))
# # # plt.plot(so2zscore.index, so2zscore, color="blue", label="Z-Scores do SO2")
# # # plt.title("Evolución dos Z-Scores do SO2 no tempo")




# # #### PM2.5 ####

# pm25zscore = zscore.iloc[:, 6]

# print(pm25zscore)


# umbral_pm25 = 2

# outliers_pm25 = pm25zscore[abs(pm25zscore) > umbral_pm25]

# print("Anomalías no PM2.5")
# print(outliers_pm25)


# # plt.figure(figsize=(10, 6))
# # plt.scatter(data.index, data["PM2_5"], label='Datos', color="blue")
# # plt.scatter(outliers_pm25.index, data["PM2_5"][outliers_pm25.index], color='red', label='Anomalías')
# # plt.title(f'Valores anómalos do PM2.5')
# # plt.xlabel("Data")
# # plt.ylabel("PM2.5")
# # plt.legend()


# # plt.show()


# # porcentaxe_anomalias_pm25 = (abs(pm25zscore) > umbral_pm25).mean() * 100
# # print(f"Porcentaxe de valores anómalos en '{pm25zscore}': {porcentaxe_anomalias_pm25:.2f}%")


# # ### Gráfica PM2.5 ###

# # # plt.figure(figsize=(10, 6))
# # # plt.plot(pm25zscore.index, pm25zscore, color="blue", label="Z-Scores do PM2.5")
# # # plt.title("Evolución dos Z-Scores do PM2.5 no tempo")




# # #### O3 ####

# o3zscore = zscore.iloc[:, 5]

# print(o3zscore)


# umbral_o3 = 2

# outliers_o3 = o3zscore[abs(o3zscore) > umbral_o3]

# print("Anomalías no O3")
# print(outliers_o3)


# # plt.figure(figsize=(10, 6))
# # plt.scatter(data.index, data["O3"], label='Datos', color="blue")
# # plt.scatter(outliers_o3.index, data["O3"][outliers_o3.index], color='red', label='Anomalías')
# # plt.title(f'Valores anómalos do O3')
# # plt.xlabel("Data")
# # plt.ylabel("O3")
# # plt.legend()


# # plt.show()


# # porcentaxe_anomalias_o3 = (abs(o3zscore) > umbral_o3).mean() * 100
# # print(f"Porcentaxe de valores anómalos en '{o3zscore}': {porcentaxe_anomalias_o3:.2f}%")


# # ### Gráfica O3 ###

# # # plt.figure(figsize=(10, 6))
# # # plt.plot(o3zscore.index, o3zscore, color="blue", label="Z-Scores do O3")
# # # plt.title("Evolución dos Z-Scores do O3 no tempo")




# # #### NO ####

# nozscore = zscore.iloc[:, 4]

# print(nozscore)


# umbral_no = 2

# outliers_no = nozscore[abs(nozscore) > umbral_no]

# print("Anomalías no NO")
# print(outliers_no)


# # plt.figure(figsize=(10, 6))
# # plt.scatter(data.index, data["NO"], label='Datos', color="blue")
# # plt.scatter(outliers_no.index, data["NO"][outliers_no.index], color='red', label='Anomalías')
# # plt.title(f'Valores anómalos do NO')
# # plt.xlabel("Data")
# # plt.ylabel("NO")
# # plt.legend()


# # plt.show()


# # porcentaxe_anomalias_no = (abs(nozscore) > umbral_no).mean() * 100
# # print(f"Porcentaxe de valores anómalos en '{nozscore}': {porcentaxe_anomalias_no:.2f}%")

# # ### Gráfica NO ###

# # # plt.figure(figsize=(10, 6))
# # # plt.plot(nozscore.index, nozscore, color="blue", label="Z-Scores do NO")
# # # plt.title("Evolución dos Z-Scores do NO no tempo")




# # #### NO2 ####

# no2zscore = zscore.iloc[:, 3]

# print(no2zscore)

# umbral_no2 = 2

# outliers_no2 = no2zscore[abs(no2zscore) > umbral_no2]

# print("Anomalías no NO2")
# print(outliers_no2)


# # plt.figure(figsize=(10, 6))
# # plt.scatter(data.index, data["NO2"], label='Datos', color="blue")
# # plt.scatter(outliers_no2.index, data["NO2"][outliers_no2.index], color='red', label='Anomalías')
# # plt.title(f'Valores anómalos do NO2')
# # plt.xlabel("Data")
# # plt.ylabel("NO2")
# # plt.legend()


# # plt.show()


# # porcentaxe_anomalias_no2 = (abs(no2zscore) > umbral_no2).mean() * 100
# # print(f"Porcentaxe de valores anómalos en '{no2zscore}': {porcentaxe_anomalias_no2:.2f}%")



# # ### Gráfica NO2 ###

# # # plt.figure(figsize=(10, 6))
# # # plt.plot(no2zscore.index, no2zscore, color="blue", label="Z-Scores do NO2")
# # # plt.title("Evolución dos Z-Scores do NO2 no tempo")




# # #### MXIL ####

# mxilzscore = zscore.iloc[:, 2]

# print(mxilzscore)


# umbral_mxil = 2

# outliers_mxil = mxilzscore[abs(mxilzscore) > umbral_mxil]

# print("Anomalías no MXIL")
# print(outliers_mxil)


# # plt.figure(figsize=(10, 6))
# # plt.scatter(data.index, data["MXIL"], label='Datos', color="blue")
# # plt.scatter(outliers_mxil.index, data["MXIL"][outliers_mxil.index], color='red', label='Anomalías')
# # plt.title(f'Valores anómalos do MXileno')
# # plt.xlabel("Data")
# # plt.ylabel("MXileno")
# # plt.legend()


# # plt.show()


# # porcentaxe_anomalias_mxil = (abs(mxilzscore) > umbral_mxil).mean() * 100
# # print(f"Porcentaxe de valores anómalos en '{mxilzscore}': {porcentaxe_anomalias_mxil:.2f}%")

# # ### Gráfica MXIL ###

# # # plt.figure(figsize=(10, 6))
# # # plt.plot(mxilzscore.index, mxilzscore, color="blue", label="Z-Scores do MXileno")
# # # plt.title("Evolución dos Z-Scores do MXileno no tempo")




# # #### CO ####

# cozscore = zscore.iloc[:, 1]

# print(cozscore)


# umbral_co = 2

# outliers_co = cozscore[abs(cozscore) > umbral_co]

# print("Anomalías no CO")
# print(outliers_co)


# # plt.figure(figsize=(10, 6))
# # plt.scatter(data.index, data["CO"], label='Datos', color="blue")
# # plt.scatter(outliers_co.index, data["CO"][outliers_co.index], color='red', label='Anomalías')
# # plt.title(f'Valores anómalos do CO')
# # plt.xlabel("Data")
# # plt.ylabel("CO")
# # plt.legend()


# # plt.show()


# # porcentaxe_anomalias_co = (abs(cozscore) > umbral_co).mean() * 100
# # print(f"Porcentaxe de valores anómalos en '{cozscore}': {porcentaxe_anomalias_co:.2f}%")


# # ### Gráfica CO ###

# # # plt.figure(figsize=(10, 6))
# # # plt.plot(cozscore.index, cozscore, color="blue",  label="Z-Scores do CO")
# # # plt.title("Evolución dos Z-Scores do CO no tempo")




# # #### BENCENO ####

# benzscore = zscore.iloc[:, 0]

# print(benzscore)

# umbral_ben = 2

# outliers_ben = benzscore[abs(benzscore) > umbral_ben]

# print("Anomalías no Benceno")
# print(outliers_ben)


# # plt.figure(figsize=(10, 6))
# # plt.scatter(data.index, data["BEN"], label='Datos', color="blue")
# # plt.scatter(outliers_ben.index, data["BEN"][outliers_ben.index], color='red', label='Anomalías')
# # plt.title(f'Valores anómalos do Benceno')
# # plt.xlabel("Data")
# # plt.ylabel("Benceno")
# # plt.legend()


# # plt.show()


# porcentaxe_anomalias_ben = (abs(benzscore) > umbral_ben).mean() * 100
# print(f"Porcentaxe de valores anómalos en '{benzscore}': {porcentaxe_anomalias_ben:.2f}%")


### Gráfica BEN ###

# # plt.figure(figsize=(10, 6))
# # plt.plot(benzscore.index, benzscore, color="blue", label="Z-Scores do Benceno")
# # plt.title("Evolución dos Z-Scores do Benceno no tempo")




# #### Xeral para as gráficas ####
# plt.figure(figsize=(10, 6))
# cores = plt.cm.rainbow(np.linspace(0, 1, len(zscore.columns)))

# for i, columna in enumerate(zscore.columns):
#     plt.plot(zscore.index, zscore[columna], alpha=0.5, label=columna, color=cores[i])

# plt.xlabel("Data")
# plt.ylabel("Z-Scores")
# plt.title("Evolución dos Z-Scores das variables no tempo")

# plt.legend()

# plt.show()





##### Gardar nun CSV #####
# umbral = 2
# anomalias_columna = {}

# for columna in zscore.columns:
#     zscore_columna = zscore[columna]
#     outliers_columna = zscore_columna[abs(zscore_columna) > umbral]

#     print(f"Anomalías en {columna}")
#     print(outliers_columna)

#     anomalias_columna[columna] = outliers_columna

# df_anomalias = pd.DataFrame(anomalias_columna)

# # df_anomalias.to_csv("taboa_valores_anomalos_zscore.csv", sep=";")

# #### Calculamos o % de valores anómalos de cada variable para comprobar que gardamos no CSV os datos que eran ####

# data_copia = data.copy()

# porcentaxes_anomalias_variable = {}

# for columna in data_copia.columns:

#     anomalias_variable = np.abs(stats.zscore(data_copia[columna])) > umbral
#     porcentaxes_anomalias = (anomalias_variable.sum() / len(data_copia[columna])) * 100
#     porcentaxes_anomalias_variable[columna] = porcentaxes_anomalias

# print("% Anomalías para cada variable")
# print(porcentaxes_anomalias_variable)
