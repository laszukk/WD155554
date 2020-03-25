a =int(input("Wysokosc diamentu:"))
if (a%2==0):
    print("Liczba musi byc nieparzysta ")
elif (a<=0) or (a>9):
    print("Liczba musi byc w przediziale(0,9)")
else:
    s=a
    i=1
    while i<=a:
        print(" "*s,"O"*i)
        if i==a:
            break
        else:
            i=i+2
            s=s-1
    j=a-2
    s=s+1
    while j>=1:
        print(" "*s,"O"*j)
        j=j-2
        s=s+1
        
    