#!/usr/bin/env python

# Knihovny Numpy a matplotlib
#
# Dvacátý šestý demonstrační příklad:
# - zobrazení 3D grafu funkce typu z=f(x,y)
# - pomocná legenda - colorbar

import numpy as np
from mpl_toolkits.mplot3d import axes3d

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import FormatStrFormatter, LinearLocator

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

ax.set_zlim(-1.01, 1.01)

# styl formátování popisků
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter("%.02f"))

# přidání pomocné legendy
fig.colorbar(surface, shrink=0.7, aspect=5)

# zobrazení grafu
plt.show()
