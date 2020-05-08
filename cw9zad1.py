import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

dane=pd.read_csv('imiona1.csv')
print(dane)
grupa=dane.groupby(['Rok']).agg({'Liczba': ['sum']})
wykres=grupa.plot()
wykres.set_ylabel('Tys')
wykres.set_xlabel('Rok')
wykres.legend()
plt.title('Ilosc urodzonych dzieci w danym roku')
plt.show()