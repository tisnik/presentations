#!/usr/bin/env python

"""Konstrukce kružnice."""

from PIL import Image, ImageDraw

RADIUS = 200

try:
    # vytvoření prázdného obrázku se specifikovanými rozměry
    test_image = Image.new(mode="RGB", size=(640, 480))

    # objekt umožňující kreslení do obrázku
    draw = ImageDraw.Draw(test_image)

    # rozměry obrázku
    width = test_image.size[0]
    height = test_image.size[1]

    # vykreslení čtverce, ve kterém se bude provádět konstrukce kružnice
    x1 = width / 2 - RADIUS
    y1 = height / 2 - RADIUS
    x2 = width / 2 + RADIUS
    y2 = height / 2 + RADIUS

    draw.rectangle((x1, y1, x2, y2), outline=(255, 255, 255))

    # uložení upraveného obrázku
    test_image.save("circle.png")

    # zobrazení upraveného obrázku
    test_image.show()

except Exception as e:
    print(e)
