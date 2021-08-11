"""Implicitně zadaná křivka."""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# příprava vektorů pro konstrukci mřížky
x = np.linspace(-5, 5, 150)
y = np.linspace(-5, 5, 150)

# konstrukce mřížky
x, y = np.meshgrid(x, y)

# implicitní funkce
z = np.sin(x**2) - np.cos(y**2)

fig = plt.figure()
ax = fig.gca(projection='3d')

# zobrazení 3D grafu formou plochy
surface = ax.plot_surface(x, y, z, rstride=2, cstride=2, cmap=cm.coolwarm,
                          linewidth=0, antialiased=False)

# titulek grafu
fig.suptitle('Sin/cos', fontsize=15)

# rozměry grafu ve směru osy x
ax.set_xlabel('X')
ax.set_xlim(-4, 4)

# rozměry grafu ve směru osy y
ax.set_ylabel('Y')
ax.set_ylim(-4, 4)

# rozměry grafu ve směru osy z
ax.set_zlabel('Z')
ax.set_zlim(-5, 15)

# uložení grafu do rastrového obrázku
plt.savefig("sin_cos_2.png")

# zobrazení grafu
plt.show()
