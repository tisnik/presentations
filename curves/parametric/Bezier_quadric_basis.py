"""Bázové polynomy Bézierovy kvadriky."""

#
# Použito v článku:
#
# Parametrické křivky používané v designu i při tvorbě animací
# https://www.root.cz/clanky/parametricke-krivky-pouzivane-v-designu-i-pri-tvorbe-animaci/
#
# Součást seriálu:
#
# Křivky nejen v počítačové grafice
# https://www.root.cz/serialy/krivky-nejen-v-pocitacove-grafice/
#
# Zdrojový kód tohoto skriptu ve stylu literate programming
# https://tisnik.github.io/presentations/appendix/lit_sources/parametric/Bezier_quadric_basis.html
#

import numpy as np
import matplotlib.pyplot as plt

# hodnoty parametru t
t = np.linspace(0, 1, 50)

# Bernsteinovy polynomy pro Bézierovu kvadriku
B = [1 * (1 - t) ** 2, 2 * t * (1 - t), 1 * t ** 2]

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle("Bázové polynomy", fontsize=15)

# určení rozsahů na obou souřadných osách
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# bázové polynomy
ax.plot(t, B[0], "r-", label="b0,2")
ax.plot(t, B[1], "g-", label="b1,2")
ax.plot(t, B[2], "b-", label="b2,2")

# zobrazení legendy
ax.legend()

# uložení grafu do rastrového obrázku
plt.savefig("bezier_quadric_basis_.png")

# zobrazení grafu
plt.show()
