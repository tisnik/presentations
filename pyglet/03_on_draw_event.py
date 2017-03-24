#!/usr/bin/env python

import pyglet

window = pyglet.window.Window(width=640,
                              height=480,
                              caption="Pyglet library")

@window.event
def on_draw():
    window.clear()

pyglet.app.run()

