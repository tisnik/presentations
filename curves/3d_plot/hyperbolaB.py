"""Hyperbola zadaná implicitní funkcí."""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# příprava vektorů pro konstrukci mřížky
x = np.linspace(-4, 4, 50)
y = np.linspace(-4, 4, 50)

# konstrukce mřížky
x, y = np.meshgrid(x, y)

# implicitní funkce hyperboly
a = 1
z = (x**2 - y**2)/a**2 - 1

fig = plt.figure()
ax = fig.gca(projection='3d')

# zobrazení 3D grafu formou plochy
surface = ax.plot_surface(x, y, z, rstride=2, cstride=2, cmap=cm.coolwarm,
                          linewidth=0, antialiased=False)

# titulek grafu
fig.suptitle('Hyperbola', fontsize=15)

# kontura: průmět na rovinu x-y
cset = ax.contour(x, y, z, zdir='z', offset=10)

# rozměry grafu ve směru osy x
ax.set_xlabel('X')
ax.set_xlim(-4, 4)

# rozměry grafu ve směru osy y
ax.set_ylabel('Y')
ax.set_ylim(-4, 4)

# rozměry grafu ve směru osy z
ax.set_zlabel('Z')
ax.set_zlim(-10, 10)

# uložení grafu do rastrového obrázku
plt.savefig("hyperbola.png")

# zobrazení grafu
plt.show()
