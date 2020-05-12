import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 30, 0.1)
s = np.sin(x)
c = np.cos(x)
plt.plot(x+1.5, s+2, label='sin(x)')
plt.plot(x, c, label='cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([0,30,-1,3])
plt.legend()
plt.show()