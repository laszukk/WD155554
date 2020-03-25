a=int(input(u"Podaj najmniejsza liczbe przedziału:"))
b=int(input(u"Podaj najwiekszą liczbę z przedziału:"))

if b<a:
    print(u"Zły przedział")
else:
    i=a
    while i <=b:
        print(i*i)
        i+= 1



