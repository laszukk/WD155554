plik =open('zad1.txt','w')
import random
lista=[]
i=1
while i<=4:
    liczba=(random.randint(0,100))
    lista.append(liczba)
    i=i+1
plik.write(str(lista))