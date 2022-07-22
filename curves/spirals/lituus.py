"""Lituus."""

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
points = 300

# úhel v polárním grafu
theta = np.linspace(0.1, 8 * np.pi, points)

# koeficient spirály
k = 1

# funkce: vzdálenost od středu
radius = k / np.sqrt(theta)

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8), subplot_kw={"projection": "polar"})

# titulek grafu
fig.suptitle("Lituus", fontsize=15)

# vrcholy na křivce pospojované úsečkami
ax.plot(theta + (radius < 0) * np.pi, np.abs(radius), "g-")

# uložení grafu do rastrového obrázku
plt.savefig("lituus.png")

# zobrazení grafu
plt.show()
