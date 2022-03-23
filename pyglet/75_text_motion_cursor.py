#!/usr/bin/env python

import pyglet


def create_window(width, height):
    return pyglet.window.Window(width=width, height=height, caption="Pyglet library")


def make_sprite(filename, window):
    image_stream = open("gnome-globe.png", "rb")
    image = pyglet.image.load("gnome-globe.png", file=image_stream)

    sprite = pyglet.sprite.Sprite(image)
    # vycentrovani spritu
    sprite.x = window.width / 2 - image.width / 2
    sprite.y = window.height / 2 - image.height / 2
    sprite.step = 5
    return sprite


window = create_window(640, 480)
sprite = make_sprite("gnome-globe.png", window)


@window.event
def on_draw():
    window.clear()
    sprite.draw()


@window.event
def on_text_motion(motion):
    global sprite
    if motion == pyglet.window.key.MOTION_LEFT:
        sprite.x -= sprite.step
    elif motion == pyglet.window.key.MOTION_RIGHT:
        sprite.x += sprite.step
    elif motion == pyglet.window.key.MOTION_UP:
        sprite.y += sprite.step
    elif motion == pyglet.window.key.MOTION_DOWN:
        sprite.y -= sprite.step
    on_draw()


pyglet.app.run()
