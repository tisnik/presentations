"""Hyperbolická spirála."""

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

# úhel v polárním grafu
theta = np.arange(1.00, 50.0, 0.05)

a = 1.0

# funkce: inverzní vzdálenost od středu
radius = a / theta

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8), subplot_kw={"projection": "polar"})

# titulek grafu
fig.suptitle("Hyperbolická spirála - obě ramena", fontsize=15)

# vrcholy na křivce pospojované úsečkami
ax.plot(theta, radius, "r-")

# vrcholy na křivce pospojované úsečkami
ax.plot(np.pi - theta, radius, "b-")

# uložení grafu do rastrového obrázku
plt.savefig("hyperbolic_spiral_2.png")

# zobrazení grafu
plt.show()
