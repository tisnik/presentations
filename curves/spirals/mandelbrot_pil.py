#!/usr/bin/env python

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

"""Vykreslení klasické Mandelbrotovy množiny."""

import palette_greens
from PIL import Image

# textura by měla být čtvercová a její šířka i výška by měla být
# mocninou čísla 2
IMAGE_WIDTH = 256
IMAGE_HEIGHT = 256


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
    width, height = image.size  # rozměry obrázku
    stepx = (xmax - xmin) / width
    stepy = (ymax - ymin) / height

    y1 = ymin
    for y in range(0, height):
        x1 = xmin
        for x in range(0, width):
            i = mandelbrot(x1, y1, maxiter)
            i = 3 * i % 256
            color = (palette[i][0], palette[i][1], palette[i][2])
            image.putpixel((x, y), color)
            x1 += stepx
        y1 += stepy


image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT))

recalc_fractal(image, palette_greens.palette, -2.0, -1.5, 1.0, 1.5, 1000)
image.save("mandelbrot.png")
