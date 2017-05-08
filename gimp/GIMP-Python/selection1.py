#!/usr/bin/env python

from gimpfu import *

# funkce zavolana po spusteni pluginu uzivatelem
def new_image_with_circle(width, height, radius, selected_color, background_color):
    # vytvoreni noveho obrazku
    image = gimp.Image(int(width), int(height), RGB);

    # vytvoreni nove hladiny
    layer = gimp.Layer(image, "Circle", int(width), int(height), RGB_IMAGE, 100, NORMAL_MODE)

    # nastaveni barvy vykreslovani pozadi (druha barva ve vyberu)
    gimp.set_background(background_color)

    # vyplneni hladiny konstantni barvou
    layer.fill(BACKGROUND_FILL)

    # pridani hladiny do zasobniku hladin v obrazku
    image.add_layer(layer, 0)

    # vytvoreni vyberu ve tvaru kruznice
    pdb.gimp_image_select_ellipse(image,
                              CHANNEL_OP_REPLACE, # obrazek v nemz se vyber vytvori
                              width/2 - radius,   # prepsani oblasti puvodniho vyberu
                              height/2 - radius,  # levy horni roh vyberu
                              2*radius, 2*radius) # rozmery vyberu

    # nastaveni barvy vykreslovani pozadi (prvni barva ve vyberu)
    gimp.set_background(selected_color)

    # vykresleni obrazce - jeho vypln
    pdb.gimp_edit_fill(layer, BACKGROUND_FILL)

    # zobrazeni
    gimp.Display(image)

    # zajisteni, ze se okno s obrazkem skutecne prekresli
    gimp.displays_flush()


# Registrace skriptu do prostredi grafickeho editoru GIMP
# a specifikace parametru nastavitelnych uzivatelem,
# ktere se posleze prenesou jako parametry skriptu.
register(
    "new_image_with_circle",
    "Vytvor novy obrazek s kruznici.",
    "Vytvor novy obrazek s kruznici.",
    "Pavel Tisnovsky",
    "Open source",
    "2017-05-04",
    "Vytvor novy obrazek s kruznici",
    "", # plugin se spusti jen pokud neexistuje obrazek
    [   # parametry
        (PF_SPINNER, "width",      "Image width",  256, (16, 8192, 16)),
        (PF_SPINNER, "height",     "Image height", 256, (16, 8192, 16)),
        (PF_SPINNER, "radius",     "Radius",       50,  (10, 200, 10)),
        (PF_COLOR,   "color",      "Barva",        (1.0, 1.0, 0.0)),
        (PF_COLOR,   "background", "Pozadi",       (0.0, 0.0, 0.0))
    ],
    [],
    new_image_with_circle,
    menu="<Image>/Filters/Test/")

main()

