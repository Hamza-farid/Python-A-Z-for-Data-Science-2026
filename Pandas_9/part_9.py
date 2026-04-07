import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'class': ['5', '5', '6', '6'],
    'section': ['X', 'Y', 'X', 'Y'],
    'physics': [85, 90, 78, 88]
})

# Pivot table: mean of 'physics' by 'class' and 'section'
pivot = pd.pivot_table(df, index='class', columns='section', values='physics', aggfunc='mean')
print("Pivot table (mean of physics by class and section):")
print(pivot)

# Pivot table: mean of 'physics' by 'class' only
pivot2 = pd.pivot_table(df, index='class', values='physics', aggfunc='mean')
print("\nPivot table (mean of physics by class):")
print(pivot2)