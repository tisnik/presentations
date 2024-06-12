#!/usr/bin/env python

# ---------------------------------------------------------------------
#
# Demonstrační příklady využívající knihovnu Pyglet
#
# Příklad číslo 3: obsluha události - překreslení obsahu okna
#
# ---------------------------------------------------------------------


# všechny třídy a funkce jsou obsaženy v jediném modulu nazvaném pyglet
import pyglet

# vytvoření okna
window = pyglet.window.Window(width=640, height=480, caption="Pyglet library")


@window.event
def on_draw():
    """Obsluha události - překreslení obsahu okna."""
    window.clear()


# spuštění smyčky pro zpracování událostí
pyglet.app.run()
