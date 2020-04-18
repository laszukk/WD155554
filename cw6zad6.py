import numpy as np

def wykreslanka():
    a=list("amperowoltomierz")
    a=np.asarray(a)
    a=a.reshape(4,4)
    a=np.asmatrix(a)
    slowo1=list("tata")
    slowo2=list("mata")
    slowo3=list("metr")
    slowo4=list("tor")
    slowo1=np.asarray(slowo1)
    slowo2=np.asarray(slowo2)
    slowo3=np.asarray(slowo3)
    slowo4=np.asarray(slowo4)
    np.fill_diagonal(a,slowo2)
    print(a)



wykreslanka()