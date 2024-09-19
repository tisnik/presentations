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


def create_label_left_shift():
    return create_gray_label("Shift", 10, 60, "left", "bottom")


def create_label_right_shift():
    return create_gray_label("Shift", window.width - 10, 60, "right", "bottom")


window = create_window(640, 480)
label_left_control = create_label_left_control()
label_right_control = create_label_right_control()
label_left_shift = create_label_left_shift()
label_right_shift = create_label_right_shift()


def display_key_event(symbol, modifiers, new_color):
    if symbol == pyglet.window.key.LCTRL:
        label_left_control.color = new_color
    elif symbol == pyglet.window.key.RCTRL:
        label_right_control.color = new_color
    elif symbol == pyglet.window.key.LSHIFT:
        label_left_shift.color = new_color
    elif symbol == pyglet.window.key.RSHIFT:
        label_right_shift.color = new_color
    on_draw()


@window.event
def on_draw():
    window.clear()
    label_left_control.draw()
    label_right_control.draw()
    label_left_shift.draw()
    label_right_shift.draw()


@window.event
def on_key_press(symbol, modifiers):
    display_key_event(symbol, modifiers, RED)


@window.event
def on_key_release(symbol, modifiers):
    display_key_event(symbol, modifiers, GRAY)


pyglet.app.run()
