"""Koeficienty Lagrangeova polynomu."""

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
# https://tisnik.github.io/presentations/appendix/lit_sources/interpolation/lagrange_poly_1.html
#

import numpy as np
import numpy.polynomial.polynomial as poly

import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = [0, 1, 2]

# vstupní koeficienty
P1_coeff = [1, -1.5, 0.5]
P2_coeff = [0, 2, -1]
P3_coeff = [0, -0.5, 0.5]

# získání funkcí pro výpočet křivky na základě báze
P1 = poly.Polynomial(P1_coeff)
P2 = poly.Polynomial(P2_coeff)
P3 = poly.Polynomial(P3_coeff)

x_new = np.arange(-1.0, 3.1, 0.1)

# rozměry grafu při uložení: 640x480 pixelů
fig = plt.figure(figsize=(6.4, 4.8))

# vykreslení jednotlivých bází
plt.plot(x_new, P1(x_new), "b", label="P1")
plt.plot(x_new, P2(x_new), "r", label="P2")
plt.plot(x_new, P3(x_new), "g", label="P3")

# zobrazení pomocných bodů v mřížce

plt.plot(x, np.ones(len(x)), "ko", x, np.zeros(len(x)), "ko")

# popisky grafu
plt.title("Lagrange Basis Polynomials")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()

# uložení grafu do rastrového obrázku
plt.savefig("langrange_poly_1.png")

# zobrazení grafu
plt.show()
