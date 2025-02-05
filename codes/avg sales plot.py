avgSales20202022 = dfFiltered2020To2022.groupby('Year')['Sales'].mean()
avgProfit20202022 = dfFiltered2020To2022.groupby('Year')['Profit'].mean()

# perbandingan dengan menggunakan bar plot
plt.figure(figsize=(10, 5))
plt.plot(avgSales20202022.index, avgSales20202022.values, marker='o', linestyle='-', color='b', label='Avg Sales')


plt.xlabel('Tahun')
plt.ylabel('Rata-rata Sales')
plt.title('Rata-rata Sales per Tahun 2020 - 2022')
plt.legend()
plt.grid(True)
plt.show()


# menggunakan line plot

df.index = pd.to_datetime(df.index)

df['Year'] = df.index.year

avgSalesPerYear = df.groupby('Year')['Sales'].mean()


plt.figure(figsize=(10, 5))
plt.bar(avgSalesPerYear.index, avgSalesPerYear.values, marker='o', linestyle='-', color='b', label='Avg Sales')


plt.xlabel('Tahun')
plt.ylabel('Rata-rata Sales')
plt.title('Rata-rata Sales per Tahun')
plt.legend()
plt.grid(True)
plt.show()


# bar plot

