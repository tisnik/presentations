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

"""Vykreslení spirál v Juliových množinách."""

from PIL import Image
import palette_greens

IMAGE_WIDTH = 800
IMAGE_HEIGHT = 600


def julia(cx, cy, zx, zy, maxiter):
    """Výpočet, kolik iterací je nutné pro opuštění jednotkového kruhu."""
    c = complex(cx, cy)
    z = complex(zx, zy)
    for i in range(0, maxiter):
        if abs(z) > 2:
            return i
        z = z * z + c
    return 0


def recalc_fractal(image, palette, cx, cy, maxiter=1000):
    """Přepočet celého fraktálu."""
    xmin = -2.0
    ymin = -1.5
    xmax = 2.0
    ymax = 1.5
    width, height = image.size  # rozměry obrázku
    stepx = (xmax - xmin) / width
    stepy = (ymax - ymin) / height

    y1 = ymin
    for y in range(0, height):
        x1 = xmin
        for x in range(0, width):
            i = julia(cx, cy, x1, y1, maxiter)
            i = 3 * i % 256
            color = (palette[i][0], palette[i][1], palette[i][2])
            image.putpixel((x, y), color)
            x1 += stepx
        y1 += stepy


image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT))

recalc_fractal(
    image,
    palette_greens.palette,
    -0.769824999999999998320,
    -0.109270000000000000000,
    255,
)
image.save("spiral_1.png")

recalc_fractal(
    image,
    palette_greens.palette,
    -0.171119200000000013445,
    0.657309400000000000000,
    255,
)
image.save("spiral_2.png")

recalc_fractal(
    image,
    palette_greens.palette,
    -0.207190825000000012496,
    0.676656624999999999983,
    255,
)
image.save("spiral_3.png")

recalc_fractal(
    image,
    palette_greens.palette,
    -0.540623850000000003876,
    0.523798050000000000019,
    255,
)
image.save("spiral_4.png")
