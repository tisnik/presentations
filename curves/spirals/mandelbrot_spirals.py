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

"""Vykreslení spirál v Mandelbrotově množině."""

import palette_mandmap
from PIL import Image

IMAGE_WIDTH = 800
IMAGE_HEIGHT = 600


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

recalc_fractal(
    image,
    palette_mandmap.palette,
    -0.769824999999999998320,
    -0.109270000000000000000,
    -0.766247499999999998426,
    -0.106570000000000000000,
    1000,
)
image.save("spiral_1.png")

recalc_fractal(
    image,
    palette_mandmap.palette,
    -0.171119200000000013445,
    0.657309400000000000000,
    -0.169318975000000013445,
    0.658660750000000000000,
    1000,
)
image.save("spiral_2.png")

recalc_fractal(
    image,
    palette_mandmap.palette,
    -0.207190825000000012496,
    0.676656624999999999983,
    -0.206107925000000012496,
    0.677468799999999999983,
    1000,
)
image.save("spiral_3.png")

recalc_fractal(
    image,
    palette_mandmap.palette,
    -0.540623850000000003876,
    0.523798050000000000019,
    -0.532306600000000003876,
    0.530031950000000000019,
    1000,
)
image.save("spiral_4.png")
