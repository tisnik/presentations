#!/usr/bin/env python

import pyglet

GRAY = (128, 128, 128, 255)


def create_window(width, height):
    return pyglet.window.Window(width=width, height=height, caption="Pyglet library")


def create_gray_label(text, x, y, anchor_x, anchor_y):
    return pyglet.text.Label(
        text, font_size=18, x=x, y=y, anchor_x=anchor_x, anchor_y=anchor_y, color=GRAY
    )


window = create_window(640, 480)
label = create_gray_label("P - play again", 10, 10, "left", "bottom")


@window.event
def on_draw():
    window.clear()
    label.draw()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.P:
        source.play()


pyglet.options["audio"] = ("pulse", "openal", "silent")

source = pyglet.media.load("login.wav", streaming=False)

pyglet.app.run()
