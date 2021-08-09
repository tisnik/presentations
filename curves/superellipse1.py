"""Parametrická křivka: superelipsa."""

import numpy as np
import matplotlib.pyplot as plt

# hodnoty parametru t
t = np.arange(0, 2*np.pi, 0.1)

# poloměry superelipsy v osách
a = 3.0
b = 3.0

# určení tvaru křivky
n = 1

# výpočet bodů ležících na elipse
x = a*(np.cos(t) ** n)
y = b*(np.sin(t) ** n)

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle('Superelipsa', fontsize=15)

# určení rozsahů na obou souřadných osách
ax.set_xlim(-4, 4)
ax.set_ylim(-3, 3)

# vrcholy na křivce pospojované úsečkami
ax.plot(x, y, 'g-')

# uložení grafu do rastrového obrázku
plt.savefig("superellipse1.png")

# zobrazení grafu
plt.show()
