"""Fermatova spirála."""

#
# Použito v článku:
#
# Křivky v přírodě i v počítačové grafice – svět spirál
# https://www.root.cz/clanky/krivky-v-prirode-i-v-pocitacove-grafice-svet-spiral/
#
# Součást seriálu:
#
# Křivky nejen v počítačové grafice
# https://www.root.cz/serialy/krivky-nejen-v-pocitacove-grafice/
#

import numpy as np

import matplotlib.pyplot as plt

# počet bodů na spirále
points = 150

# úhel v polárním grafu
theta = np.linspace(0, 4 * np.pi, points)

# funkce: vzdálenost od středu
radius = np.sqrt(theta)

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8), subplot_kw={"projection": "polar"})

# titulek grafu
fig.suptitle("Fermatova spirála", fontsize=15)

# vrcholy na křivce pospojované úsečkami
ax.plot(theta + (radius < 0) * np.pi, np.abs(radius), "r-")

# druhá polovina křivky
ax.plot(np.pi + theta + (radius < 0) * np.pi, np.abs(radius), "b-")

# uložení grafu do rastrového obrázku
plt.savefig("fermat_spiral.png")

# zobrazení grafu
plt.show()
