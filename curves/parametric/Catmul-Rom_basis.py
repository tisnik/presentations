"""Bázové polynomy Catmul-Romovy spline."""

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
# https://tisnik.github.io/presentations/appendix/lit_sources/parametric/Catmul-Rom_basis.html
#

import numpy as np
import matplotlib.pyplot as plt

# hodnoty parametru t
t = np.linspace(0, 1, 50)

# koeficient Catmul-Romovy spline
tau = 0.5

# bázové polynomy
Q = [
    -tau * t + 2 * tau * t ** 2 - tau * t ** 3,
    1 + (tau - 3) * t ** 2 + (2 - tau) * t ** 3,
    tau * t + (3 - 2 * tau) * t ** 2 + (tau - 2) * t ** 3,
    -tau * t ** 2 + tau * t ** 3,
]

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle("Bázové polynomy", fontsize=15)

# určení rozsahů na obou souřadných osách
ax.set_xlim(0, 1)
ax.set_ylim(-0.25, 1)

# bázové polynomy
ax.plot(t, Q[0], "r-")
ax.plot(t, Q[1], "g-")
ax.plot(t, Q[2], "b-")
ax.plot(t, Q[3], "k-")

# uložení grafu do rastrového obrázku
plt.savefig("catmul-rom_basis.png")

# zobrazení grafu
plt.show()
