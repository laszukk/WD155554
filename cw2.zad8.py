import sys 

lista=[]
print(u"Podaj ciag liczb")
a=sys.stdin.readline()
i=0
while i<len(a)-1:
    lista.insert(i,a[i])
    i+=1
print(lista)

