import numpy as np

def funkcja(n):
    a=np.arange(n,0.9,-1)
    b=np.zeros((n,n))
    np.fill_diagonal(b,a)
    return b

a=funkcja(3)
print(a)