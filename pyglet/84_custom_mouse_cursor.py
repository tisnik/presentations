#!/usr/bin/env python

import pyglet


def create_window(width, height):
    return pyglet.window.Window(width=width, height=height, caption="Pyglet library")


def load_cursor(filename):
    image = pyglet.image.load(filename)
    return pyglet.window.ImageMouseCursor(image)


window = create_window(640, 480)
cursor = load_cursor("gnome-globe.png")
window.set_mouse_cursor(cursor)


@window.event
def on_draw():
    window.clear()


pyglet.app.run()
