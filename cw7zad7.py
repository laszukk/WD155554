import numpy as np

x=np.arange(6).reshape(2,3)
x=np.array([0,2,5,7,3,1])
a=np.sin(x)

y=np.arange(6).reshape(2,3)
y=np.array([0,2,5,7,3,1])
b=np.cos(y)

print(a+b)
