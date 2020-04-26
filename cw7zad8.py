import numpy as np

def rzad(macierz):
    for x in range(3):
        a=[]
        for y in range(3):
            a.append(macierz[x][y])
        print(a)

a = np.arange(9).reshape(3,3)
rzad(a)