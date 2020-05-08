import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

dane=pd.read_csv('imiona1.csv')
print(dane)
filtr=dane.groupby(['Rok','Plec']).agg({'Liczba': ['sum']})
grupa=filtr.tail(10)
wykres = grupa.plot.pie(subplots=True, autopct='%1.1f%%')
plt.title('Liczba urodzen w latach 2013-2017')
plt.show()