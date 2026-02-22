import pandas as pd
df = pd.read_csv(r'C:\Users\hamza\Downloads\archive (1)\titanic.csv')


# groupby 
branch_group = df.groupby(by = ['class','section']) 
branch_group.groups # to print


for name, group in branch_group:
    print(name)  # to print group name
    print(group)  # to print group data









