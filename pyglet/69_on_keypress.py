#!/usr/bin/env python

import pyglet


def create_window(width, height):
    return pyglet.window.Window(width=width, height=height, caption="Pyglet library")


def create_label():
    return pyglet.text.Label(
        "Event:",
        font_size=18,
        x=window.width // 4,
        y=window.height // 2,
        anchor_x="left",
        anchor_y="center",
    )


window = create_window(640, 480)
label = create_label()


def display_key_event(symbol, modifiers, action):
    text = format("Event: key with code %d %s" % (symbol, action))
    label.text = text
    print(symbol)
    on_draw()


@window.event
def on_draw():
    window.clear()
    label.draw()


@window.event
def on_key_press(symbol, modifiers):
    display_key_event(symbol, modifiers, "pressed")


@window.event
def on_key_release(symbol, modifiers):
    display_key_event(symbol, modifiers, "released")


pyglet.app.run()
