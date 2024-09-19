#!/usr/bin/env python

import pyglet

GRAY = (128, 128, 128, 255)
RED = (255, 128, 128, 255)


def create_window(width, height):
    return pyglet.window.Window(width=width, height=height, caption="Pyglet library")


def create_gray_label(text, x, y, anchor_x, anchor_y):
    return pyglet.text.Label(
        text, font_size=36, x=x, y=y, anchor_x=anchor_x, anchor_y=anchor_y, color=GRAY
    )


def create_label_left_control():
    return create_gray_label("Ctrl", 10, 10, "left", "bottom")


def create_label_right_control():
    return create_gray_label("Ctrl", window.width - 10, 10, "right", "bottom")


window = create_window(640, 480)
keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(keys)

label_left_control = create_label_left_control()
label_right_control = create_label_right_control()


@window.event
def on_draw():
    window.clear()

    if keys[pyglet.window.key.LCTRL]:
        label_left_control.color = RED
    else:
        label_left_control.color = GRAY

    if keys[pyglet.window.key.RCTRL]:
        label_right_control.color = RED
    else:
        label_right_control.color = GRAY

    label_left_control.draw()
    label_right_control.draw()


pyglet.app.run()
