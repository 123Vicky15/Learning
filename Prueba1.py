import pandas as pd
df = pd.read_csv(r"C:\\Users\\MARIA GARCES\\Downloads\\Ratios.csv")
df_filtrado = df[['symbol', 'peRatioTTM']]
df_filtrado
   