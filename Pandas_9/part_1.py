import pandas as pd

lst = [1,2,3,4,5]
print(lst)

series = pd.Series(lst)
print(series)
print(type(series))


empty = pd.Series([])
print(empty)



a = pd.Series([1,2,3], index=['a','b','c'])
print(a)


b = pd.Series({'a':1,})
print(b)

print(a['a'])  # access by index label
print(a[0])  # access by position