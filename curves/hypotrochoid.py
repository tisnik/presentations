"""Parametrická křivka: hypotrochoida."""

import numpy as np
import matplotlib.pyplot as plt

# hodnoty parametru t
t = np.arange(0, 2*np.pi, 0.01)

# parametry
R = 5
r = 3
d = 5

# výpočet bodů ležících na křivce
x = (R-r)*np.cos(t)+d*np.cos(t * (R-r/r))
y = (R-r)*np.sin(t)-d*np.sin(t * (R-r/r))

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle('Hypotrochoida', fontsize=15)

# určení rozsahů na obou souřadných osách
ax.set_xlim(-12, 12)
ax.set_ylim(-9, 9)

# vrcholy na křivce pospojované úsečkami
ax.plot(x, y, 'g-')

# uložení grafu do rastrového obrázku
plt.savefig("hypotrochoid.png")

# zobrazení grafu
plt.show()
