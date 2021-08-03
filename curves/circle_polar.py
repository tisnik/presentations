"""Kružnice vykreslená v polárním grafu."""

import numpy as np
import matplotlib.pyplot as plt

# úhel v polárním grafu
theta = np.arange(0.00, 2*np.pi, 0.05)

a = 1.0

# funkce: vzdálenost od středu
radius = np.repeat(a, len(theta))

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8), subplot_kw={'projection': 'polar'})

# titulek grafu
fig.suptitle('Kružnice', fontsize=15)

# vrcholy na křivce pospojované úsečkami
ax.plot(theta, radius, 'g-')

# uložení grafu do rastrového obrázku
plt.savefig("circle_polar.png")

# zobrazení grafu
plt.show()
