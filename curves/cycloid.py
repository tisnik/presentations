"""Parametrická křivka: cykloida."""

import numpy as np
import matplotlib.pyplot as plt

# hodnoty parametru t
t = np.arange(0, 3*np.pi, 0.1)

# poloměr kružnice
a = 1.0

# výpočet bodů ležících na cykloidě
x = a*(t-np.sin(t))
y = a*(1-np.cos(t))

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle('Cykloida', fontsize=15)

# vrcholy na křivce pospojované úsečkami
ax.plot(x, y, 'g-')

# vrcholy na křivce (každý pátý)
ax.plot(x[::5], y[::5], 'ro')

# uložení grafu do rastrového obrázku
plt.savefig("cycloid.png")

# zobrazení grafu
plt.show()
