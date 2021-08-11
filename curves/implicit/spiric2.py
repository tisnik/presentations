"""Křivka získaná řezem toru."""

import numpy as np
import matplotlib.pyplot as plt

# příprava vektorů pro konstrukci mřížky
x = np.linspace(-4, 4, 150)
y = np.linspace(-4, 4, 150)

# konstrukce mřížky
x, y = np.meshgrid(x, y)

# parametry toru
a = 1
b = 2
c = 0.99

# pomocné členy
d = 2*(a**2+b**2-c**2)
e = 2*(a**2-b**2-c**2)
f = -(a+b+c)*(a+b-c)*(a-b+c)*(a-b-c)

# implicitní funkce křivky
z = (x**2+y**2)**2 - d*x**2 - e*y**2 - f

# hodnota, která se má zvýraznit na isoploše
levels = [0]

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle('Spiric', fontsize=15)

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
plt.savefig("spiric2.png")

# zobrazení grafu
plt.show()
