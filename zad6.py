import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

xlsx=pd.ExcelFile("imiona.xlsx")
dane=pd.read_excel(xlsx)
print(dane)

plt.subplot(131)
grupa=dane.groupby('Plec')['Liczba'].sum().reset_index()
plt.bar(grupa['Plec'],grupa['Liczba'],color=['pink','red'])
plt.xlabel('Plec')
plt.ylabel('Ilosc')

plt.subplot(132)
grupaM=dane[dane['Plec']=="M"].reset_index()
grupaK=dane[dane['Plec']=="M"].reset_index()
grupa2M=grupaM.groupby('Rok')['Liczba'].sum().reset_index()
grupa2K=grupaK.groupby('Rok')['Liczba'].sum().reset_index()
plt.plot(grupa2M['Rok'],grupa2M['Liczba'],color='green')
plt.plot(grupa2K['Rok'],grupa2K['Liczba'],color='c')
plt.xlabel('Rok')
plt.ylabel('Liczba')

plt.subplot(133)

grupa1=dane.groupby('Rok')['Liczba'].sum().reset_index()
plt.bar(grupa1['Rok'],grupa1['Liczba'],color='yellow')
plt.xlabel('Rok')
plt.ylabel('Liczba')

plt.show()



