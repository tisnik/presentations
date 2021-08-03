"""Parabola versus řetězovka."""

import numpy as np
import matplotlib.pyplot as plt

# hodnoty parametru x
x = np.arange(-3, 3, 0.04)

# parabola: hodnoty na y-ové ose (sklon úsečky řízen konstantou)
y1 = np.power(x, 2)

# poloměr křivosti ve vrcholu
a = 1.0

# řetězovka: výpočet bodů ležících na řetězovce
y2 = a*np.cosh(x/a)-1

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle('Parabola versus řetězovka #1', fontsize=15)

# vrcholy na křivce pospojované úsečkami
ax.plot(x, y1, 'g-', label="Parabola")

# vrcholy na křivce pospojované úsečkami
ax.plot(x, y2, 'r-', label="Řetězovka")

# zobrazení popisku křivek
plt.legend()

# uložení grafu do rastrového obrázku
plt.savefig("parabola_catenary.png")

# zobrazení grafu
plt.show()
