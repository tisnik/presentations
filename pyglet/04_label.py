#!/usr/bin/env python
# vim: set fileencoding=utf-8

# Demonstrační příklady využívající knihovnu Pyglet

# všechny třídy a funkce jsou obsaženy v jediném modulu pyglet
import pyglet

# vytvoření okna
window = pyglet.window.Window(width=640,
                              height=480,
                              caption="Pyglet library")

label = pyglet.text.Label("Pyglet library",
                          font_name="Terminus",
                          font_size=36,
                          x=window.width//2,
                          y=window.height//2)


@window.event
def on_draw():
    """Obsluha události."""
    window.clear()
    label.draw()


# spuštění smyčky pro zpracování událostí
pyglet.app.run()
