import math

import numpy as np

import matplotlib.pyplot as plt

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

# počet hodnot na x-ové ose
points = 300

# hodnoty na x-ové ose
x = np.linspace(0, 5, points)


# vektorizace předchozích funkcí
y_s = np.sin(x)
y_c = np.cos(x)

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle("sin(x) a cos(x)", fontsize=15)

# vrcholy na křivce pospojované úsečkami
ax.plot(x, y_s, "r-")

# vrcholy na křivce pospojované úsečkami
ax.plot(x, y_c, "b-")

# uložení grafu do rastrového obrázku
plt.savefig("sin_cos.png")

# zobrazení grafu
plt.show()
