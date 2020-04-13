class Material:

    def __init__(self,rodzaj,dlugosc,szerokosc):
        self.rodzaj=rodzaj
        self.dlugosc=dlugosc
        self.szerokosc=szerokosc

    def wyswietl_nazwe(self):
        print(self.rodzaj)

class Ubrania(Material):
    def __init__(self,rodzaj,dlugosc,szerokosc,rozmiar,kolor,dla_kogo):
        Material.__init__(self,rodzaj,dlugosc,szerokosc)
        self.rozmiar=rozmiar
        self.kolor=kolor
        self.dla_kogo=dla_kogo

    def wyswietl_dane1(self):
        print(self.rozmiar,self.kolor,self.dla_kogo)

class Sweter(Ubrania):
    def __init__(self,rodzaj,dlugosc,szerokosc,rozmiar,kolor,dla_kogo,rodzaj_swetra):
        Ubrania.__init__(self,rodzaj,dlugosc,szerokosc,rozmiar,kolor,dla_kogo)
        self.rodzaj_swetra=rodzaj_swetra

    def wyswietl_dane2(self):
        print(self.rodzaj_swetra)


k1=Sweter("bawelna",30,20,"XL","czarny","Marta","polar")
k1.wyswietl_dane1()

