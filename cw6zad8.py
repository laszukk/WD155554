import numpy as np

def dzielenie(m,kierunek):
    if kierunek=="poziom":
        if len(m)%2==1:
            return  "Nie da sie podzielic"
        else:
            x=int(len(m)/2)
            a=list(m[:x,],m[x:,])
            print(m[:x,])
            print(m[x:,])
            return 0
        
    if kierunek =="pion":
        if len(m[0])%2==1:
            return "Nie da sie podzielic"
        else:
            x=int(len(m[0])/2)
            #a=list(m[:x,],m[x:,])
            print(m[:,:x])
            print(m[:,x:])
            return 0

m=np.zeros((4,4))
np.fill_diagonal(m,3)
k=dzielenie(m,"pion")
print(k)

