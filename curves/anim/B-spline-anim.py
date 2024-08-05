"""Parametrická křivka: B-spline složená z Coonsových oblouků, násobné body."""

#
# Použito v článku:
#
# Parametrické křivky používané v designu i při tvorbě animací (dokončení)
# https://www.root.cz/clanky/parametricke-krivky-pouzivane-v-designu-i-pri-tvorbe-animaci-dokonceni/
#
# Součást seriálu:
#
# Křivky nejen v počítačové grafice
# https://www.root.cz/serialy/krivky-nejen-v-pocitacove-grafice/
#
# Zdrojový kód tohoto skriptu ve stylu literate programming
# https://tisnik.github.io/presentations/appendix/lit_sources/anim/B-spline-anim.html
#

import numpy as np

import matplotlib.pyplot as plt

# hodnoty parametru t
t = np.linspace(0, 1, 20)

# řídicí body B-spline
xc = [1, 2, 3, 4, 5, 6, 7]
yc = [1, 2, 1, 2, 1, 2, 1]

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


def draw_b_spline(filename, xc, yc, draw_first_arcs, draw_second_arcs, y):
    # změnit polohu prostředního řídicího bodu
    yc[3] = y

    # rozměry grafu při uložení: 640x480 pixelů
    fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

    # titulek grafu
    fig.suptitle("B-spline", fontsize=15)

    # určení rozsahů na obou souřadných osách
    ax.set_xlim(0.5, 7.5)
    ax.set_ylim(0.5, 2.5)

    # řídicí body B-spline
    ax.plot(xc, yc, "k--", alpha=0.5)
    ax.plot(xc, yc, "ro")

    # první dva oblouky s násobnými body
    if draw_first_arcs:
        draw_coons_arc(
            (xc[0], xc[0], xc[0], xc[1]), (yc[0], yc[0], yc[0], yc[1]), ax, "g-"
        )

    if draw_second_arcs:
        draw_coons_arc(
            (xc[0], xc[0], xc[1], xc[2]), (yc[0], yc[0], yc[1], yc[2]), ax, "y-"
        )

    last = len(xc)

    # další oblouky
    for start in range(0, last - 3):
        style = "r-" if start % 2 == 0 else "b-"
        draw_coons_arc(xc[start : start + 4], yc[start : start + 4], ax, style)

    # poslední dva oblouky s násobnými body
    if draw_second_arcs:
        draw_coons_arc(
            (xc[last - 3], xc[last - 2], xc[last - 1], xc[last - 1]),
            (yc[last - 3], yc[last - 2], yc[last - 1], yc[last - 1]),
            ax,
            "y-",
        )

    if draw_first_arcs:
        draw_coons_arc(
            (xc[last - 2], xc[last - 1], xc[last - 1], xc[last - 1]),
            (yc[last - 2], yc[last - 1], yc[last - 1], yc[last - 1]),
            ax,
            "g-",
        )

    # uložení grafu do rastrového obrázku
    plt.savefig(filename)


frame = 0
for y in np.linspace(0.5, 2.5, 30):
    draw_b_spline("b-spline_anim_{:02}.png".format(frame), xc, yc, True, True, y)

    # další snímek
    frame += 1
