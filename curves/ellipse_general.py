"""Parametrická křivka: obecná elipsa."""

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
# https://tisnik.github.io/presentations/appendix/lit_sources/basic/ellipse_general.html
#

import numpy as np

import matplotlib.pyplot as plt

# hodnoty parametru t
t = np.arange(0, 2 * np.pi, 0.1)

# poloměry elipsy v osách
a = 3.0
b = 2.0

# natočení celé elipsy
phi = np.pi / 4

# střed elipsy
xc = 0
yc = 0

# výpočet bodů ležících na elipse
x = xc + a * np.cos(t) * np.cos(phi) - b * np.sin(t) * np.sin(phi)
y = yc + a * np.cos(t) * np.sin(phi) + b * np.sin(t) * np.cos(phi)

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle("Obecná elipsa", fontsize=15)

# určení rozsahů na obou souřadných osách
ax.set_xlim(-4, 4)
ax.set_ylim(-3, 3)

# vrcholy na křivce pospojované úsečkami
ax.plot(x, y, "g-")

# vrcholy na křivce (každý čtvrtý)
ax.plot(x[::4], y[::4], "ro")

# uložení grafu do rastrového obrázku
plt.savefig("ellipse_general.png")

# zobrazení grafu
plt.show()
