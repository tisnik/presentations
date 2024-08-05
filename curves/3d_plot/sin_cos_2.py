"""Implicitně zadaná křivka."""

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
# https://tisnik.github.io/presentations/appendix/lit_sources/3d_plot/sin_cos_2.html
#

import numpy as np

import matplotlib.cm as cm
import matplotlib.pyplot as plt

# příprava vektorů pro konstrukci mřížky
x = np.linspace(-5, 5, 150)
y = np.linspace(-5, 5, 150)

# konstrukce mřížky
x, y = np.meshgrid(x, y)

# implicitní funkce
z = np.sin(x ** 2) - np.cos(y ** 2)

# inicializace grafu
fig = plt.figure()

# nastavení 3D projekce
ax = fig.gca(projection="3d")

# zobrazení 3D grafu formou plochy
surface = ax.plot_surface(
    x, y, z, rstride=2, cstride=2, cmap=cm.coolwarm, linewidth=0, antialiased=False
)

# titulek grafu
fig.suptitle("Sin/cos", fontsize=15)

# rozměry grafu ve směru osy x
ax.set_xlabel("X")
ax.set_xlim(-4, 4)

# rozměry grafu ve směru osy y
ax.set_ylabel("Y")
ax.set_ylim(-4, 4)

# rozměry grafu ve směru osy z
ax.set_zlabel("Z")
ax.set_zlim(-5, 15)

# uložení grafu do rastrového obrázku
plt.savefig("sin_cos_2.png")

# zobrazení grafu
plt.show()
