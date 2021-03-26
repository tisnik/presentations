#!/usr/bin/env python

import pyglet

window = pyglet.window.Window(width=640,
                              height=480,
                              caption="Pyglet library")

image_stream = open("gnome-globe.png", "rb")
image = pyglet.image.load('gnome-globe.png', file=image_stream)

sprite = pyglet.sprite.Sprite(image)
sprite.x = window.width / 2
sprite.y = window.height / 2

@window.event
def on_draw():
    window.clear()
    sprite.draw()

def update(dt):
    sprite.rotation += 1


pyglet.clock.schedule_interval(update, 1/60.)
pyglet.app.run()
