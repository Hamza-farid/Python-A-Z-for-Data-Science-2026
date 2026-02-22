import pandas as pd
df = pd.read_csv(r'C:\Users\hamza\Downloads\archive (1)\titanic.csv')


df.replace(to_replace=26, value=100, inplace=True) 

df.replace(36,22)

df.replace(to_replace=[26,36], value=[100,22], inplace=True)

df.replace(to_replace=[26,36], value='A', inplace=True)

df['physics'].replace([22,21,23],['A','B','C'], inplace=True)

df.replace('[A-Za-z]',0,regex=True)

df.replace(15,method='ffill')
