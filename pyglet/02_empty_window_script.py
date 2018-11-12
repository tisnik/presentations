#!/usr/bin/env python
# vim: set fileencoding=utf-8

# Demonstrační příklady využívající knihovnu Pyglet

# všechny třídy a funkce jsou obsaženy v jediném modulu pyglet
import pyglet

# vytvoření okna
window = pyglet.window.Window(width=640,
                              height=480,
                              caption="Pyglet library")

# spuštění smyčky pro zpracování událostí
pyglet.app.run()
