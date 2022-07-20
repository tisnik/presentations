"""Fresnel fractal generator."""

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
# https://tisnik.github.io/presentations/appendix/lit_sources/basic/fresnel.html
#

import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos

# Celkový počet vypočtených bodů
n = 10000

# Prozatím prázdná pole připravená pro uložení výsledků výpočtu.
xa = np.zeros((n,))
ya = np.zeros((n,))


x = 0.0
y = 0.0
t = 0.0

for i in range(n):
    t += 0.05
    x += cos(t * t)
    y += sin(t * t)
    xa[i] = x
    ya[i] = y

# vrcholy na křivce pospojované úsečkami
plt.plot(xa, ya, "b")

# uložení grafu do rastrového obrázku
plt.savefig("fresnel.png")

# zobrazení grafu
plt.show()
