import numpy as np
import pandas as pd

dane=pd.read_csv('imiona1.csv')
print(dane)
print(dane[dane['Liczba']>1000])
print(dane[dane['Imie']=='KACPER'])
print(dane['Rok'].sum())
print(dane[(dane['Rok']>=2000) & (dane['Rok']<=2005)])
e = dane.groupby(['Plec'])
print(e['Liczba'].sum())
print(dane.sort_values('Liczba',ascending=False).groupby(['Rok', 'Plec']).nth(0))
print(dane.groupby(['Plec', 'Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'), ascending=False).iloc[[0, 1]])

