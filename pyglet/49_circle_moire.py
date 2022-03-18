#!/usr/bin/env python

# Vytvoreni textury s "kruznicovym moare"

from PIL import Image

# textura by mela byt ctvercova a jeji sirka i vyska by mela byt
# mocninou cisla 2
IMAGE_WIDTH = 256
IMAGE_HEIGHT = 256


# Funkce provadejici vypocet moare s kruznicovym vzorkem
def recalc_circle_pattern(image, xmin, ymin, xmax, ymax):
    width, height = image.size  # rozmery obrazku
    stepx = (xmax - xmin) / width
    stepy = (ymax - ymin) / height
    print(xmin, xmax, ymin, ymax, width, height, stepx, stepy)

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


for i in range(0, 50, 10):
    image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT))
    mez = (2 << 5) + i * 2.5
    recalc_circle_pattern(image, -mez, -mez, mez, mez)
    fileName = "patternA{index:02d}.png".format(index=i)
    image.save(fileName)
