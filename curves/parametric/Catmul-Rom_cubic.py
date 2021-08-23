"""Parametrická křivka: Catmul-Romova spline."""

import numpy as np
import matplotlib.pyplot as plt

# hodnoty parametru t
t = np.arange(0, 1.05, 0.05)

# řídicí body
xc = (1, 1, 3, 3)
yc = (1, 2.9, 0.1, 2)

# koeficient Catmul-Romovy spline
tau = 0.5

# bázové polynomy
Q = [-tau*t + 2*tau*t**2 - tau*t**3,
     1+(tau-3)*t**2+(2-tau)*t**3,
     tau*t + (3-2*tau)*t**2 + (tau-2)*t**3,
     -tau*t**2+tau*t**3]

# výpočet bodů ležících na spline
x = 0
y = 0
for i in range(0, 4):
    x += xc[i]*Q[i]
    y += yc[i]*Q[i]

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle('Catmul-Romova spline', fontsize=15)

# určení rozsahů na obou souřadných osách
ax.set_xlim(0, 4)
ax.set_ylim(0, 3)

# vrcholy na křivce pospojované úsečkami
ax.plot(x, y, 'g-')

# řídicí body kubiky
ax.plot(xc, yc, 'ro')

# uložení grafu do rastrového obrázku
plt.savefig("catmul-rom_cubic.png")

# zobrazení grafu
plt.show()
