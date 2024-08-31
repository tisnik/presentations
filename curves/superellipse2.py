"""Parametrická křivka: superelipsa."""

#
# Použito v článku:
#
# Křivky v přírodě, architektuře, stavitelství i v počítačové grafice: matematický popis křivek
# https://www.root.cz/clanky/krivky-v-prirode-architekture-stavitelstvi-i-v-pocitacove-grafice-matematicky-popis-krivek/
#
# Součást seriálu:
#
# Křivky nejen v počítačové grafice
# https://www.root.cz/serialy/krivky-nejen-v-pocitacove-grafice/
#
# Zdrojový kód tohoto skriptu ve stylu literate programming
# https://tisnik.github.io/presentations/appendix/lit_sources/basic/superellipse2.html
#

import numpy as np

import matplotlib.pyplot as plt

# hodnoty parametru t
t = np.arange(0, 2 * np.pi, 0.1)

# poloměry superelipsy v osách
a = 3.0
b = 3.0

# určení tvaru křivky
n = 3

# výpočet bodů ležících na elipse
x = a * (np.cos(t) ** n)
y = b * (np.sin(t) ** n)

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle("Superelipsa", fontsize=15)

# určení rozsahů na obou souřadných osách
ax.set_xlim(-4, 4)
ax.set_ylim(-3, 3)

# vrcholy na křivce pospojované úsečkami
ax.plot(x, y, "g-")

# uložení grafu do rastrového obrázku
plt.savefig("superellipse2.png")

# zobrazení grafu
plt.show()
