#!/usr/bin/env python

import pyglet


def create_window(width, height):
    return pyglet.window.Window(width=width, height=height, caption="Pyglet library")


def create_label1():
    return pyglet.text.Label(
        "Event:",
        font_size=18,
        x=window.width // 4,
        y=window.height // 2,
        anchor_x="left",
        anchor_y="center",
    )


def create_label2():
    return pyglet.text.Label(
        "Modifiers:",
        font_size=16,
        x=window.width // 4,
        y=window.height // 2 - 32,
        anchor_x="left",
        anchor_y="center",
    )


window = create_window(640, 480)
label1 = create_label1()
label2 = create_label2()


def display_key_event(symbol, modifiers, action):
    text = format("Event: key with code %d %s" % (symbol, action))
    label1.text = text
    text = "Modifiers: "

    if modifiers & pyglet.window.key.MOD_SHIFT:
        text = text + "Shift "
    if modifiers & pyglet.window.key.MOD_CTRL:
        text = text + "Ctrl "
    if modifiers & pyglet.window.key.MOD_ALT:
        text = text + "Alt "

    label2.text = text

    on_draw()
    print(symbol, modifiers)


@window.event
def on_draw():
    window.clear()
    label1.draw()
    label2.draw()


@window.event
def on_key_press(symbol, modifiers):
    display_key_event(symbol, modifiers, "pressed")


@window.event
def on_key_release(symbol, modifiers):
    display_key_event(symbol, modifiers, "released")


pyglet.app.run()
