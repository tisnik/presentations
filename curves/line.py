"""Nejjednodušší křivka: úsečka."""

import numpy as np
import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.arange(0, 100)

# hodnoty na y-ové ose (sklon úsečky řízen konstantou)
y = x * 0.3

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle('Úsečka', fontsize=15)

# vrcholy na křivce pospojované úsečkami
ax.plot(x, y, 'g-')

# vrcholy na křivce (každý pátý)
ax.plot(x[::5], y[::5], 'ro')

# uložení grafu do rastrového obrázku
plt.savefig("line.png")

# zobrazení grafu
plt.show()
