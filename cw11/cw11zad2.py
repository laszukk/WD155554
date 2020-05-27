import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random

np.random.seed( 19680801 )

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

colory=['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
znaczniki=[',','.','v','^','o','s','<','>']

fig = plt.figure()
ax = fig.add_subplot( 111 , projection = '3d' )
n = 100

ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )

for x in range(6):
    zs = randrange(n,0 ,20)
    xs = randrange(n, 23 , 32 )
    ys = randrange(n, 0 , 100 )
    ax.scatter(xs, ys, zs, c =random.choice(colory), marker =random.choice(znaczniki))

plt.show()