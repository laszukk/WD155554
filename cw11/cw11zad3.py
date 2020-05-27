import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import random
import matplotlib.gridspec as gridspec


fig = plt.figure(figsize=(8,3))
X = np.arange(- 5 , 5 , 0.25 )
Y = np.arange(- 5 , 5 , 0.25 )
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X** 2 + Y** 2 )
Z = np.sin(R)

kolory=['flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
            'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg', 'hsv',
            'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar']


for x in range(1,6):
    ax = fig.add_subplot(1, 5, x, projection='3d')
    kolor=random.choice(kolory)
    surf = ax.plot_surface(X, Y, Z, cmap =kolor,
    linewidth = 0 , antialiased = False )
    ax.set_zlim(- 1.01 , 1.01 )
    ax.zaxis.set_major_locator(LinearLocator( 10 ))
    ax.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))
    fig.colorbar(surf, shrink = 0.5 , aspect = 5 )
plt.show()