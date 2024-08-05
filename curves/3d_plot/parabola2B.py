"""Parabola zadaná implicitní funkcí."""

#
# Použito v článku:
#
# Křivky popsané implicitní funkcí, animace křivek
# https://www.root.cz/clanky/krivky-popsane-implicitni-funkci-animace-krivek/
#
# Součást seriálu:
#
# Křivky nejen v počítačové grafice
# https://www.root.cz/serialy/krivky-nejen-v-pocitacove-grafice/
#
# Zdrojový kód tohoto skriptu ve stylu literate programming
# https://tisnik.github.io/presentations/appendix/lit_sources/3d_plot/parabola2B.html
#

import numpy as np

import matplotlib.pyplot as plt

# příprava vektorů pro konstrukci mřížky
x = np.linspace(-4, 4, 50)
y = np.linspace(0, 8, 50)

# konstrukce mřížky
x, y = np.meshgrid(x, y)

# implicitní funkce paraboly
f = 0.5
p = 2 * f
z = x ** 2 - p * p * y

# inicializace grafu
fig = plt.figure()

# nastavení 3D projekce
ax = fig.gca(projection="3d")

# zobrazení 3D grafu formou kontur
ax.contour3D(x, y, z, 50, cmap="binary")

# titulek grafu
fig.suptitle("Parabola", fontsize=15)

# kontura: průmět na rovinu x-y
cset = ax.contour(x, y, z, zdir="z", offset=10)

# rozměry grafu ve směru osy x
ax.set_xlabel("X")
ax.set_xlim(-4, 4)

# rozměry grafu ve směru osy y
ax.set_ylabel("Y")
ax.set_ylim(0, 8)

# rozměry grafu ve směru osy z
ax.set_zlabel("Z")
ax.set_zlim(0, 10)

# uložení grafu do rastrového obrázku
plt.savefig("parabola2.png")

# zobrazení grafu
plt.show()
