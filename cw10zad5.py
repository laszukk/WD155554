import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import random

dane=pd.read_csv('iris.csv')
print(dane)

dane1=dane[dane['species']=="setosa"]
dane2=dane[dane['species']=="versicolor"]
dane3=dane[dane['species']=="virginica"]
s1=abs(dane1["petal_length"]-dane1["petal_width"])
s2=abs(dane2["petal_length"]-dane2["petal_width"])
s3=abs(dane3["petal_length"]-dane3["petal_width"])

wykres1 = plt.scatter(dane1["sepal_length"], dane1["sepal_width"],s=s1, color=(random.random(),random.random(),random.random()))
wykres2 = plt.scatter(dane2["sepal_length"], dane2["sepal_width"],s=s2, color=(random.random(),random.random(),random.random()))
wykres3 = plt.scatter(dane3["sepal_length"], dane3["sepal_width"],s=s3,  color=(random.random(),random.random(),random.random()))

plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()