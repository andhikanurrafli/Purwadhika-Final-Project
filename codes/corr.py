# data correlation

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

correlation = df[['Discount','Sales','Quantity']].corr()
print(correlation)

# matriks korelasi

plt.figure(figsize=(8,6))
sns.heatmap(correlation , annot=True, cmap='coolwarm', fmt=".2mf")
plt.title('Matriks Korelasi antara Discount, Sales, dan Quantity')
plt.show()
