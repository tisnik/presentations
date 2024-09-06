#!/usr/bin/env python

# Knihovny Numpy a matplotlib
#
# Dvacátý osmý demonstrační příklad:
# - zobrazení 3D grafu funkce typu [x,y,z]=f(t)

import numpy as np
from mpl_toolkits.mplot3d import axes3d

import matplotlib.pyplot as plt

# nezávislá proměnná
t = np.arange(0, 8 * np.pi, 0.1)

# vzdálenost od osy spirály
r = 10.0 / (t + 4)

# výpočet souřadnic [x,y,z]) pro každé t
x = r * np.cos(t)
y = r * np.sin(t)
z = t

fig = plt.figure()
ax = fig.gca(projection="3d")

# vykreslení grafu
ax.plot(x, y, z)

# zobrazení grafu
plt.show()
