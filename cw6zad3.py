import numpy as np

def tablica(n):
    macierz=np.arange(1,n*n+1,1)
    macierz.shape =(n, n)

    return macierz

print(tablica(3))