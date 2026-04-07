import pandas as pd

# Dataframe is collection of data 

df = pd.DataFrame()
print(df)

# Dataframe from list show 0th column
lst=[1,2,3,4,5 ]
df = pd.DataFrame(lst)
print(df)

# multiple colums
lst = [[1,2,3],[4,5,6],[7,8,9]]
df = pd.DataFrame(lst)
print(df)


#  dtaframe using dict
# keys will be col name and vals in rows
a = [{'a':1,'b':2,'c':3},
     {'a':4,'b':5,'c':6},]
df = pd.DataFrame(a)
print(df)


#  read csv
# df = pd.read_csv(r'C:\Users\hamza\Downloads\archive (1)\titanic.csv')
# df.head()  # first 5 rows
# df.tail()  # last 5 rows

