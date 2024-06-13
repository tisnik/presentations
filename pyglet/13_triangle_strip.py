#!/usr/bin/env python

# Demonstrační příklady využívající knihovnu Pyglet

import pyglet
from pyglet.gl import *

# vytvoření okna
window = pyglet.window.Window(width=450, height=350, caption="Pyglet+OpenGL")


def draw_triangle_strip(x, y):
    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(1.0, 0.0, 0.0)  # kazdy vertex bude vykresleny jinou barvou
    glVertex2i(x, y)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2i(x + 50, y + 80)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2i(x + 100, y)
    glColor3f(1.0, 1.0, 0.0)  # kazdy vertex bude vykresleny jinou barvou
    glVertex2i(x + 150, y + 80)
    glColor3f(0.0, 1.0, 1.0)
    glVertex2i(x + 200, y)
    glColor3f(1.0, 0.0, 1.0)
    glVertex2i(x + 250, y + 80)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2i(x + 300, y)
    glEnd()


@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    glClearColor(0.0, 0.0, 0.0, 0.0)  # nastaveni mazaci barvy na cernou
    glClear(GL_COLOR_BUFFER_BIT)  # vymazani bitovych rovin barvoveho bufferu

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    draw_triangle_strip(50, 50)

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    draw_triangle_strip(50, 200)


pyglet.app.run()
