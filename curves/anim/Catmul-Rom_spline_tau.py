"""Parametrická křivka: Catmul-Romova spline s násobnými body."""

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
# https://tisnik.github.io/presentations/appendix/lit_sources/anim/Catmul-Rom_spline_tau.html
#

import numpy as np
import matplotlib.pyplot as plt

# hodnoty parametru t
t = np.arange(0, 1.05, 0.05)

# řídicí body B-spline
xc = (1, 1, 2, 2.5, 3, 2)
yc = (1, 2, 2, 0.1, 2.9, 2.9)


def draw_catmul_rom_arc(xc, yc, ax, style):
    x = 0
    y = 0
    for i in range(0, 4):
        x += xc[i] * Q[i]
        y += yc[i] * Q[i]

    # vrcholy na křivce pospojované úsečkami
    ax.plot(x, y, style)


# koeficient Catmul-Romovy spline
tau_1 = 0.0
tau_2 = 1.0

frame = 0
for tau in np.linspace(tau_1, tau_2, 10):

    # bázové polynomy
    Q = [
        -tau * t + 2 * tau * t ** 2 - tau * t ** 3,
        1 + (tau - 3) * t ** 2 + (2 - tau) * t ** 3,
        tau * t + (3 - 2 * tau) * t ** 2 + (tau - 2) * t ** 3,
        -tau * t ** 2 + tau * t ** 3,
    ]

    # rozměry grafu při uložení: 640x480 pixelů
    fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

    # titulek grafu
    fig.suptitle("Catmul-Rom spline", fontsize=15)

    # určení rozsahů na obou souřadných osách
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 4)

    # řídicí body B-spline
    ax.plot(xc, yc, "k--", alpha=0.5)
    ax.plot(xc, yc, "ro")

    # oblouk s násobnými body
    draw_catmul_rom_arc(
        (xc[0], xc[0], xc[1], xc[2]), (yc[0], yc[0], yc[1], yc[2]), ax, "k-"
    )

    # první oblouk
    draw_catmul_rom_arc(xc[0:4], yc[0:4], ax, "r-")

    # druhý oblouk
    draw_catmul_rom_arc(xc[1:5], yc[1:5], ax, "b-")

    # třetí oblouk
    draw_catmul_rom_arc(xc[2:6], yc[2:6], ax, "g-")

    # oblouk s násobnými body
    draw_catmul_rom_arc(
        (xc[3], xc[4], xc[5], xc[5]), (yc[3], yc[4], yc[5], yc[5]), ax, "k-"
    )

    # uložení grafu do rastrového obrázku
    plt.savefig("catmul-rom_anim_{:02}.png".format(frame))

    # další snímek
    frame += 1
