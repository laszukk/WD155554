import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 30, 0.1)
s = np.sin(x)
c = np.cos(x)
plt.plot(x, s, label='sin(x)')
plt.plot(x, c, label='cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([0,30,-8,8])
plt.legend()
plt.show()