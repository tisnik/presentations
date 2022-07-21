"""Hermitova spline."""

#
# Použito v článku:
#
# Parametrické křivky používané v designu i při tvorbě animací (dokončení)
# https://www.root.cz/clanky/parametricke-krivky-pouzivane-v-designu-i-pri-tvorbe-animaci-dokonceni/
#
# Součást seriálu:
#
# Křivky nejen v počítačové grafice
# https://www.root.cz/serialy/krivky-nejen-v-pocitacove-grafice/
#
# Zdrojový kód tohoto skriptu ve stylu literate programming
# https://tisnik.github.io/presentations/appendix/lit_sources/parametric/Hermite_spline.html
#

import numpy as np
import matplotlib.pyplot as plt

# hodnoty parametru t
t = np.linspace(0, 1, 50)

# řídicí body spline
xc = (1, 3)
yc = (1, 1)

# tangenty
mx = (0, 0)
my = (1, -1)

# bázové polynomy
H = [
    2 * t ** 3 - 3 * t ** 2 + 1,
    t ** 3 - 2 * t ** 2 + t,
    -2 * t ** 3 + 3 * t ** 2,
    t ** 3 - t ** 2,
]

# výpočet bodů ležících na spline
x = xc[0] * H[0] + mx[0] * H[1] + xc[1] * H[2] + mx[1] * H[3]
y = yc[0] * H[0] + my[0] * H[1] + yc[1] * H[2] + my[1] * H[3]

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle("Hermitova spline", fontsize=15)

# určení rozsahů na obou souřadných osách
ax.set_xlim(0, 4)
ax.set_ylim(-0.5, 2.5)

# vrcholy na křivce pospojované úsečkami
ax.plot(x, y, "g-")

# řídicí body
ax.plot(xc, yc, "ro")

# tangenty
ax.plot([xc[0] + mx[0], xc[0]], [yc[0] + my[0], yc[0]], "b-")
ax.plot([xc[1] + mx[1], xc[1]], [yc[1] + my[1], yc[1]], "y-")

# uložení grafu do rastrového obrázku
plt.savefig("hermite_spline.png")

# zobrazení grafu
plt.show()
