#!/usr/bin/env python

import pyglet
from pyglet.gl import *


window = pyglet.window.Window(width=640,
                              height=480,
                              caption="Pyglet+OpenGL")


@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0)
    glVertex2f(window.width, 0)
    glVertex2f(window.width, window.height)
    glEnd()


pyglet.app.run()
