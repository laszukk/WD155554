import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.gca( projection = '3d' )

z = np.linspace( 0 , 2 * np.pi, 100 )
x = np.sin(z)
y =2*np.cos(z)
ax.plot(x, y, z, label = 'zadanie 1' )
ax.legend()
plt.show()
