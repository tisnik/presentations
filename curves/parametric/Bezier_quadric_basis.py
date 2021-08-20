"""Bázové polynomy Bézierovy kvadriky."""

import numpy as np
import matplotlib.pyplot as plt

# hodnoty parametru t
t = np.arange(0, 1.05, 0.02)

# Bernsteinovy polynomy pro Bézierovu kvadriku
B = [1 * (1-t)**2,
     2 * t * (1-t),
     1 * t**2]

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle('Bázové polynomy', fontsize=15)

# určení rozsahů na obou souřadných osách
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# bázové polynomy
ax.plot(t, B[0], 'r-', label='b0,2')
ax.plot(t, B[1], 'g-', label='b1,2')
ax.plot(t, B[2], 'b-', label='b2,2')

# zobrazení legendy
ax.legend()

# uložení grafu do rastrového obrázku
plt.savefig("bezier_quadric_basis_.png")

# zobrazení grafu
plt.show()
