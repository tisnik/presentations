"""Úsečka zadaná implicitní funkcí."""

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
# https://tisnik.github.io/presentations/appendix/lit_sources/implicit/line1.html
#

import numpy as np
import matplotlib.pyplot as plt

# příprava vektorů pro konstrukci mřížky
x = np.linspace(-2, 2, 10)
y = np.linspace(-2, 2, 10)

# konstrukce mřížky
x, y = np.meshgrid(x, y)

# koeficienty úsečky
A = 1
B = 1
C = 0

# implicitní funkce úsečky
z = A * x + B * y + C

# hodnota, která se má zvýraznit na isoploše
levels = [0]

# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle("Úsečka", fontsize=15)

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
plt.savefig("line1.png")

# zobrazení grafu
plt.show()
