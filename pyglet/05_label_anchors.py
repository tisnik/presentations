#!/usr/bin/env python

import pyglet

window = pyglet.window.Window(width=640,
                              height=480,
                              caption="Pyglet library")

label1 = pyglet.text.Label("Pyglet library",
                           font_name="Terminus",
                           font_size=36,
                           x=window.width//2,
                           y=window.height//2,
                           anchor_x='center',
                           anchor_y='center')

label2 = pyglet.text.Label("Pyglet library",
                           font_name="Terminus",
                           font_size=36,
                           x=0,
                           y=window.height,
                           anchor_x='left',
                           anchor_y='top')

label3 = pyglet.text.Label("Pyglet library",
                           font_name="Terminus",
                           font_size=36,
                           x=window.width,
                           y=0,
                           anchor_x='right',
                           anchor_y='bottom')

@window.event
def on_draw():
    window.clear()
    label1.draw()
    label2.draw()
    label3.draw()

pyglet.app.run()

