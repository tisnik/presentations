"""Parametrická křivka: lineární interpolace."""

#
# Použito v článku:
#
# Parametrické křivky používané v designu i při tvorbě animací
# https://www.root.cz/clanky/parametricke-krivky-pouzivane-v-designu-i-pri-tvorbe-animaci/
#
# Součást seriálu:
#
# Křivky nejen v počítačové grafice
# https://www.root.cz/serialy/krivky-nejen-v-pocitacove-grafice/
#
# Zdrojový kód tohoto skriptu ve stylu literate programming
# https://tisnik.github.io/presentations/appendix/lit_sources/parametric/linear_interpolation.html
#

import numpy as np

import matplotlib.pyplot as plt

# hodnoty parametru t
t = np.arange(0, 1.05, 0.05)

# řídicí body
xc = (1, 3)
yc = (1, 2)

# Bernsteinovy polynomy pro lineární interpolaci
B = [1 * (1 - t), 1 * t]

# výpočet bodů ležících na interpolační křivce
x = 0
y = 0
for i in range(0, 2):
    x += xc[i] * B[i]
    y += yc[i] * B[i]

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle("Lineární interpolace", fontsize=15)

# určení rozsahů na obou souřadných osách
ax.set_xlim(0, 4)
ax.set_ylim(0, 3)

# vrcholy na křivce pospojované úsečkami
ax.plot(x, y, "g-")

# řídicí body
ax.plot(xc, yc, "ro")

# uložení grafu do rastrového obrázku
plt.savefig("linear_interpolation.png")

# zobrazení grafu
plt.show()
