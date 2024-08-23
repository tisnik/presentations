"""Parametrická křivka: B-spline složená z Coonsových oblouků, násobné body."""

#
# Použito v článku:
#
# Křivky určené polynomem – nejpoužívanější křivky v současnosti
# https://www.root.cz/clanky/krivky-urcene-polynomem-nejpouzivanejsi-krivky-v-soucasnosti/
#
# Součást seriálu:
#
# Křivky nejen v počítačové grafice
# https://www.root.cz/serialy/krivky-nejen-v-pocitacove-grafice/
#
# Zdrojový kód tohoto skriptu ve stylu literate programming
# https://tisnik.github.io/presentations/appendix/lit_sources/parametric/B-spline-2.html
#

import numpy as np

import matplotlib.pyplot as plt

# hodnoty parametru t
t = np.linspace(0, 1, 20)

# řídicí body B-spline
xc = (1, 1, 2, 2.5, 3, 2)
yc = (1, 2, 2, 0.1, 2.9, 2.9)

# Coonsovy polynomy
C = [
    (1 - t) ** 3,
    3 * t ** 3 - 6 * t ** 2 + 4,
    -3 * t ** 3 + 3 * t ** 2 + 3 * t + 1,
    t ** 3,
]


def draw_coons_arc(xc, yc, ax, style):
    # výpočet bodů ležících na Coonsově kubice
    x = 0
    y = 0
    for i in range(0, 4):
        x += xc[i] * C[i]
        y += yc[i] * C[i]

    # konečná úprava sumy
    x /= 6
    y /= 6

    # vrcholy na křivce pospojované úsečkami
    ax.plot(x, y, style)


# rozměry grafu při uložení: 640x480 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

# titulek grafu
fig.suptitle("B-spline", fontsize=15)

# určení rozsahů na obou souřadných osách
ax.set_xlim(0, 4)
ax.set_ylim(0, 3)

# řídicí body B-spline
ax.plot(xc, yc, "k--", alpha=0.5)
ax.plot(xc, yc, "ro")

# oblouk s násobnými body
draw_coons_arc((xc[0], xc[0], xc[1], xc[2]), (yc[0], yc[0], yc[1], yc[2]), ax, "k-")

# první oblouk
draw_coons_arc(xc[0:4], yc[0:4], ax, "r-")

# druhý oblouk
draw_coons_arc(xc[1:5], yc[1:5], ax, "b-")

# třetí oblouk
draw_coons_arc(xc[2:6], yc[2:6], ax, "g-")

# oblouk s násobnými body
draw_coons_arc((xc[3], xc[4], xc[5], xc[5]), (yc[3], yc[4], yc[5], yc[5]), ax, "k-")

# uložení grafu do rastrového obrázku
plt.savefig("B-spline_2.png")

# zobrazení grafu
plt.show()
