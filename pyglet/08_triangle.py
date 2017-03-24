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
    glColor3f(1, 0, 0)
    glVertex2f(window.width/2, 0)
    glColor3f(0, 1, 0)
    glVertex2f(0, window.height)
    glColor3f(0, 0, 1)
    glVertex2f(window.width, window.height)
    glEnd()

pyglet.app.run()

