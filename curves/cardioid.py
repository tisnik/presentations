"""Parametrická křivka: kardioida/srdcovka."""

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
# https://tisnik.github.io/presentations/appendix/lit_sources/basic/cardioid.html
#

import numpy as np
import matplotlib.pyplot as plt

# hodnoty parametru t
t = np.arange(0, 3 * np.pi, 0.1)

# poloměr kružnice
a = 1.0

# výpočet bodů ležících na srdcovce
x = a * (2 * np.cos(t) - np.cos(2 * t))
y = a * (2 * np.sin(t) - np.sin(2 * t))

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle("Srdcovka", fontsize=15)

# určení rozsahů na obou souřadných osách
ax.set_xlim(-4, 4)
ax.set_ylim(-3, 3)

# vrcholy na křivce pospojované úsečkami
ax.plot(x, y, "g-")

# vrcholy na křivce (každý pátý)
ax.plot(x[::5], y[::5], "ro")

# uložení grafu do rastrového obrázku
plt.savefig("cardioid.png")

# zobrazení grafu
plt.show()
