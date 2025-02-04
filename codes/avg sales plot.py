avgSales20202022 = dfFiltered2020To2022.groupby('Year')['Sales'].mean()
avgProfit20202022 = dfFiltered2020To2022.groupby('Year')['Profit'].mean()


plt.figure(figsize=(10, 5))
plt.plot(avgSales20202022.index, avgSales20202022.values, marker='o', linestyle='-', color='b', label='Avg Sales')


plt.xlabel('Tahun')
plt.ylabel('Rata-rata Sales')
plt.title('Rata-rata Sales per Tahun 2020 - 2022')
plt.legend()
plt.grid(True)
plt.show()
