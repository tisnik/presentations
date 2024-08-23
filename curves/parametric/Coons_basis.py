"""Bázové polynomy Coonsovy kubiky."""

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
# https://tisnik.github.io/presentations/appendix/lit_sources/parametric/Coons_basis.html
#

import numpy as np

import matplotlib.pyplot as plt

# hodnoty parametru t
t = np.arange(0, 1.05, 0.02)

# Coonsovy polynomy
C = [
    (1 - t) ** 3,
    3 * t ** 3 - 6 * t ** 2 + 4,
    -3 * t ** 3 + 3 * t ** 2 + 3 * t + 1,
    t ** 3,
]

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle("Bázové polynomy", fontsize=15)

# určení rozsahů na obou souřadných osách
ax.set_xlim(0, 1)
ax.set_ylim(0, 4)

# bázové polynomy
ax.plot(t, C[0], "r-")
ax.plot(t, C[1], "g-")
ax.plot(t, C[2], "b-")
ax.plot(t, C[3], "k-")

# uložení grafu do rastrového obrázku
plt.savefig("coons_basis.png")

# zobrazení grafu
plt.show()
