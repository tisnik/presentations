#!/usr/bin/env python

# ---------------------------------------------------------------------
#
# Demonstrační příklady využívající knihovnu Pyglet
#
# Příklad číslo 4: použití textového návěští
#
# ---------------------------------------------------------------------


# všechny třídy a funkce jsou obsaženy v jediném modulu nazvaném pyglet
import pyglet

# vytvoření okna
window = pyglet.window.Window(width=640, height=480, caption="Pyglet library")

# textové návěští, které se má zobrazit v oknu
label = pyglet.text.Label(
    "Pyglet library",
    font_name="Terminus",
    font_size=36,
    x=window.width // 2,
    y=window.height // 2,
)


@window.event
def on_draw():
    """Obsluha události - překreslení obsahu okna."""
    window.clear()
    label.draw()


# spuštění smyčky pro zpracování událostí
pyglet.app.run()
