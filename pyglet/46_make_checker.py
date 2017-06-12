#!/usr/bin/env python

# Vytvoreni textury sachovnice

from PIL import Image

IMAGE_WIDTH = 200
IMAGE_HEIGHT = 200

SQUARE_SIZE = 10

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT))

for y in range(0, IMAGE_HEIGHT):
    for x in range(0, IMAGE_WIDTH):
        color = BLACK
        xs = x / SQUARE_SIZE
        ys = y / SQUARE_SIZE
        if (xs + ys) % 2 == 0:
            color = WHITE

        image.putpixel((x, y), color)

image.save("checker.png")
