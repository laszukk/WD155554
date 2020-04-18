import numpy as np

def macierz(n):
    a=np.full((n,n),4)
    np.fill_diagonal(a,6)
    a=np.flipud(a)
    np.fill_diagonal(a,2)
    print(a)

macierz(3)