class Kwadrat:
    def __init__(self,x):
        self.x = x

    def __add__(self, kwadrat):
        return Kwadrat(self.x + kwadrat.x)

    def __str__(self):
        return 'Kwadrat o boku {}'.format(self.x)
    
p1 = Kwadrat(5)
p2 = Kwadrat(6)
p3 = p1 + p2
print(p3)