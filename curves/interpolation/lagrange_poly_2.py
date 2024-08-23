"""Koeficienty Lagrangeova polynomu + vykreslení polynomu."""

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
# Založeno na příkladu z článku:
# https://pythonnumericalmethods.berkeley.edu/notebooks/chapter17.04-Lagrange-Polynomial-Interpolation.html
#
# Zdrojový kód tohoto skriptu ve stylu literate programming
# https://tisnik.github.io/presentations/appendix/lit_sources/interpolation/lagrange_poly_2.html
#

import numpy as np
import numpy.polynomial.polynomial as poly

import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = [0, 1, 2]

# hodnoty na y-ové ose
y = [1, 3, 2]

P1_coeff = [1, -1.5, 0.5]
P2_coeff = [0, 2, -1]
P3_coeff = [0, -0.5, 0.5]

# získání funkcí pro výpočet křivky na základě báze
P1 = poly.Polynomial(P1_coeff)
P2 = poly.Polynomial(P2_coeff)
P3 = poly.Polynomial(P3_coeff)

x_new = np.arange(-1.0, 3.1, 0.1)

# interpolační křivka
L = P1 + 3 * P2 + 2 * P3

# rozměry grafu při uložení: 640x480 pixelů
fig = plt.figure(figsize=(6.4, 4.8))

# vykreslení interpolační křivky i vstupních bodů
plt.plot(x_new, L(x_new), "b", x, y, "ro")

# popisky grafu
plt.title("Lagrange Polynomial")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()

# uložení grafu do rastrového obrázku
plt.savefig("langrange_poly_2.png")

# zobrazení grafu
plt.show()
