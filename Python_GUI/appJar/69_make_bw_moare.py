#!/usr/bin/env python

# Vytvoreni obrazku s "kruznicovym moare"

from PIL import Image

# velikost obrazku
# mocninou cisla 2
IMAGE_WIDTH = 256
IMAGE_HEIGHT = 256


# Funkce provadejici vypocet moare s kruznicovym vzorkem
def recalc_circle_pattern(image, xmin, ymin, xmax, ymax):
    width, height = image.size       # rozmery obrazku
    stepx = (xmax - xmin)/width
    stepy = (ymax - ymin)/height

    y1 = ymin
    for y in range(0, height):
        x1 = xmin
        for x in range(0, width):
            x1 += stepx
            x2 = x1 * x1
            y2 = y1 * y1
            i = (int)(x2 + y2) & 255
            color = (i, i, i)
            image.putpixel((x, y), color)
        y1 += stepy


mez = (2 << 5) + 50 * 2.5
image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT))

recalc_circle_pattern(image, -mez, -mez, mez, mez)
image.save("bw_moare.png")
