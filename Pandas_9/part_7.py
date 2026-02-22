import pandas as pd
df = pd.read_csv(r'C:\Users\hamza\Downloads\archive (1)\titanic.csv')


# loc 
df.loc[0]  # access first row
df.loc[0:5]  # access first 5 rows
df.loc[0:5,'age']  # access age column for first 5 rows


df.loc[df['age']>30]  # access rows where age is greater than 30
df.loc[df['age']>30,'name']  # access name column for rows where age is greater than 30


df.iloc[:,0]  # access first column
df.iloc[0:5,0]  # access first 5 rows of first column

# difference between loc and iloc is that loc is label based and iloc is integer based
# loc can access rows and columns by labels and iloc can access rows and columns by integer position

df = pd.read_csv(r'C:\Users\hamza\Downloads\archive (1)\titanic.csv',index_col='roll_no')
df.loc[1]  # access row with index label 1


