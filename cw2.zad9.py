import sys 

wynik=0
print(u"Podaj ciag liczb")
a=int(sys.stdin.readline())

wynik=0

while a>0:
    wynik+=a%10
    a//=10

print (wynik)
