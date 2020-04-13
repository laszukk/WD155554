class Parzyste:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        self.index=0
        return self

    def __next__(self):
        if self.index <=len(self.data)-1:
            x=self.index
            self.index+=2
            return self.data[x]
        else:
            raise StopIteration

x=Parzyste([2,5,4,6,8])
i=iter(x)

for x in i:
  print(x)
