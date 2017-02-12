#!/usr/bin/env python

from gimpfu import *

# funkce zavolana po spusteni pluginu uzivatelem
def create_new_image():
    # vytvoreni noveho obrazku
    image = gimp.Image(256, 256, RGB);

    # vytvoreni nove hladiny
    layer = gimp.Layer(image, "Hladina", 256, 256, RGB_IMAGE, 100, NORMAL_MODE)
    layer.fill(BACKGROUND_FILL)

    # pridani hladiny do zasobniku hladin v obrazku
    image.add_layer(layer, 0)

    # zobrazeni
    gimp.Display(image)

    # zajisteni, ze se okno s obrazkem skutecne prekresli
    gimp.displays_flush()


# Registrace skriptu do prosteedi grafickeho editoru GIMP
# a specifikace parametru nastavitelnych uzivatelem,
# ktere se posleze prenesou jako parametry skriptu.
register(
    "create_new_image",
    "Vytvor novy obrazek",
    "Vytvor novy obrazek",
    "Pavel Tisnovsky",
    "Open source",
    "2017-02-11",
    "Vytvor novy obrazek",
    "", # plugin se spusti jen pokud neexistuje obrazek
    [], # zadne parametry
    [],
    create_new_image,
    menu="<Image>/Filters/Test/")

main()

