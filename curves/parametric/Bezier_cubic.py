"""Parametrická křivka: Bézierova kubika."""

import numpy as np
import matplotlib.pyplot as plt

# hodnoty parametru t
t = np.arange(0, 1.05, 0.05)

# řídicí body Bézierovy kubiky
xc = (1, 1, 3, 3)
yc = (1, 2.9, 0.1, 2)

# Bernsteinovy polynomy
B = [(1-t)**3,
     3*t*(1-t)**2,
     3*t**2*(1-t),
     t**3]

# výpočet bodů ležících na Bézierově kubice
x = 0
y = 0
for i in range(0, 4):
    x += xc[i]*B[i]
    y += yc[i]*B[i]

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle('Bézierova kubika', fontsize=15)

# určení rozsahů na obou souřadných osách
ax.set_xlim(0, 4)
ax.set_ylim(0, 3)

# vrcholy na křivce pospojované úsečkami
ax.plot(x, y, 'g-')

# řídicí body Bézierovy kubiky
ax.plot(xc, yc, 'ro')

# uložení grafu do rastrového obrázku
plt.savefig("bezier_cubic.png")

# zobrazení grafu
plt.show()
