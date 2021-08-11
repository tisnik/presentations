"""Eliptická křivka."""

import numpy as np
import matplotlib.pyplot as plt

# příprava vektorů pro konstrukci mřížky
x = np.linspace(-2, 2, 50)
y = np.linspace(-2, 2, 50)

# konstrukce mřížky
x, y = np.meshgrid(x, y)

# koeficienty eliptické křivky
a = -2.0
b = 0.0

# implicitní funkce eliptické křivky
z = x**3 + a*x + b - y**2

# hodnota, která se má zvýraznit na isoploše
levels = [0]

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle('Eliptická křivka', fontsize=15)

# vykreslení implicitní funkce
ax.contour(x, y, z, levels)

# zobrazit mřížku
ax.grid(True)

# zachovat poměr stran
ax.axis('scaled')

# popisek os
plt.xlabel('Osa x')
plt.ylabel('Osa y')

# uložení grafu do rastrového obrázku
plt.savefig("elliptic1.png")

# zobrazení grafu
plt.show()
