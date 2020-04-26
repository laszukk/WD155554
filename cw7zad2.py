import numpy as np

a=np.arange(9)
a=[3,2,5,6,3,1,9,3,2]
a=np.asmatrix(a)
a=a.reshape(3,3)

b=np.arange(16)
b=[3,2,5,6,3,1,9,3,2,11,6,2,5,3,6,7]
b=np.asmatrix(b)
b=b.reshape(4,4)

print(a.min(axis=0))
print(b.max(axis=1))
