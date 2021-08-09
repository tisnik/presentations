"""Parametrická křivka: epicykloida."""

import numpy as np
import matplotlib.pyplot as plt

# hodnoty parametru t
t = np.arange(0, 26*np.pi, 0.01)

# parametry
a = 11
b = 13

# výpočet bodů ležících na křivce
x = (a+b)*np.cos(t)-b*np.cos((a/b+1)*t)
y = (a+b)*np.sin(t)-b*np.sin((a/b+1)*t)

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle('Epicyklodia', fontsize=15)

# určení rozsahů na obou souřadných osách
ax.set_xlim(-64, 64)
ax.set_ylim(-48, 48)

# vrcholy na křivce pospojované úsečkami
ax.plot(x, y, 'g-')

# uložení grafu do rastrového obrázku
plt.savefig("epycyclodid2.png")

# zobrazení grafu
plt.show()
