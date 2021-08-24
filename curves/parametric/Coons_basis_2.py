"""Bázové polynomy Coonsovy kubiky."""

import numpy as np
import matplotlib.pyplot as plt

# hodnoty parametru t
t = np.arange(0, 1.05, 0.02)

# Coonsovy polynomy
C = [(1-t)**3,
     3*t**3 - 6*t**2 + 4,
     -3*t**3 + 3*t**2 + 3*t + 1,
     t**3]

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle('Bázové polynomy', fontsize=15)

# určení rozsahů na obou souřadných osách
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# bázové polynomy
ax.plot(t, C[0]/6, 'r-')
ax.plot(t, C[1]/6, 'g-')
ax.plot(t, C[2]/6, 'b-')
ax.plot(t, C[3]/6, 'k-')

# uložení grafu do rastrového obrázku
plt.savefig("coons_basis.png")

# zobrazení grafu
plt.show()
