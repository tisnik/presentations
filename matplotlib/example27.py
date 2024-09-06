#!/usr/bin/env python

# Knihovny Numpy a matplotlib
#
# Dvacátý sedmý demonstrační příklad:
# - zobrazení 3D grafu funkce typu z=f(x,y)
# - pomocná legenda - colorbar
# - promítnutí grafu na ploch kolmých na osy

import numpy as np
from mpl_toolkits.mplot3d import axes3d

import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure()
ax = fig.gca(projection="3d")

delta = 0.1

# průběh nezávislé proměnné x
x = np.arange(-10.0, 10.0, delta)

# průběh nezávislé proměnné y
y = np.arange(-10.0, 10.0, delta)

# vytvoření dvou polí se souřadnicemi [x,y]
X, Y = np.meshgrid(x, y)

# vzdálenost od bodu [0,0]
R = np.sqrt(X * X + Y * Y)

# výpočet funkce, kterou použijeme při vykreslování grafu
Z = np.sin(R) / R

# zobrazení 3D grafu formou plochy
surface = ax.plot_surface(
    X, Y, Z, rstride=2, cstride=2, cmap=cm.coolwarm, linewidth=0, antialiased=False
)

# kontutra: průmět na rovinu x-y
cset = ax.contour(X, Y, Z, zdir="z", offset=-5, cmap=cm.coolwarm)

# kontutra: průmět na rovinu y-z
cset = ax.contour(X, Y, Z, zdir="x", offset=-15, cmap=cm.coolwarm)

# kontutra: průmět na rovinu x-z
cset = ax.contour(X, Y, Z, zdir="y", offset=15, cmap=cm.coolwarm)

# rozměry grafu ve směru osy x
ax.set_xlabel("X")
ax.set_xlim(-15, 15)

# rozměry grafu ve směru osy y
ax.set_ylabel("Y")
ax.set_ylim(-15, 15)

# rozměry grafu ve směru osy z
ax.set_zlabel("Z")
ax.set_zlim(-5, 5)

# zobrazení grafu
plt.show()
