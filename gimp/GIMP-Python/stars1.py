#!/usr/bin/env python

from random import *

from gimpfu import *


# funkce zavolana po spusteni pluginu uzivatelem
def create_starry_sky_1(width, height, stars):
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

    for i in range(int(stars)):
        # pozice hvezdy v obrazku
        x = randint(0, int(width) - 1)
        y = randint(0, int(height) - 1)
        # vykresleni jedne hvezdy do obrazku
        pdb.gimp_drawable_set_pixel(layer, x, y, 3, (255, 255, 50))

    # zobrazeni
    gimp.Display(image)

    # zajisteni, ze se okno s obrazkem skutecne prekresli
    gimp.displays_flush()


# Registrace skriptu do prostredi grafickeho editoru GIMP
# a specifikace parametru nastavitelnych uzivatelem,
# ktere se posleze prenesou jako parametry skriptu.
register(
    "create_starry_sky_1",
    "Vytvor novy obrazek s hvezdnou oblohou",
    "Vytvor novy obrazek s hvezdnou oblohou",
    "Pavel Tisnovsky",
    "Open source",
    "2017-03-16",
    "Vytvor novy obrazek s hvezdnou oblohou",
    "",  # plugin se spusti jen pokud neexistuje obrazek
    [
        (PF_SPINNER, "width", "Image width", 256, (16, 8192, 16)),
        (PF_SPINNER, "height", "Image height", 256, (16, 8192, 16)),
        (PF_SPINNER, "stars", "Stars", 250, (10, 2000, 10)),
    ],
    [],
    create_starry_sky_1,
    menu="<Image>/Filters/Test/",
)

main()
