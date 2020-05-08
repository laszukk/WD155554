import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

dane=pd.read_csv('iris.csv')
print(dane)

dane1=dane[dane['species']=="setosa"]
dane2=dane[dane['species']=="versicolor"]
dane3=dane[dane['species']=="virginica"]

wykres1 = plt.scatter(dane1["sepal_length"], dane1["sepal_width"], color="c")
wykres2 = plt.scatter(dane2["sepal_length"], dane2["sepal_width"], color="r")
wykres3 = plt.scatter(dane3["sepal_length"], dane3["sepal_width"], color="purple")

plt.ylabel("Sepal length")
plt.xlabel("Sepal width")
plt.legend((wykres1,wykres2,wykres3),("setosa","versicolor","virginica"))
plt.show()
