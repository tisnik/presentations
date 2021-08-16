"""Vykreslení sady (pseudo)náhodných dat."""

import numpy as np
import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.arange(0, 50)

# generátor pseudonáhodných dat
rng = np.random.default_rng(seed=42)

# hodnoty na y-ové ose
y = np.power(x, 2) + 10*rng.random((len(x))) - 5

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle('Pseudonáhodná data', fontsize=15)

# vrcholy na křivce
ax.plot(x, y, 'go')

# uložení grafu do rastrového obrázku
plt.savefig("random_data_poly.png")

# zobrazení grafu
plt.show()
