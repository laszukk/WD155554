class Ciagi:
    def __init__(self):
        pass
    def pobierz_parametry(self,a1,r,n):
        self.a1=a1
        self.r=r
        self.n=n
    def wyswietl_dane(self):
        i=1
        while i<=self.n:
            print(self.a1+(i-1)*self.r)
            i+=1
    def policz_sume(self):
        suma=0
        i=1
        while i<=self.n:
            suma=suma+(self.a1+(i-1)*self.r)
            i+=1
        print("Suma",suma)
    def pobierz_elementy(self,an):
        self.an=an
    def policz_elementy(self,a1,an,r):
        print("Elementy:",(self.an-self.a1+self.r)/r)

Aryt=Ciagi()
Aryt.pobierz_parametry(1,1,10)
Aryt.wyswietl_dane()
Aryt.policz_sume()
Aryt.pobierz_elementy(50)
Aryt.policz_elementy(5,50,5)