"""Algebraická křivka."""

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
# https://tisnik.github.io/presentations/appendix/lit_sources/basic/algebraic.html
#

import numpy as np

import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.linspace(-3, 3, 70)

# hodnoty na y-ové ose
y = x ** 3 - 2 * x

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle("Algebraická křivka", fontsize=15)

# vrcholy na křivce pospojované úsečkami
ax.plot(x, y, "g-")

# vrcholy na křivce (každý pátý)
ax.plot(x[::5], y[::5], "ro")

# určení rozsahů na obou souřadných osách
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)

# uložení grafu do rastrového obrázku
plt.savefig("algebraic.png")

# zobrazení grafu
plt.show()
