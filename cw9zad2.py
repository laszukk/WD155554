import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

dane=pd.read_csv('imiona1.csv')
print(dane)
grupa=dane.groupby(['Plec']).agg({'Liczba': ['sum']})
wykres=grupa.plot.bar()
wykres.set_ylabel('Tys')
wykres.set_xlabel('Plec')
wykres.legend()
plt.title('Ilosc chlopcow i dziewczynek w calym okresie')
plt.show()