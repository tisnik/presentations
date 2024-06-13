#!/usr/bin/env python

# ---------------------------------------------------------------------
#
# Demonstrační příklady využívající knihovnu Pyglet
#
# Příklad číslo 8: ukázka použití základních funkcí OpenGL
#                  vykreslení trojúhelníku vyplněného RGB gradientem
#
# ---------------------------------------------------------------------

# všechny třídy a funkce jsou obsaženy v jediném modulu nazvaném pyglet
import pyglet

# druhý import s funkcemi převzatými z OpenGL
from pyglet.gl import *

# vytvoření okna
window = pyglet.window.Window(width=640, height=480, caption="Pyglet+OpenGL")


@window.event
def on_draw():
    """Obsluha události - překreslení obsahu okna."""
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)
    glVertex2f(window.width / 2, 0)
    glColor3f(0, 1, 0)
    glVertex2f(0, window.height)
    glColor3f(0, 0, 1)
    glVertex2f(window.width, window.height)
    glEnd()


# spuštění smyčky pro zpracování událostí
pyglet.app.run()
