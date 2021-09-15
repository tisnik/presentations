"""Triviální spirála - kružnice."""

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
theta = np.linspace(0.01, 8*np.pi, points)

# funkce: vzdálenost od středu
radius = np.full(shape=points, fill_value=1)

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8), subplot_kw={'projection': 'polar'})

# titulek grafu
fig.suptitle('Triviální spirála', fontsize=15)

# vrcholy na křivce pospojované úsečkami
ax.plot(theta, radius, 'g-')

# uložení grafu do rastrového obrázku
plt.savefig("trivial_spiral.png")

# zobrazení grafu
plt.show()
