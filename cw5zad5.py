class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik:

    def __init__(self, pensja):
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


class Menadzer(Osoba, Pracownik):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        Pracownik.__init__(self, pensja)

    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)

x1=Pracownik(500)
y=isinstance(x1,Pracownik)
print(y)
x2=Menadzer("Karol","Broda",500)
y=isinstance(x2,Menadzer)
print(y)
y=isinstance(x1,Menadzer)
print(y)

y1=issubclass(Menadzer,Osoba)
print(y1)
y1=issubclass(Menadzer,Pracownik)
print(y1)
y1=issubclass(Pracownik,Osoba)
print(y1)
y1=issubclass(Osoba,Pracownik)
print(y1)
