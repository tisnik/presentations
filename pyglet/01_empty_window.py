#!/usr/bin/python

# ---------------------------------------------------------------------
#
# Demonstrační příklady využívající knihovnu Pyglet
#
# Příklad číslo 1: vytvoření a zobrazení prázdného okna
#
# ---------------------------------------------------------------------


# všechny třídy a funkce jsou obsaženy v jediném modulu nazvaném pyglet
import pyglet

# vytvoření okna
window = pyglet.window.Window(width=640, height=480, caption="Pyglet library")

# spuštění smyčky pro zpracování událostí
pyglet.app.run()
