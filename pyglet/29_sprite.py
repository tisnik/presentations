#!/usr/bin/env python

import pyglet

window = pyglet.window.Window(width=640, height=480, caption="Pyglet library")

image_stream = open("gnome-globe.png", "rb")
image = pyglet.image.load("gnome-globe.png", file=image_stream)

sprite = pyglet.sprite.Sprite(image)


@window.event
def on_draw():
    window.clear()
    sprite.draw()


pyglet.app.run()
