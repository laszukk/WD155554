def parzyste(lista):
    lista2=[]
    index=0
    for index in range(len(lista)):
        if(index%2==0):
            lista2.append(lista[index])
            yield lista2


gen=parzyste([5,6,7,6])
print(next(gen))
print(next(gen))
