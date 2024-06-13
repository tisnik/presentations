#!/usr/bin/env python

# ---------------------------------------------------------------------
#
# Demonstrační příklady využívající knihovnu Pyglet
#
# Příklad číslo 6: ukázka použití základních funkcí OpenGL
#
# ---------------------------------------------------------------------


# všechny třídy a funkce jsou obsaženy v jediném modulu nazvaném pyglet
import pyglet

# druhý import s funkcemi převzatými z OpenGL
import pyglet.gl

# vytvoření okna
window = pyglet.window.Window(width=640, height=480, caption="Pyglet+OpenGL")


@window.event
def on_draw():
    """Obsluha události - překreslení obsahu okna."""
    pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
    pyglet.gl.glLoadIdentity()
    pyglet.gl.glBegin(pyglet.gl.GL_TRIANGLES)
    pyglet.gl.glVertex2f(0, 0)
    pyglet.gl.glVertex2f(window.width, 0)
    pyglet.gl.glVertex2f(window.width, window.height)
    pyglet.gl.glEnd()


# spuštění smyčky pro zpracování událostí
pyglet.app.run()
