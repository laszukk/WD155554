import numpy as np

def fibo():
    wyrazy=[]
    a,b=0,1
    wyrazy.append(a)
    wyrazy.append(b)
    i=2
    while i<25:
        wyrazy.append(a+b)
        a,b=b,a+b
        i+=1
    wyrazy=np.asarray(wyrazy)
    wyrazy=wyrazy.reshape(5,5)
    return wyrazy
    
print(fibo())
    
