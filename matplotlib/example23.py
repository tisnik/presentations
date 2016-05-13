#!/usr/bin/env python

# Knihovny Numpy a matplotlib
#
# Dvacátý třetí demonstrační příklad:
# - zobrazení kontur funkce typu z=f(x,y)
# - zobrazení hodnot u jednotlivých "vrstevnic"
# - přidání legendy

import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


delta = 0.1

# průběh nezávislé proměnné x
x = np.arange(-10.0, 10.0, delta)

# průběh nezávislé proměnné y
y = np.arange(-10.0, 10.0, delta)

# vytvoření dvou polí se souřadnicemi [x,y] 
X, Y = np.meshgrid(x, y)

# vzdálenost od bodu [0,0]
R1 = np.sqrt(X*X+Y*Y)

# vzdálenost od bodu [3,3]
R2 = np.sqrt((X-3)*(X-3)+(Y-3)*(Y-3))

# výpočet funkce, kterou použijeme při vykreslování grafu
Z = np.sin(R1)-np.cos(R2)

# povolení zobrazení mřížky
plt.grid(True)

# vytvoření grafu s konturami funkce z=f(x,y)
CS = plt.contour(X, Y, Z)

# přidání legendy (colorbar)
CB = plt.colorbar(CS, shrink=0.7, extend='both')

# popisky "vrstevnic"
plt.clabel(CS, inline=1, fontsize=10)

# zobrazení grafu
plt.show()

