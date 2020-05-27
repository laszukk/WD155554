# Projekcja 3d
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.gca( projection = '3d' )

x = np.linspace( 0 , 1 , 20 )
y = np.sin(x * 2 * np.pi) / 2 + 0.5
ax.scatter(x, y, zs = 0 , zdir = 'y' , c ="r", label = 'points in (x,z)' )

ax.legend()
ax.set_xlim( 0 , 1 )
ax.set_ylim( 0 , 1 )
ax.set_zlim( 0 , 1 ) 
ax.set_xlabel( 'X' )
ax.set_ylabel( 'Y' )
ax.set_zlabel( 'Z' )
ax.view_init( elev = 20. , azim =- 35 )

ax.plot(x, y, zs = 0 , zdir = 'y' ,c="g", label = 'curve in (x,y)' )

plt.show()