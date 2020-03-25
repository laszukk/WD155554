import math

a=int(input(u"Podaj liczbę:"))
try:
    x=math.sqrt(a)
except ValueError:
    print("Dupa")
print(x)