"""Parametrická křivka: Bézierova kvadrika."""

#
# Použito v článku:
#
# Křivky určené polynomem – nejpoužívanější křivky v současnosti
# https://www.root.cz/clanky/krivky-urcene-polynomem-nejpouzivanejsi-krivky-v-soucasnosti/
#
# Součást seriálu:
#
# Křivky nejen v počítačové grafice
# https://www.root.cz/serialy/krivky-nejen-v-pocitacove-grafice/
#
# Zdrojový kód tohoto skriptu ve stylu literate programming
# https://tisnik.github.io/presentations/appendix/lit_sources/parametric/Bezier_kvadric.html
#

import numpy as np

import matplotlib.pyplot as plt

# hodnoty parametru t
t = np.arange(0, 1.05, 0.05)

# řídicí body Bézierovy kubiky
xc = (1, 2, 3)
yc = (1, 2.9, 1)

# Bernsteinovy polynomy pro Bézierovu kvadriku
B = [(1 - t) ** 2, 2 * t * (1 - t), t ** 2]

# výpočet bodů ležících na Bézierově kvadrice
x = 0
y = 0
for i in range(0, 3):
    x += xc[i] * B[i]
    y += yc[i] * B[i]

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle("Bézierova kvadrika", fontsize=15)

# určení rozsahů na obou souřadných osách
ax.set_xlim(0, 4)
ax.set_ylim(0, 3)

# vrcholy na křivce pospojované úsečkami
ax.plot(x, y, "g-")

# řídicí body Bézierovy kvadriky
ax.plot(xc, yc, "ro")

# uložení grafu do rastrového obrázku
plt.savefig("bezier_quadric.png")

# zobrazení grafu
plt.show()
