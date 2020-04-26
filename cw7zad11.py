import numpy as np

a=np.arange(12)
b=a.reshape((3,4))
c=a.reshape((4,3))
d=a.reshape((2,6))

print("Macierz B")
for x in b.flat:
    print(x)

print("Macierz C")
for x in c.flat:
    print(x)

print("Macierz D")
for x in d.flat:
    print(x)