import pandas as pd

df = pd.read_excel(r'E:\salary.xlsx')
print(df.columns)  # Print column names

df.to_csv(r'E:/salary.csv')
print(df)


print(df.shape)
print(df.size)

print(df.info())

print(df.describe())


print(df.head(3))  # first 3 rows


