"""Vykreslení sady (pseudo)náhodných dat + polynomiální regrese."""

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
# https://tisnik.github.io/presentations/appendix/lit_sources/approximation/poly_regression_1.html
#

import numpy as np

import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.arange(0, 50)

# generátor pseudonáhodných dat
rng = np.random.default_rng(seed=42)

# hodnoty na y-ové ose
y = np.power(x, 2) + 100 * rng.random((len(x))) - 50

# výpočet lineární regrese
coefficients = np.polyfit(x, y, 1)

# koeficienty úsečky
print(coefficients)

# konstrukce polynomu
poly1d_fn = np.poly1d(coefficients)

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle("Polynomiální regrese", fontsize=15)

# vrcholy na křivce
ax.plot(x, y, "go")

# vykreslení interpolační křivky
plt.plot(poly1d_fn(np.arange(0, len(x))), "r-")

# uložení grafu do rastrového obrázku
plt.savefig("poly_regression_1.png")

# zobrazení grafu
plt.show()
