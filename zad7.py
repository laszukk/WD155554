import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

xlsx=pd.ExcelFile("imiona.xlsx")
dane=pd.read_excel(xlsx)
print(dane)

grupaM=dane[dane['Plec']=="M"].reset_index()
grupaK=dane[dane['Plec']=="M"].reset_index()
grupa2M=grupaM.groupby('Rok')['Liczba'].sum().reset_index()
grupa2K=grupaK.groupby('Rok')['Liczba'].sum().reset_index()
plt.bar(grupa2M['Rok'],grupa2M['Liczba'],color='blue')
plt.bar(grupa2K['Rok'],grupa2K['Liczba'],color='c', bottom=grupa2M['Liczba'])
plt.xlabel('Rok')
plt.ylabel('Liczba')
plt.legend()
plt.show()
