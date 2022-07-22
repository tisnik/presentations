"""Evolventa cykloidy."""

#
# Použito v článku:
#
# Křivky v přírodě i v počítačové grafice – svět spirál (dokončení)
# https://www.root.cz/clanky/krivky-v-prirode-i-v-pocitacove-grafice-svet-spiral-dokonceni/
#
# Součást seriálu:
#
# Křivky nejen v počítačové grafice
# https://www.root.cz/serialy/krivky-nejen-v-pocitacove-grafice/
#

import numpy as np
import matplotlib.pyplot as plt

# nezávislý parametr t
t = np.linspace(0.00, 2 * np.pi, 100)

# funkce cykloidy
xc = t - np.sin(t)
yc = 1 - np.cos(t)

# funkce evolventy
xe = t + np.sin(t)
ye = 3 + np.cos(t)

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle("Evolventa cykloidy", fontsize=15)

# vrcholy na cykloidě
ax.plot(xc, yc, "r-")

# vrcholy na křivce pospojované úsečkami
ax.plot(xe, ye, "g-")

# uložení grafu do rastrového obrázku
plt.savefig("involute4.png")

# zobrazení grafu
plt.show()
