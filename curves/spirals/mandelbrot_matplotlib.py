"""Vykreslení klasické Mandelbrotovy množiny."""

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

import palette_greens


# velikost bitmapy s nakresleným fraktálem
WIDTH = 256
HEIGHT = 256


def mandelbrot(cx, cy, maxiter):
    """Výpočet, kolik iterací je nutné pro opuštění jednotkového kruhu."""
    c = complex(cx, cy)
    z = 0
    for i in range(0, maxiter):
        if abs(z) > 2:
            return i
        z = z * z + c
    return 0


def recalc_fractal(image, palette, xmin, ymin, xmax, ymax, maxiter=1000):
    """Přepočet celého fraktálu."""
    stepx = (xmax - xmin) / WIDTH
    stepy = (ymax - ymin) / HEIGHT

    y1 = ymin
    for y in range(0, HEIGHT):
        x1 = xmin
        for x in range(0, WIDTH):
            i = mandelbrot(x1, y1, maxiter)
            i = 3 * i % 256
            for index in range(0, 3):
                image[y][x][index] = palette[i][index]
                image[y][x][index] = palette[i][index]
                image[y][x][index] = palette[i][index]
            x1 += stepx
        y1 += stepy


# vytvoření prázdné bitmapy
image = np.zeros(shape=(HEIGHT, WIDTH, 3), dtype=np.uint8)

recalc_fractal(image, palette_greens.palette, -2.0, -1.5, 1.0, 1.5, 1000)

# vykreslení bitmapy do grafu
plt.figure(1, figsize=(8, 6), dpi=100)
plt.imshow(image)

# uložení grafu do rastrového obrázku
plt.savefig("test.png")

# zobrazení grafu s bitmapou
plt.show()
