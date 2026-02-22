import pandas as pd



df = pd.read_csv(r'C:\Users\hamza\Downloads\archive (1)\titanic.csv')
df.isnull().sum()
df2 = df.dropna()  # drop rows with missing values
df2 = df.dropna(axis=1)  # drop columns with missing values

df2 = df.dropna(how = 'all')  # drop rows where all values are missing

# replaces your oringinal dataframe
df.dropna(inplace = True)  # drop rows with missing values and modify the original dataframe

