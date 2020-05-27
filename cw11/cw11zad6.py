from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure( figsize =( 8 , 3 ))
ax = fig.add_subplot( 121 , projection = '3d' )
ax1 = fig.add_subplot( 122 , projection = '3d' )

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

ax1.plot(x, y, zs = 0 , zdir = 'y' ,c="g", label = 'curve in (x,y)' )
ax1.legend()
ax1.set_xlim( 0 , 1 )
ax1.set_ylim( 0 , 1 )
ax1.set_zlim( 0 , 1 ) 
ax1.set_xlabel( 'X' )
ax1.set_ylabel( 'Y' )
ax1.set_zlabel( 'Z' )
ax1.view_init( elev = 20. , azim =- 35 )

plt.show()