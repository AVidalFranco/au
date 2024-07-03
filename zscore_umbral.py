
import pandas as pd 
import scipy.stats as stats
from matplotlib import pyplot as plt
plt.style.use("ggplot")

# Calcular z-score de cada día e variable
data = pd.read_csv("data/data_pro.csv", delimiter=';', parse_dates=["date"], index_col=["date"])

zscore = data.apply(stats.zscore)
print(zscore)

# Sort z-scores for each column
sorted_z_scores = {col: sorted(zscore[col]) for col in zscore.columns}

# Plot sorted z-scores
plt.figure(figsize=(14, 10))
for i, col in enumerate(zscore.columns):
    plt.subplot(3, 3, i + 1)
    plt.plot(sorted_z_scores[col], marker='o', linestyle='-')
    plt.title(col)
    # plt.xlabel('Index')
    plt.ylabel('Sorted Z-scores')
    plt.grid(True)

plt.tight_layout()
plt.show()