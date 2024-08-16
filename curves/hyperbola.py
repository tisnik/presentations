"""Hyperbola."""

#
# Použito v článku:
#
# Křivky v přírodě, architektuře, stavitelství i v počítačové grafice
# https://www.root.cz/clanky/krivky-v-prirode-architekture-stavitelstvi-i-v-pocitacove-grafice/
#
# Součást seriálu:
#
# Křivky nejen v počítačové grafice
# https://www.root.cz/serialy/krivky-nejen-v-pocitacove-grafice/
#
# Zdrojový kód tohoto skriptu ve stylu literate programming
# https://tisnik.github.io/presentations/appendix/lit_sources/basic/hyperbola.html
#

import numpy as np

import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.arange(-100, 101, 1)

# hodnoty na y-ové ose
y = 1 / x

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle("Hyperbola", fontsize=15)

# vrcholy na křivce pospojované úsečkami
ax.plot(x, y, "g-")

# vrcholy na křivce (každý pátý)
ax.plot(x[::5], y[::5], "ro")

# uložení grafu do rastrového obrázku
plt.savefig("hyperbola.png")

# zobrazení grafu
plt.show()
