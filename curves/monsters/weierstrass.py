"""Průběh Weierstrassovy funkce."""

#
# Použito v článku:
#
# Patologické křivky a jiná matematická monstra
# https://www.root.cz/clanky/patologicke-krivky-a-jina-matematicka-monstra/
#
# Součást seriálu:
#
# Křivky nejen v počítačové grafice
# https://www.root.cz/serialy/krivky-nejen-v-pocitacove-grafice/
#
# Zdrojový kód tohoto skriptu ve stylu literate programming
# https://tisnik.github.io/presentations/appendix/lit_sources/monsters/weierstrass.html
#

import numpy as np
import matplotlib.pyplot as plt

# hodnoty parametru x
x = np.linspace(-2, 2, 500)

# úroveň detailů
details = 100

# koeficienty
a = 0.7
b = 7


def weierstrass(x, a, b, details):
    """Definice Weierstrassovy funkce."""
    w = 0
    for n in range(0, details):
        w += a ** n * np.cos(b ** n * np.pi * x)
    return w


# příprava na vlastní výpočet
y = np.vectorize(weierstrass)

# výpočet s převodem na typ numpy_array
approx = y(x, a, b, details)

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle("Wiererstrassova funkce", fontsize=15)

# vrcholy na křivce pospojované úsečkami
ax.plot(x, approx, "g-")

# uložení grafu do rastrového obrázku
plt.savefig("weierstrass.png")

# zobrazení grafu
plt.show()
