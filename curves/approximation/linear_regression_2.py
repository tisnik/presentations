"""Vykreslení sady (pseudo)náhodných dat + lineární regrese."""

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
# https://tisnik.github.io/presentations/appendix/lit_sources/approximation/linear_regression_2.html
#

import numpy as np

import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.arange(0, 50)

# generátor pseudonáhodných dat
rng = np.random.default_rng(seed=42)

# hodnoty na y-ové ose
y = x + 2 * rng.random((len(x))) - 1

# výpočet lineární regrese
coefficients = np.polyfit(x, y, 1)

# koeficienty úsečky
print(coefficients)

# konstrukce lineární funkce
poly1d_fn = np.poly1d(coefficients)

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle("Lineární regrese", fontsize=15)

# vrcholy na křivce
ax.plot(x, y, "go")

# vykreslení interpolační křivky
plt.plot(poly1d_fn(np.arange(0, len(x))), "r-")

# uložení grafu do rastrového obrázku
plt.savefig("linear_regression_2.png")

# zobrazení grafu
plt.show()
