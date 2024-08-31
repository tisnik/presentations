"""Evolventa."""

#
# Použito v článku:
#
# Křivky v přírodě i v počítačové grafice – svět spirál (dokončení)
# https://www.root.cz/clanky/krivky-v-prirode-i-v-pocitacove-grafice-svet-spiral-dokonceni/
#
# Součást seriálu:
#
# Křivky nejen v počítačové grafice
# https://www.root.cz/serialy/krivky-nejen-v-pocitacove-grafice/
#

import numpy as np

import matplotlib.pyplot as plt

# nezávislý parametr t
t = np.linspace(0.00, 3 * np.pi, 100)

# koeficient evolventy
r = 10

# funkce kružnice
xc = r * np.cos(t)
yc = r * np.sin(t)


def draw_evolvent(ax, a, style):
    # funkce evolventy
    xe = r * (np.cos(t) + (t - a) * np.sin(t))
    ye = r * (np.sin(t) - (t - a) * np.cos(t))

    # vrcholy na křivce pospojované úsečkami
    ax.plot(xe, ye, style)


# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle("Evolventa", fontsize=15)

# určení rozsahů na obou souřadných osách
ax.set_xlim(-100, 140)
ax.set_ylim(-80, 100)

# vrcholy na kružnici
ax.plot(xc, yc, "r-")

# vykreslení několika evolvent, pokaždé s jiným koeficientem a
draw_evolvent(ax, -0.5, "g-")
draw_evolvent(ax, 0, "m-")
draw_evolvent(ax, 0.5, "c-")

# uložení grafu do rastrového obrázku
plt.savefig("involute3.png")

# zobrazení grafu
plt.show()
