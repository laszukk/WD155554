import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

dane=pd.read_csv('zamowienia.csv',sep=";")
print(dane)

grupa=dane.groupby('Sprzedawca')['idZamowienia'].count().reset_index()
print(grupa)
sprzedawcy=grupa['Sprzedawca']
suma=grupa['idZamowienia']
explode = (0.1, 0.1, 0, 0,0,0,0,0,0)

wedges, texts, autotexts = plt.pie(suma,explode=explode,labels=sprzedawcy,autopct=lambda pct: "{:.1f}%".format(pct),shadow=True,textprops=dict(color="black"))
plt.setp(autotexts, size=14, weight="bold")
plt.legend(title='Sprzedawcy')
plt.show()