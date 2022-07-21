"""Interpolace Lagrangeovým polynomem."""

#
# Použito v článku:
#
# Křivky určené polynomem – nejpoužívanější křivky v současnosti
# https://www.root.cz/clanky/krivky-urcene-polynomem-nejpouzivanejsi-krivky-v-soucasnosti/
#
# Součást seriálu:
#
# Křivky nejen v počítačové grafice
# https://www.root.cz/serialy/krivky-nejen-v-pocitacove-grafice/
#
# Zdrojový kód tohoto skriptu ve stylu literate programming
# https://tisnik.github.io/presentations/appendix/lit_sources/interpolation/lagrange_interpolation_2.html
#

import numpy as np
import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.arange(1, 11, 1)

# hodnoty na y-ové ose
y = [1, 3, 2, 3, -1, 3, 2, 2, -1, 0]

# odvození stupně Lagrangeova polynomu
n = len(x)

# příprava polí pro výpočet hodnot Lagrangeovým polynomem
xp = np.arange(1, 10.1, 0.1)
yp = np.zeros(91)

# výpočet interpolační křivky
for i in range(n):
    p = 1
    for j in range(n):
        if i != j:
            p = p * (xp - x[j]) / (x[i] - x[j])
    yp += p * y[i]

# rozměry grafu při uložení: 640x480 pixelů
fig = plt.figure(figsize=(6.4, 4.8))

# vstupní hodnoty
plt.plot(x, y, "ko")

# vlastní interpolace polynomem
plt.plot(xp, yp, "r-")

# popisky grafu
plt.title("Lagrange Interpolation")
plt.xlabel("x")
plt.ylabel("y")

# zobrazení mřížky
plt.grid()

# uložení grafu do rastrového obrázku
plt.savefig("langrange_interpolation_2.png")

# zobrazení grafu
plt.show()
