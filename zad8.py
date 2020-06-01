import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
import random 

def generuj(n):
    rzuty=[]
    for i in range(n):
        liczba=random.randint(2,12)
        rzuty.append(liczba)
    plt.hist(rzuty, bins=2, facecolor='g', alpha=0.75, density=True)
    plt.xlabel('Suma rzutów')
    plt.ylabel('Prawdopodobieństwo')
    plt.title('Histogram')
    plt.grid(True)
    plt.show()

print(generuj(120))
