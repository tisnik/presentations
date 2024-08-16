"""Obecná elipsa zadaná implicitní funkcí."""

#
# Použito v článku:
#
# Křivky popsané implicitní funkcí, animace křivek
# https://www.root.cz/clanky/krivky-popsane-implicitni-funkci-animace-krivek/
#
# Součást seriálu:
#
# Křivky nejen v počítačové grafice
# https://www.root.cz/serialy/krivky-nejen-v-pocitacove-grafice/
#
# Zdrojový kód tohoto skriptu ve stylu literate programming
# https://tisnik.github.io/presentations/appendix/lit_sources/implicit/ellipse3.html
#

import numpy as np

import matplotlib.pyplot as plt

# příprava vektorů pro konstrukci mřížky
x = np.linspace(-4, 4, 50)
y = np.linspace(-4, 4, 50)

# konstrukce mřížky
x, y = np.meshgrid(x, y)

# parametry obecné elipsy
x0 = 0
y0 = 0
a = 2
b = 3
phi = -np.pi / 4

# pomocné členy
a2 = a ** 2
b2 = b ** 2
sin2 = np.sin(phi) ** 2
cos2 = np.cos(phi) ** 2

A = a2 * sin2 + b2 * cos2
B = 2 * (b2 - a2) * np.sin(phi) * np.cos(phi)
C = a2 * cos2 + b2 * sin2
D = -2 * A * x0 - B * y0
E = -B * x0 - 2 * C * y0
F = A * x0 ** 2 + B * x0 * y0 + C * y0 ** 2 - a2 * b2

# implicitní funkce obecné elipsy
z = A * x ** 2 + B * x * y + C * y ** 2 + D * x + E * y + F

# hodnota, která se má zvýraznit na isoploše
levels = [0]

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle("Elipsa", fontsize=15)

# vykreslení implicitní funkce
ax.contour(x, y, z, levels)

# zobrazit mřížku
ax.grid(True)

# zachovat poměr stran
ax.axis("scaled")

# popisek os
plt.xlabel("Osa x")
plt.ylabel("Osa y")

# uložení grafu do rastrového obrázku
plt.savefig("ellipse3.png")

# zobrazení grafu
plt.show()
