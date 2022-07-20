"""Parametrická křivka: hypocykloida."""

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
# https://tisnik.github.io/presentations/appendix/lit_sources/basic/hypocycloid1.html
#

import numpy as np
import matplotlib.pyplot as plt

# hodnoty parametru t
t = np.arange(0, 6 * np.pi, 0.01)

# parametry
a = 5
b = 3

# výpočet bodů ležících na křivce
x = (a - b) * np.cos(t) + b * np.cos((a / b - 1) * t)
y = (a - b) * np.sin(t) - b * np.sin((a / b - 1) * t)

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle("Hypocykloida", fontsize=15)

# určení rozsahů na obou souřadných osách
ax.set_xlim(-8, 8)
ax.set_ylim(-6, 6)

# vrcholy na křivce pospojované úsečkami
ax.plot(x, y, "g-")

# uložení grafu do rastrového obrázku
plt.savefig("hypocycloid1.png")

# zobrazení grafu
plt.show()
