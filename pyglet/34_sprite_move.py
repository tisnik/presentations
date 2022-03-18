#!/usr/bin/env python

import pyglet

window = pyglet.window.Window(width=640, height=480, caption="Pyglet library")

image_stream = open("gnome-globe.png", "rb")
image = pyglet.image.load("gnome-globe.png", file=image_stream)

sprite = pyglet.sprite.Sprite(image)
sprite.dx = 1
sprite.dy = 1


@window.event
def on_draw():
    window.clear()
    sprite.draw()


def update(dt):
    sprite.x += sprite.dx * dt * 200
    sprite.y += sprite.dy * dt * 200
    if sprite.x < 0:
        sprite.x = 0
        sprite.dx = -sprite.dx
    if sprite.y < 0:
        sprite.y = 0
        sprite.dy = -sprite.dy
    if sprite.x + sprite.width > window.width:
        sprite.x = window.width - sprite.width
        sprite.dx = -sprite.dx
    if sprite.y + sprite.height > window.height:
        sprite.y = window.height - sprite.height
        sprite.dy = -sprite.dy


pyglet.clock.schedule_interval(update, 1 / 60.0)
pyglet.app.run()
