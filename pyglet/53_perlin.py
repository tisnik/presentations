#!/usr/bin/env python

# Perlinuv sum

import math
from random import random

import numpy as np
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


def compute_min_max(bitmap, width, height):
    # pro prepocet intenzit pixelu
    min = float("inf")
    max = float("-inf")

    # ziskani statistiky o obrazku - minimalni a maximalni hodnoty
    for j in range(height):
        for i in range(width):
            z = bitmap[j][i]
            if max < z:
                max = z
            if min > z:
                min = z
    return min, max


def convert_to_image(bitmap, image, width, height, palette):
    print("contrast adjustment")

    min, max = compute_min_max(bitmap, width, height)
    k = 255.0 / (max - min)

    # zmena kontrastu a kopie bitmapy
    for y in range(height):
        for x in range(width):
            f = float(bitmap[y][x])
            f -= min
            f *= k
            i = int(f) & 255
            color = (palette[i][0], palette[i][1], palette[i][2])
            image.putpixel((x, y), color)


def random_array(width, height, amplitude):
    return [[random() * amplitude for i in range(width)] for j in range(height)]


def perlin_noise(image, palette, noise, octaves):
    width, height = image.size  # rozmery obrazku

    bitmap = np.zeros([height, width])

    # postupne vytvoreni 'octaves' vrstev v obrazku
    for k in range(octaves):
        size = 2 ** k + 1
        amplitude = noise ** k

        # vytvoreni pole nahodnych cisel o dane amplidude
        array = random_array(size, size, amplitude)

        n = width / float(size - 1.0)

        # interpolace hodnot v poli nahodnych cisel
        for y in range(height):
            for x in range(width):
                i = int(x / n)  # prepocet mezi pozici pixelu a indexem v poli
                j = int(y / n)
                x0 = x - i * n
                x1 = n - x0
                y0 = y - j * n
                y1 = n - y0
                # interpolace
                z = array[j][i] * x1 * y1
                z += array[j][i + 1] * x0 * y1
                z += array[j + 1][i] * x1 * y0
                z += array[j + 1][i + 1] * x0 * y0
                z /= n * n
                bitmap[y][x] += z

    convert_to_image(bitmap, image, width, height, palette)


image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT))

perlin_noise(image, palette_mandmap.palette, 0.7, 6)
image.save("patternE_perlin_noise1.png")

perlin_noise(image, palette_mandmap.palette, 0.7, 7)
image.save("patternE_perlin_noise2.png")

perlin_noise(image, palette_blues.palette, 0.7, 9)
image.save("patternE_perlin_noise3.png")

perlin_noise(image, palette_gold.palette, 0.7, 11)
image.save("patternE_perlin_noise4.png")

perlin_noise(image, palette_greens.palette, 0.3, 12)
image.save("patternE_perlin_noise5.png")
