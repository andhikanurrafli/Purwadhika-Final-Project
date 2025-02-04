

df.head(10)

df = df.drop_duplicates()
df = df.dropna()

df['Year'] = df['Date Key'].astype(str).str[:4]

print(df[['Date Key', 'Year']].head()) 

df.describe()
df.info()
df
