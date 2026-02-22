import pandas as pd

# pivot table
df = pd.read_csv(r'C:\Users\hamza\Downloads\archive (1)\titanic.csv')

pd.pivot_table(df, index = 'class', columns = 'section', values = 'physics', aggfunc = 'mean')
# aggfunc = sum etc



pd.pivot_table(df,index='class')
