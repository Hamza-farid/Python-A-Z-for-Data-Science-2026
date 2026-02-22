import numpy as np
# 1-D
arr = np.array([1,2,3,4,5])
print(arr)  # output: [1 2 3 4 5]

# 2-D
arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d)


print(type(arr))
print(type(arr_2d))

print(arr.size)
print(arr_2d.size)

print(arr.shape)  # row,col
print(arr_2d.shape) #row,col

print(arr.dtype)  # data type of the elements in the array

d = np.array([[1,2,3,4.5,7],
              [6,7,8,9,10],
            [11,22,32,14,15]])

print(type(d))
print(d.dtype)  # output: float64 - because of the presence of a float value (4.5) in the array, numpy promotes the entire array to float type to maintain consistency.


d.transpose()

