import numpy as np

#  start,end,step
x=np.arange(1,10,2)
print(x)



a=np.arange(2,20,2)

a=a.reshape(3,3)
print(a)

a=a.ravel() #faster than flatten , do not occupy space too
print(a)

# flatten give copy of the oringinal arr