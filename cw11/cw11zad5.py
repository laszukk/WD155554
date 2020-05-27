import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

fig = plt.figure( figsize =( 8 , 3 ))
ax = fig.add_subplot( 121 , projection = '3d' )
ax1 = fig.add_subplot( 122 , projection = '3d' )

X = np.arange(- 5 , 5 , 0.25 )
Y = np.arange(- 5 , 5 , 0.25 )
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X** 2 + Y** 2 )
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, cmap =cm.coolwarm,
linewidth = 0 , antialiased = False )
ax.set_zlim(- 1.01 , 1.01 )
ax.zaxis.set_major_locator(LinearLocator( 10 ))
ax.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))
fig.colorbar(surf, shrink = 0.5 , aspect = 5 )

X = np.arange(- 5 , 5 , 0.1 )
Y = np.arange(- 5 , 5 , 0.1 )
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X** 2 + Y** 2 )
Z = np.sin(R)
surf = ax1.plot_surface(X, Y, Z, cmap =cm.coolwarm,
linewidth = 0 , antialiased = True )
ax1.set_zlim(- 1.01 , 1.01 )
ax1.zaxis.set_major_locator(LinearLocator( 10 ))
ax1.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))
fig.colorbar(surf, shrink = 0.5 , aspect = 5 )

plt.show()