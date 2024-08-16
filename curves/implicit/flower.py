"""Křivka zadaná implicitní funkcí."""

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
# https://tisnik.github.io/presentations/appendix/lit_sources/implicit/flower.html
#

import numpy as np

import matplotlib.pyplot as plt

# číslo snímku
frame = 1

for step in (10, 20, 50, 100, 150, 200, 300, 500, 1000, 2000, 5000):
    # příprava vektorů pro konstrukci mřížky
    x = np.linspace(-1.5, 1.5, step)
    y = np.linspace(-1.5, 1.5, step)

    # konstrukce mřížky
    x, y = np.meshgrid(x, y)

    # implicitní funkce
    z = (3 * x ** 2 - y ** 2) ** 2 * y ** 2 - (x ** 2 + y ** 2) ** 4

    # hodnota, která se má zvýraznit na isoploše
    levels = [0]

    # rozměry grafu při uložení: 640x480 pixelů
    fig, ax = plt.subplots(1, figsize=(6.4, 4.8))

    # titulek grafu
    fig.suptitle("Flower, step={}".format(step), fontsize=15)

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
    plt.savefig("flower_{:02}.png".format(frame))

    # další snímek
    frame += 1
