"""Fermatova spirála."""

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
# https://tisnik.github.io/presentations/appendix/lit_sources/basic/fermats_spiral.html
#

import numpy as np

import matplotlib.pyplot as plt

# úhel v polárním grafu
theta = np.arange(0.00, 20.0, 0.05)

a = 1.0

# funkce: vzdálenost od středu
radius = a * np.sqrt(theta)

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8), subplot_kw={"projection": "polar"})

# titulek grafu
fig.suptitle("Fermatova spirála", fontsize=15)

# vrcholy na křivce pospojované úsečkami
ax.plot(theta, radius, "g-")

# uložení grafu do rastrového obrázku
plt.savefig("fermat_spiral.png")

# zobrazení grafu
plt.show()
