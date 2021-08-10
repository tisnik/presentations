"""Parabola zadaná implicitní funkcí."""

import numpy as np
import matplotlib.pyplot as plt

# příprava vektorů pro konstrukci mřížky
x = np.linspace(-4, 4, 50)
y = np.linspace(0, 8, 50)

# konstrukce mřížky
x, y = np.meshgrid(x, y)

# implicitní funkce paraboly
f = 0.5
p = 2*f
z = x**2 - p*p*y

fig = plt.figure()
ax = fig.gca(projection='3d')

# zobrazení 3D grafu formou kontur
ax.contour3D(x, y, z, 50, cmap='binary')

# titulek grafu
fig.suptitle('Parabola', fontsize=15)

# rozměry grafu ve směru osy x
ax.set_xlabel('X')
ax.set_xlim(-4, 4)

# rozměry grafu ve směru osy y
ax.set_ylabel('Y')
ax.set_ylim(0, 8)

# rozměry grafu ve směru osy z
ax.set_zlabel('Z')
ax.set_zlim(0, 10)

# uložení grafu do rastrového obrázku
plt.savefig("parabola2.png")

# zobrazení grafu
plt.show()
