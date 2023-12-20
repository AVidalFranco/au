
import pandas as pd 
import numpy as np
import scipy.stats as stats
import os
from matplotlib import pyplot as plt

data = pd.read_csv("data/data_pro.csv", delimiter=';', parse_dates=["date"], index_col=["date"])

zscore = data.apply(stats.zscore) 

# print(zscore)





#### TOLUENO ####

# tolueno = data.iloc[:, 8].to_list()

# print(tolueno)

# print(type(tolueno))

# tolzscore = zscore.iloc[:, 8]

# # print(tolzscore)

# plt.plot(tolzscore.index, tolzscore, label="Z-Scores do Tolueno")
# plt.title("Evolución dos Z-Scores do Tolueno no tempo")




# #### SO2 ####

# so2zscore = zscore.iloc[:, 7]

# print(so2zscore)

# plt.plot(so2zscore.index, so2zscore, label="Z-Scores do SO2")
# plt.title("Evolución dos Z-Scores do SO2 no tempo")




# #### PM2.5 ####

# pm25zscore = zscore.iloc[:, 6]

# print(pm25zscore)

# plt.plot(pm25zscore.index, pm25zscore, label="Z-Scores do PM2.5")
# plt.title("Evolución dos Z-Scores do PM2.5 no tempo")




# #### O3 ####

# o3zscore = zscore.iloc[:, 5]

# print(o3zscore)

# plt.plot(o3zscore.index, o3zscore, label="Z-Scores do O3")
# plt.title("Evolución dos Z-Scores do O3 no tempo")




# #### NO ####

# nozscore = zscore.iloc[:, 4]

# print(nozscore)

# plt.plot(nozscore.index, nozscore, label="Z-Scores do NO")
# plt.title("Evolución dos Z-Scores do NO no tempo")




# #### NO2 ####

# no2zscore = zscore.iloc[:, 3]

# print(no2zscore)

# plt.plot(no2zscore.index, no2zscore, label="Z-Scores do NO2")
# plt.title("Evolución dos Z-Scores do NO2 no tempo")




# #### MXIL ####

# mxilzscore = zscore.iloc[:, 2]

# print(mxilzscore)

# plt.plot(mxilzscore.index, mxilzscore, label="Z-Scores do MXileno")
# plt.title("Evolución dos Z-Scores do MXileno no tempo")




# #### CO ####

# cozscore = zscore.iloc[:, 1]

# print(cozscore)

# plt.plot(cozscore.index, cozscore, label="Z-Scores do CO")
# plt.title("Evolución dos Z-Scores do CO no tempo")




# #### BENCENO ####

# benzscore = zscore.iloc[:, 0]

# print(benzscore)

# plt.plot(benzscore.index, benzscore, label="Z-Scores do Benceno")
# plt.title("Evolución dos Z-Scores do Benceno no tempo")


plt.xlabel("Data")
plt.ylabel("Z-Scores")
plt.title("Evolución dos Z-Scores das variables no tempo")

plt.legend()

plt.show()