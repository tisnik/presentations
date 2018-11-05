#!/usr/bin/env python
# vim: set fileencoding=utf-8

# Demonstrační příklady využívající knihovnu Pyglet

import pyglet

# vytvoření okna
window = pyglet.window.Window(width=640,
                              height=480,
                              caption="Pyglet library")


@window.event
def on_draw():
    window.clear()


# spuštění smyčky pro zpracování událostí
pyglet.app.run()
