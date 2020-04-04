import math
class Slowa:
    def __init__(self):
        pass
    def sprawdz_czy_palindrom(self,slowo):
        self.slowo=slowo
        for i in range(len(self.slowo)):
            if(self.slowo[i]!=self.slowo[len(self.slowo)-1-i]):
                return "Nie jest"
        return "Jest"

    def sprawdz_czy_metagramy(self,slowo1,slowo2):
        self.slowo1=slowo1
        self.slowo2=slowo2
        if(len(self.slowo1)!=len(self.slowo2)):
            return "Nie jest"
        suma=0
        for i in range(len(self.slowo1)):
            if(self.slowo1[i]!=self.slowo2[i]):
                suma=suma+1
        if(suma>1 or suma==0):
            return "Nie jest"
        else:
            return "Jest"
    def sprawdz_czy_anagramy(self,slowo1,slowo2):
        if(''.join(sorted(slowo1))==''.join(sorted(slowo2))):
            return "Jest"
        else:
            return "Nie jest"

    def wyswietl_wyrazy(self,slowo1,slowo2):
        self.slowo1=slowo1
        self.slowo2=slowo2
        print(slowo1,slowo2)

s=Slowa()
print(s.sprawdz_czy_palindrom("qwerty"))
print(s.sprawdz_czy_metagramy("tama","mata"))
print(s.sprawdz_czy_anagramy("tama","mata"))
print(s.wyswietl_wyrazy("ryk","byk"))