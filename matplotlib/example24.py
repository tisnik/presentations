#!/usr/bin/env python

# Knihovny Numpy a matplotlib
#
# Dvacátý čtvrtý demonstrační příklad:
# - zobrazení 3D grafu funkce typu z=f(x,y)

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

delta = 0.1

# průběh nezávislé proměnné x
x = np.arange(-10.0, 10.0, delta)

# průběh nezávislé proměnné y
y = np.arange(-10.0, 10.0, delta)

# vytvoření dvou polí se souřadnicemi [x,y] 
X, Y = np.meshgrid(x, y)

# vzdálenost od bodu [0,0]
R = np.sqrt(X*X+Y*Y)

# výpočet funkce, kterou použijeme při vykreslování grafu
Z = np.sin(R)/R

# zobrazení 3D grafu
ax.plot_wireframe(X, Y, Z, rstride=7, cstride=7)

# zobrazení grafu
plt.show()

