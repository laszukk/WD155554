import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 20, 0.1)
s = 1/x
plt.plot(x+1, s, label='f(x)=1/x')
plt.axis([1, 20, 0, 1])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()