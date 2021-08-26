"""Bázové polynomy pro lineární interpolaci."""

import numpy as np
import matplotlib.pyplot as plt

# hodnoty parametru t
t = np.linspace(0, 1, 50)

# Bernsteinovy polynomy pro lineární interpolaci
B = [1 * (1-t),
     1 * t]

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle('Bázové polynomy', fontsize=15)

# určení rozsahů na obou souřadných osách
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# bázové polynomy
ax.plot(t, B[0], 'r-', label='b0,1')
ax.plot(t, B[1], 'g-', label='b1,1')

# zobrazení legendy
ax.legend()

# uložení grafu do rastrového obrázku
plt.savefig("linear_basis.png")

# zobrazení grafu
plt.show()
