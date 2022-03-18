#!/usr/bin/env python

import pyglet

window = pyglet.window.Window(width=640, height=480, caption="Pyglet library")

image_stream = open("gnome-globe.png", "rb")
image = pyglet.image.load("gnome-globe.png", file=image_stream)

print("Loaded image with size %d x %d pixels" % (image.width, image.height))

label = pyglet.text.Label(
    "Pyglet library",
    font_name="Terminus",
    font_size=36,
    x=window.width // 2,
    y=window.height // 2,
)


@window.event
def on_draw():
    window.clear()
    label.draw()
    image.blit(20, 20)


pyglet.app.run()
