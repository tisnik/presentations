"""Bázové polynomy Bézierovy kvartiky."""

import numpy as np
import matplotlib.pyplot as plt

# hodnoty parametru t
t = np.arange(0, 1.05, 0.02)

# Bernsteinovy polynomy pro Bézierovu kvartiku
B = [1 * (1-t)**4,
     4 * t * (1-t)**3,
     6 * t**2 * (1-t)**2,
     4 * t**3 * (1-t),
     1 * t**4]

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle('Bázové polynomy', fontsize=15)

# určení rozsahů na obou souřadných osách
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# bázové polynomy
ax.plot(t, B[0], 'r-', label='b0,4')
ax.plot(t, B[1], 'g-', label='b1,4')
ax.plot(t, B[2], 'b-', label='b2,4')
ax.plot(t, B[3], 'k-', label='b3,4')
ax.plot(t, B[4], 'm-', label='b4,4')

# zobrazení legendy
ax.legend()

# uložení grafu do rastrového obrázku
plt.savefig("bezier_quartic_basis_.png")

# zobrazení grafu
plt.show()
