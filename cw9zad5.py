import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

dane = pd.read_csv("zamowienia.csv", sep=";")
print(dane)
filtr=dane.groupby(['Sprzedawca']).agg({'idZamowienia': ['count']})
wykres = filtr.plot.pie(subplots=True,autopct='%d')
plt.title('Ilosc zamowien zlozonych przez sprzedawcow')
plt.show()