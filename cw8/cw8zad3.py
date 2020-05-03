import numpy as np
import pandas as pd 

dane = pd.read_csv("zamowienia.csv", sep=";")

print(dane)

print(dane['Sprzedawca'].unique())

print(dane.sort_values('Utarg',ascending=False).head())

print(dane.groupby('Sprzedawca')['idZamowienia'].count())

print(dane.groupby('Kraj')['idZamowienia'].count())

filtr1=dane['Kraj']=='Polska'
filtr2=dane['Data zamowienia']>='2005-01-01'
filtr3=dane['Data zamowienia']<='2005-01-01'
print(dane.where(filtr1 & filtr3 & filtr3)['idZamowienia'].count())

print(dane[dane["Data zamowienia"].str.contains("2004")]['Utarg'].mean())

dane[dane["Data zamowienia"].str.contains("2004")].to_csv("zamowienia_2004.csv", index=False, sep=";")
dane[dane["Data zamowienia"].str.contains("2005")].to_csv("zamowienia_2005.csv", index=False, sep=";")