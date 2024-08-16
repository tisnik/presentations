"""Rovinná křivka: řetězovka."""

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
# https://tisnik.github.io/presentations/appendix/lit_sources/basic/catenary.html
#

import numpy as np

import matplotlib.pyplot as plt

# hodnoty parametru x
x = np.arange(-4, 4, 0.04)

# poloměr křivosti ve vrcholu
a = 1.0

# výpočet bodů ležících na řetězovce
y = a * np.cosh(x / a)

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle("Řetězovka", fontsize=15)

# vrcholy na křivce pospojované úsečkami
ax.plot(x, y, "g-")

# vrcholy na křivce (každý pátý)
ax.plot(x[::5], y[::5], "ro")

# uložení grafu do rastrového obrázku
plt.savefig("cateanry.png")

# zobrazení grafu
plt.show()
