#  automatically remove duplicates

my_set={1,1,1,1,2,2,2,2,2}
print(my_set)  # output: {1, 2} - duplicates are removed


a={1,2,3}
b={3,4,5}
# common element will come only once
print(a.union(b))  # output: {1, 2, 3, 4, 5} - combines unique elements from both sets

a={} # empty dict
a=set() # empty set


