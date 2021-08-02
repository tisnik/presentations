"""Fresnel fractal generator."""

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
f = 0.0

for i in range(n):
    f += 0.05
    x += cos(f * f)
    y += sin(f * f)
    xa[i] = x
    ya[i] = y

# vrcholy na křivce pospojované úsečkami
plt.plot(xa, ya, 'b')

# uložení grafu do rastrového obrázku
plt.savefig("fresnel.png")

# zobrazení grafu
plt.show()
