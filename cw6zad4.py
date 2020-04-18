import numpy as np

def generuj(n,m):
    return np.logspace(1.0, m, num=m, base=n)

print(generuj(2,4))