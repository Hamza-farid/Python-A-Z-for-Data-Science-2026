import numpy as np

a=np.arange(1,51)
a=a.reshape(10,5)


print(a[0:10]) # all 10 rows printed
print("\n\n")


print(a[:,0]) 
print(a[2:5,0]) #rows and col






# my_list=[1,2,3,4,5]
# print(my_list[0:4])
# print(my_list[:4])
# print(my_list[:-2])
# # last two
# print(my_list[-2:])