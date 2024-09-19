#!/usr/bin/env python

# Vytvoreni textury s "kruznicovym moare" i dalsimi typy moare

import palette_blues
import palette_gold
import palette_greens
import palette_ice
import palette_mandmap
from PIL import Image

# textura by mela byt ctvercova a jeji sirka i vyska by mela byt
# mocninou cisla 2
IMAGE_WIDTH = 256
IMAGE_HEIGHT = 256


# Funkce provadejici vypocet moare s kruznicovym ci jinym vzorkem
def recalc_any_pattern(image, palette, xmin, ymin, xmax, ymax, function):
    width, height = image.size  # rozmery obrazku
    stepx = (xmax - xmin) / width
    stepy = (ymax - ymin) / height

    y1 = ymin
    for y in range(0, height):
        x1 = xmin
        for x in range(0, width):
            x1 += stepx
            val = function(x1, y1)
            i = int(val) & 255
            color = (palette[i][0], palette[i][1], palette[i][2])
            image.putpixel((x, y), color)
        y1 += stepy


image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT))

mez = (2 << 5) + 30 * 2.5
recalc_any_pattern(
    image,
    palette_mandmap.palette,
    mez / 5,
    mez / 5,
    mez,
    mez,
    lambda x, y: x * x + y * y,
)
image.save("patternC_circle.png")

mez = (2 << 5) + 30 * 2.5
recalc_any_pattern(
    image,
    palette_mandmap.palette,
    mez / 5,
    mez / 5,
    mez,
    mez,
    lambda x, y: x * x - y * y,
)
image.save("patternC_anticircle.png")

mez = 15.0
recalc_any_pattern(
    image,
    palette_mandmap.palette,
    mez / 5,
    mez / 5,
    mez,
    mez,
    lambda x, y: x ** 3 + y ** 3,
)
image.save("patternC_x3y3.png")

mez = 15.0
recalc_any_pattern(
    image,
    palette_mandmap.palette,
    mez / 5,
    mez / 5,
    mez,
    mez,
    lambda x, y: x ** 4 + y ** 4,
)
image.save("patternC_x4y4.png")

mez = 60.0
recalc_any_pattern(
    image,
    palette_mandmap.palette,
    mez / 5,
    mez / 5,
    mez,
    mez,
    lambda x, y: x * x + y * y + x * y * 1.5,
)
image.save("patternC_var1.png")

mez = 15.0
recalc_any_pattern(
    image,
    palette_mandmap.palette,
    mez / 5,
    mez / 5,
    mez,
    mez,
    lambda x, y: x * x * y + y * y * x,
)
image.save("patternC_var2.png")
