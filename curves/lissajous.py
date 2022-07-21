"""Parametrická křivka: Lissajousův obrazec."""

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
# https://tisnik.github.io/presentations/appendix/lit_sources/basic/lissajous.html
#

import numpy as np
import matplotlib.pyplot as plt

# hodnoty parametru t
t = np.arange(0, 2 * np.pi, 0.02)

# poloměry v osách
a = 3.0
b = 3.0

#
kx = 3
ky = 2

# výpočet bodů ležících na obrazci
x = a * np.cos(kx * t)
y = b * np.sin(ky * t)

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle("Lissajousův obrazec", fontsize=15)

# určení rozsahů na obou souřadných osách
ax.set_xlim(-4, 4)
ax.set_ylim(-3, 3)

# vrcholy na křivce pospojované úsečkami
ax.plot(x, y, "g-")

# vrcholy na křivce (každý čtvrtý)
ax.plot(x[::4], y[::4], "ro")

# uložení grafu do rastrového obrázku
plt.savefig("lissajous.png")

# zobrazení grafu
plt.show()
