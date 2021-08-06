"""Kružnice zadaná implicitní funkcí."""

import numpy as np
import matplotlib.pyplot as plt

# příprava vektorů pro konstrukci mřížky
x = np.linspace(-2, 2, 50)
y = np.linspace(-2, 2, 50)

# konstrukce mřížky
x, y = np.meshgrid(x, y)

# implicitní funkce kružnice
r = 1
z = x**2 + y ** 2 - r ** 2

# hodnota, která se má zvýraznit na isoploše
levels = [0]

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle('Kružnice', fontsize=15)

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
plt.savefig("circle2.png")

# zobrazení grafu
plt.show()
