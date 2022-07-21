"""Parametrická křivka: B-spline složená z Coonsových oblouků, posun vybraného řídicího bodu."""

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
# https://tisnik.github.io/presentations/appendix/lit_sources/parametric/B-spline-3.html
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


def draw_b_spline(filename, xc, yc, y):
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

    last = len(xc)

    # další oblouky
    for start in range(0, last - 3):
        style = "r-" if start % 2 == 0 else "b-"
        draw_coons_arc(xc[start : start + 4], yc[start : start + 4], ax, style)

    # uložení grafu do rastrového obrázku
    plt.savefig(filename)


draw_b_spline("B-spline_3A.png", xc, yc, 0.5)
draw_b_spline("B-spline_3B.png", xc, yc, 1.5)
draw_b_spline("B-spline_3C.png", xc, yc, 2.5)
