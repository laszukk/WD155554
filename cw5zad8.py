class Samogloski:
    lista2=[]
    def __init__(self,wyraz):
        self.wyraz=wyraz
    
    def sprawdzanie(self):
        if(isinstance(self.wyraz, str)!=True):
            return "To nie jest wyraz"
    
    def __iter__(self):
        self.index=0
        return self

    def __next__(self):
        lista=["a","e","i","o","u","y"]
        if self.index<=len(self.wyraz)-1:
            if self.wyraz[self.index] in lista:
                self.lista2.append(self.wyraz[self.index])
            self.index+=1
        else:
            raise StopIteration

x=Samogloski("Maciek")
isinstance(x,Samogloski)
i=iter(x)
num=0

for x in i:
    num+=1
        
print(i.lista2)

