#!/usr/bin/env python

# ---------------------------------------------------------------------
#
# Demonstrační příklady využívající knihovnu Pyglet
#
# Příklad číslo 11: ukázka použití základních funkcí OpenGL
#                   základní vlastnosti úseček (line)
#
# ---------------------------------------------------------------------

# všechny třídy a funkce jsou obsaženy v jediném modulu nazvaném pyglet
import pyglet

# druhý import s funkcemi převzatými z OpenGL
from pyglet.gl import *

# vytvoření okna
window = pyglet.window.Window(width=450, height=350, caption="Pyglet+OpenGL")


@window.event
def on_draw():
    """Obsluha události - překreslení obsahu okna."""
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    patterns = [0xFF00, 0xF0F0, 0xCCCC, 0x5555, 0xFE10, 0x5E32]

    glDisable(GL_LINE_SMOOTH)  # zakazani antialiasingu usecek
    glDisable(GL_LINE_STIPPLE)  # zakazani maskovani pixelu na care

    glLineWidth(1.0)  # tloustka usecky je jeden pixel
    glBegin(GL_LINES)
    for i in xrange(0, 10):  # vykresleni prvni rady usecek ruzne barvy
        step = i / 10.0
        glColor3f(
            step, 0.0, 1.0 - step
        )  # zmena barvy uvnitr prikazovych "zavorek" glBegin()/glEnd()
        glVertex2f(50.0 + 300.0 * step, 20.0)
        glColor3f(step, 1.0, 1.0 - step)
        glVertex2f(100.0 + 300.0 * step, 70.0)
    glEnd()

    for i in xrange(0, 10):  # vykresleni druhe rady usecek ruzne tloustky
        step = i / 10.0
        glLineWidth(step * 10.0 + 0.1)  # zmena tloustky usecky
        glBegin(GL_LINES)
        glColor3f(
            step, 0.0, 1.0 - step
        )  # zmena barvy uvnitr prikazovych "zavorek" glBegin()/glEnd()
        glVertex2f(50.0 + 300.0 * step, 90.0)
        glColor3f(step, 1.0, 1.0 - step)
        glVertex2f(100.0 + 300.0 * step, 140.0)
        glEnd()

    glEnable(GL_LINE_SMOOTH)  # povoleni antialiasingu usecek
    for i in xrange(0, 10):  # vykresleni treti rady usecek ruzne tloustky
        step = i / 10.0
        glLineWidth(step * 10.0 + 0.1)  # zmena tloustky usecky
        glBegin(GL_LINES)
        glColor3f(
            step, 0.0, 1.0 - step
        )  # zmena barvy uvnitr prikazovych "zavorek" glBegin()/glEnd()
        glVertex2f(50.0 + 300.0 * step, 160.0)
        glColor3f(step, 1.0, 1.0 - step)
        glVertex2f(100.0 + 300.0 * step, 210.0)
        glEnd()

    glDisable(GL_LINE_SMOOTH)  # zakazani antialiasingu usecek
    glEnable(GL_LINE_STIPPLE)  # povoleni maskovani pixelu na care
    glLineWidth(1.0)  # tloustka usecky je jeden pixel
    glColor3f(1.0, 1.0, 1.0)  # zmena barvy vne prikazovych "zavorek" glBegin()/glEnd()

    for i in xrange(0, 6):
        glLineStipple(2, patterns[i])  # nastaveni masky pri kresleni usecek
        glBegin(GL_LINES)
        glVertex2i(50, 250 + i * 20)  # vykresleni usecky
        glVertex2i(350, 250 + i * 20)
        glEnd()


# spuštění smyčky pro zpracování událostí
pyglet.app.run()
