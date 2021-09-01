"""Parametrická křivka: Catmul-Romova spline, násobné body."""

import numpy as np
import matplotlib.pyplot as plt

# hodnoty parametru t
t = np.linspace(0, 1, 20)

# řídicí body Catmul-Romovy spline
xc1 = [1, 2, 3, 4, 5, 6, 7]
yc1 = [1, 2, 1, 2, 1, 2, 1]

# násobné řídicí body Catmul-Romovy spline
xc2 = [1, 2, 3, 4, 4, 5, 6, 7]
yc2 = [1, 2, 1, 2, 2, 1, 2, 1]

# násobné řídicí body Catmul-Romovy spline
xc3 = [1, 2, 3, 4, 4, 4, 5, 6, 7]
yc3 = [1, 2, 1, 2, 2, 2, 1, 2, 1]

# koeficient Catmul-Romovy spline
tau = 0.5

# bázové polynomy
Q = [-tau*t + 2*tau*t**2 - tau*t**3,
     1+(tau-3)*t**2+(2-tau)*t**3,
     tau*t + (3-2*tau)*t**2 + (tau-2)*t**3,
     -tau*t**2+tau*t**3]


def draw_catmul_rom_arc(xc, yc, ax, style):
    x = 0
    y = 0
    for i in range(0, 4):
        x += xc[i]*Q[i]
        y += yc[i]*Q[i]

    # vrcholy na křivce pospojované úsečkami
    ax.plot(x, y, style)


def draw_catmul_rom_spline(filename, xc, yc, draw_first_arcs, draw_second_arcs):
    # rozměry grafu při uložení: 640x480 pixelů
    fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

    # titulek grafu
    fig.suptitle('Catmul-Rom spline', fontsize=15)

    # určení rozsahů na obou souřadných osách
    ax.set_xlim(0.5, 7.5)
    ax.set_ylim(0.5, 2.5)

    # řídicí body Catmul-Romovy spline
    ax.plot(xc, yc, 'k--', alpha=0.5)
    ax.plot(xc, yc, 'ro')

    # první dva oblouky s násobnými body
    if draw_first_arcs:
        draw_catmul_rom_arc((xc[0], xc[0], xc[0], xc[1]),
                            (yc[0], yc[0], yc[0], yc[1]), ax, "g-")

    if draw_second_arcs:
        draw_catmul_rom_arc((xc[0], xc[0], xc[1], xc[2]),
                            (yc[0], yc[0], yc[1], yc[2]), ax, "y-")

    last = len(xc)

    # další oblouky
    for start in range(0, last-3):
        style = "r-" if start % 2 == 0 else "b-"
        draw_catmul_rom_arc(xc[start:start+4], yc[start:start+4], ax, style)

    # poslední dva oblouky s násobnými body
    if draw_second_arcs:
        draw_catmul_rom_arc((xc[last-3], xc[last-2], xc[last-1], xc[last-1]),
                            (yc[last-3], yc[last-2], yc[last-1], yc[last-1]), ax, "y-")

    if draw_first_arcs:
        draw_catmul_rom_arc((xc[last-2], xc[last-1], xc[last-1], xc[last-1]),
                            (yc[last-2], yc[last-1], yc[last-1], yc[last-1]), ax, "g-")

    # uložení grafu do rastrového obrázku
    plt.savefig(filename)

    # zobrazení grafu
    plt.show()


# čtyři varianty B-spline křivky
draw_catmul_rom_spline("Catmul-Rom-spline_4A.png", xc1, yc1, False, False)
draw_catmul_rom_spline("Catmul-Rom-spline_4B.png", xc2, yc2, False, False)
draw_catmul_rom_spline("Catmul-Rom-spline_4C.png", xc3, yc3, False, False)
