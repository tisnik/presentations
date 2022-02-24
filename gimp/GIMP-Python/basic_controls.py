#!/usr/bin/env python

from gimpfu import *


# funkce zavolana po spusteni pluginu uzivatelem
def basic_controls():
    pass


# Registrace skriptu do prosteedi grafickeho editoru GIMP
# a specifikace parametru nastavitelnych uzivatelem,
# ktere se posleze prenesou jako parametry skriptu.
register(
    "basic_controls",
    "Zobrazeni zakladnich ovladacich prvku",
    "Zobrazeni zakladnich ovladacich prvku",
    "Pavel Tisnovsky",
    "Open source",
    "2017-02-11",
    "Zobrazeni zakladnich ovladacich prvku",
    "",  # plugin se spusti jen pokud neexistuje obrazek
    [
        (PF_INT, "number", "Cele cislo", 42),
        (PF_FLOAT, "angle", "Desetinne cislo", 0.5),
        (PF_STRING, "string", "String", "bla bla"),
        (PF_TEXT, "text", "Text", "The quick red fox jumped over the lazy dog"),
        (PF_BOOL, "prepinac", "Prepinac", True),
        (PF_TOGGLE, "prepinac2", "Prepinac2", 1),
        (PF_OPTION, "vyber1", "List box", 2, ("foo", "bar", "baz")),
        (PF_RADIO, "vyber2", "Prepinace", "jpg", (("png", "png"), ("jpg", "jpg"))),
        (PF_SPINNER, "spinner", "Numericky vstup", 42, (1, 8000, 1)),
        (PF_SLIDER, "slider", "Posuvnik", 100, (0, 100, 1)),
        (PF_COLOR, "color", "Barva", (1.0, 1.0, 1.0)),
    ],
    [],
    basic_controls,
    menu="<Image>/Filters/Test/",
)

main()
