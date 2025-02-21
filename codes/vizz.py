import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/drive/MyDrive/SaaS-Sales.csv')

# exploring data

# Industries
plt.figure(figsize=(10, 5))
sns.countplot(x=df['Industry'])
plt.xticks(rotation=45)
plt.title('Distribution of Industries')
plt.xlabel('Industry')
plt.ylabel('Frequency')
plt.show()

# Products
plt.figure(figsize=(10, 5))
sns.countplot(x=df['Product'])
plt.xticks(rotation=45)
plt.title('Distribution of Products')
plt.xlabel('Product')
plt.ylabel('Frequency')
plt.show()



# Total Sales per Quarter
# jika terjadi error gunakan ini --> df = df.reset_index()

df['Order Date'] = pd.to_datetime(df['Order Date'])

df['Quarter'] = df['Order Date'].dt.to_period('Q')

df_grouped = df.groupby(['Year', 'Quarter'])['Sales'].sum().reset_index()

# Konversi Quarter ke format string untuk pemetaan lebih mudah
df_grouped['Quarter'] = df_grouped['Quarter'].astype(str)

# Dataa Vizz
plt.figure(figsize=(12, 6))
for year in df_grouped['Year'].unique():
    data = df_grouped[df_grouped['Year'] == year]
    plt.plot(data['Quarter'], data['Sales'], marker='o', linestyle = '-', color='skyblue')

plt.xlabel('Quarter')
plt.ylabel('Total Sales')
plt.title('Tren Sales per Quarter')
plt.legend()
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()




# Profit per Quarter
# df_grouped = df.groupby(['Year', 'Quarter'])['Profit'].sum().reset_index()

df_grouped['Quarter'] = df_grouped['Quarter'].astype(str)
#vizzz
plt.figure(figsize=(12, 6))
for year in df_grouped['Year'].unique():
    data = df_grouped[df_grouped['Year'] == year]
    plt.plot(data['Quarter'], data['Profit'], marker='o', linestyle='-', color='skyblue')

plt.xlabel('Quarter')
plt.ylabel('Total Profit')
plt.title('Tren Profit per Quarter')
plt.legend()
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()




# Average Discount per Q
df_grouped = df.groupby(['Year', 'Quarter'])['Discount'].mean().reset_index()

df_grouped['Quarter'] = df_grouped['Quarter'].astype(str)
#vizz
plt.figure(figsize=(12, 6))
for year in df_grouped['Year'].unique():
    data = df_grouped[df_grouped['Year'] == year]
    plt.plot(data['Quarter'], data['Discount'], marker='o', linestyle='-', color='skyblue')

plt.xlabel('Quarter')
plt.ylabel('Average Discount')
plt.title('Average Discount per Quarter')
plt.legend()
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()



# Heatmap
df["Order Date"] = pd.to_datetime(df["Order Date"])  # Konversi ke format datetime
df["Year"] = df["Order Date"].dt.year  # Ambil tahun
df["Quarter"] = df["Order Date"].dt.to_period("Q")  # Ambil kuartal (contoh: 2022Q3)

salesPivot = df.pivot_table(values="Sales", index="Subregion", columns="Quarter", aggfunc="sum").fillna(0)


plt.figure(figsize=(15, 6))
sns.heatmap(salesPivot, cmap="RdYlGn", annot=True, fmt=".0f", linewidths=0.5)

plt.title("Sales Heatmap per Subregion dan Quarter", fontsize=14)
plt.xlabel("Quarter")
plt.ylabel("Subregion")
plt.xticks(rotation=45)
plt.show()
