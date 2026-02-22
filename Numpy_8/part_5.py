import numpy as np

a=np.arange(0,18).reshape(6,3)
b=np.arange(20,38).reshape(6,3)
print(a,"\n")
print(b)
print("\n\n")
print(a+b) # element wise addition

np.add(a,b) # same as above

np.subtract(a,b) # element wise subtraction
np.multiply(a,b) # element wise multiplication
np.divide(a,b) # element wise division

np.sum(a)






