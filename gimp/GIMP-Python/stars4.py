#!/usr/bin/env python

from random import *

from gimpfu import *


def pixel_1x1(drawable, x, y, color):
    pdb.gimp_drawable_set_pixel(drawable, x, y, 3, color)


def pixel_2x2(drawable, x, y, color):
    pdb.gimp_drawable_set_pixel(drawable, x, y, 3, color)
    pdb.gimp_drawable_set_pixel(drawable, x + 1, y, 3, color)
    pdb.gimp_drawable_set_pixel(drawable, x, y + 1, 3, color)
    pdb.gimp_drawable_set_pixel(drawable, x + 1, y + 1, 3, color)


def pixel_3x3(drawable, x, y, color):
    for dy in range(0, 3):
        for dx in range(0, 3):
            pdb.gimp_drawable_set_pixel(drawable, x + dx, y + dy, 3, color)


# funkce zavolana po spusteni pluginu uzivatelem
def create_starry_sky_4(width, height, stars1, stars2, stars3):
    # vytvoreni noveho obrazku
    image = gimp.Image(int(width), int(height), RGB)

    # vytvoreni nove hladiny
    layer = gimp.Layer(
        image, "Stars", int(width), int(height), RGB_IMAGE, 100, NORMAL_MODE
    )

    # nastaveni barvy vykreslovani pozadi (druha barva ve vyberu)
    gimp.set_background(0, 0, 40)

    # vyplneni hladiny konstantni barvou
    layer.fill(BACKGROUND_FILL)

    # pridani hladiny do zasobniku hladin v obrazku
    image.add_layer(layer, 0)

    star_color = (255, 255, 50)

    for i in range(int(stars1)):
        # pozice hvezdy v obrazku
        x = randint(0, int(width) - 1)
        y = randint(0, int(height) - 1)
        # vykresleni jedne hvezdy do obrazku
        pixel_1x1(layer, x, y, star_color)

    for i in range(int(stars2)):
        # pozice hvezdy v obrazku
        x = randint(0, int(width) - 2)
        y = randint(0, int(height) - 2)
        # vykresleni jedne hvezdy do obrazku
        pixel_2x2(layer, x, y, star_color)

    for i in range(int(stars3)):
        # pozice hvezdy v obrazku
        x = randint(0, int(width) - 3)
        y = randint(0, int(height) - 3)
        # vykresleni jedne hvezdy do obrazku
        pixel_3x3(layer, x, y, star_color)

    # zobrazeni
    gimp.Display(image)

    # zajisteni, ze se okno s obrazkem skutecne prekresli
    gimp.displays_flush()


# Registrace skriptu do prostredi grafickeho editoru GIMP
# a specifikace parametru nastavitelnych uzivatelem,
# ktere se posleze prenesou jako parametry skriptu.
register(
    "create_starry_sky_4",
    "Vytvor novy obrazek s hvezdnou oblohou (4)",
    "Vytvor novy obrazek s hvezdnou oblohou (4)",
    "Pavel Tisnovsky",
    "Open source",
    "2017-03-16",
    "Vytvor novy obrazek s hvezdnou oblohou (4)",
    "",  # plugin se spusti jen pokud neexistuje obrazek
    [
        (PF_SPINNER, "width", "Image width", 256, (16, 8192, 16)),
        (PF_SPINNER, "height", "Image height", 256, (16, 8192, 16)),
        (PF_SPINNER, "stars1", "Stars1", 200, (10, 2000, 10)),
        (PF_SPINNER, "stars2", "Stars2", 50, (10, 2000, 10)),
        (PF_SPINNER, "stars3", "Stars3", 5, (10, 2000, 10)),
    ],
    [],
    create_starry_sky_4,
    menu="<Image>/Filters/Test/",
)

main()
