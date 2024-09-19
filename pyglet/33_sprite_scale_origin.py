#!/usr/bin/env python

import math

import pyglet

window = pyglet.window.Window(width=640, height=480, caption="Pyglet library")

image_stream = open("gnome-globe.png", "rb")
image = pyglet.image.load("gnome-globe.png", file=image_stream)

image.anchor_x = image.width / 2
image.anchor_y = image.height / 2

sprite = pyglet.sprite.Sprite(image)
sprite.x = window.width / 2
sprite.y = window.height / 2
sprite.t = 0


@window.event
def on_draw():
    window.clear()
    sprite.draw()


def update(dt):
    sprite.t += 1
    sprite.scale = 5.0 * math.sin(sprite.t / 10.0)


pyglet.clock.schedule_interval(update, 1 / 60.0)
pyglet.app.run()
