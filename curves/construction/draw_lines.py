#!/usr/bin/env python

"""Vykreslení úseček knihovnou PIL/Pillow."""

from PIL import Image
from PIL import ImageDraw

try:
    # vytvoření prázdného obrázku se specifikovanými rozměry
    test_image = Image.new(mode="RGB", size=(640, 480))

    # objekt umožňující kreslení do obrázku
    draw = ImageDraw.Draw(test_image)

    # rozměry obrázku
    width = test_image.size[0]
    height = test_image.size[1]

    # vertikální úsečky
    for x in range(0, width, 30):
        draw.line((x, 0, x, height - 1), fill=(255, 255, 255))

    # horizontální úsečky
    for y in range(0, height, 30):
        draw.line((0, y, width - 1, y), fill=(255, 255, 255))

    # uložení upraveného obrázku
    test_image.save("grid.png")

    # zobrazení upraveného obrázku
    test_image.show()

except Exception as e:
    print(e)
