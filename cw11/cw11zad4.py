import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure( figsize =( 8 , 3 ))
ax1 = fig.add_subplot(1, 5, 1, projection='3d')
ax2 = fig.add_subplot(1, 5, 2, projection='3d')
ax3 = fig.add_subplot(1, 5, 3, projection='3d')
ax4 = fig.add_subplot(1, 5, 4, projection='3d')
ax5 = fig.add_subplot(1, 5, 5, projection='3d')


_x = np.arange( 4 )
_y = np.arange( 5 )
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = x + y
bottom = np.zeros_like(top)
width = depth = 1
ax1.bar3d(x, y, top, width, depth, bottom, shade = True )
ax2.bar3d(x, y, bottom, width, depth, top, shade = False )
ax3.bar3d(x, y, bottom, width, depth, bottom, shade = True )
ax4.bar3d(x, y, top, width, depth, top, shade = False )
ax5.bar3d(x, y, bottom, width, depth, top, shade = True )
plt.show()