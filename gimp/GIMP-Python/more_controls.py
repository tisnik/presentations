#!/usr/bin/env python

from gimpfu import *


# funkce zavolana po spusteni pluginu uzivatelem
def more_controls():
    pass


# Registrace skriptu do prosteedi grafickeho editoru GIMP
# a specifikace parametru nastavitelnych uzivatelem,
# ktere se posleze prenesou jako parametry skriptu.
register(
    "more_controls",
    "Zobrazeni dalsich ovladacich prvku",
    "Zobrazeni dalsich ovladacich prvku",
    "Pavel Tisnovsky",
    "Open source",
    "2017-02-11",
    "Zobrazeni dalsich ovladacich prvku",
    "*",  # plugin se spusti jen pokud existuje obrazek
    [
        (PF_PALETTE, "palette", "Paleta", ""),
        (PF_BRUSH, "brush", "Stetec", None),
        (PF_PATTERN, "pattern", "Vzorek", None),
        (PF_GRADIENT, "gradient", "Gradient", None),
        (PF_FONT, "font", "Font", "Sans"),
        (PF_IMAGE, "image", "Obrazek", None),
        (PF_LAYER, "layer", "Hladina", None),
        (PF_CHANNEL, "channel", "Kanal", None),
        (PF_DRAWABLE, "drawable", "Drawable", None),
        (PF_FILE, "imagefile", "Image file", ""),
        (PF_DIRNAME, "dir", "Directory", "/tmp"),
    ],
    [],
    more_controls,
    menu="<Image>/Filters/Test/",
)

main()
