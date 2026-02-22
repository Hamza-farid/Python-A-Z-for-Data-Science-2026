# how to handle null val
from pandas import pd


df = pd.read_csv(r'C:\Users\hamza\Downloads\archive (1)\titanic.csv')

df.fillna(0)  # replace null values with 0

df.fillna(method = 'ffill',axis = 1)  # forward fill - replace null values with the last valid col val
df.fillna(method = 'ffill',axis = 0)  # backward fill - replace null values with the prev valid row val



df['phy'.fillna(df['phy'].mean())]



