"""Parametrická křivka: hypotrochoida."""

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
# https://tisnik.github.io/presentations/appendix/lit_sources/basic/hypotrochoid3.html
#

import numpy as np

import matplotlib.pyplot as plt

# hodnoty parametru t
t = np.arange(0, 2 * np.pi, 0.01)

# parametry
R = 3
r = 1
d = 2

# výpočet bodů ležících na křivce
x = (R - r) * np.cos(t) + d * np.cos(t * (R - r) / r)
y = (R - r) * np.sin(t) - d * np.sin(t * (R - r) / r)

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle("Hypotrochoida", fontsize=15)

# určení rozsahů na obou souřadných osách
ax.set_xlim(-6, 6)
ax.set_ylim(-4, 4)

# vrcholy na křivce pospojované úsečkami
ax.plot(x, y, "g-")

# uložení grafu do rastrového obrázku
plt.savefig("hypotrochoid3.png")

# zobrazení grafu
plt.show()
