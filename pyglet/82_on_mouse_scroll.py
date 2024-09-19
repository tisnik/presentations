#!/usr/bin/env python

import pyglet

GRAY = (128, 128, 128, 255)
RED = (255, 128, 128, 255)


def create_window(width, height):
    return pyglet.window.Window(width=width, height=height, caption="Pyglet library")


def make_sprite(filename, window):
    image_stream = open("gnome-globe.png", "rb")
    image = pyglet.image.load("gnome-globe.png", file=image_stream)

    # stred spritu bude odpovidat stredu obrazku - sprite se nam bude
    # mnohem lepe pozicovat
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2

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
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    if buttons & pyglet.window.mouse.LEFT:
        sprite.x += dx
        sprite.y += dy


@window.event
def on_mouse_scroll(x, y, scroll_x, scroll_y):
    sprite.scale += float(scroll_y / 4.0)


pyglet.app.run()
