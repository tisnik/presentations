#!/usr/bin/env python

import pyglet


def create_window(width, height):
    return pyglet.window.Window(width=width, height=height, caption="Pyglet library")


def create_label():
    return pyglet.text.Label(
        "Motion:",
        font_size=18,
        x=10,
        y=window.height // 2,
        anchor_x="left",
        anchor_y="center",
    )


window = create_window(640, 480)
label = create_label()


@window.event
def on_draw():
    window.clear()
    label.draw()


@window.event
def on_text_motion(motion):
    global x
    if motion == pyglet.window.key.MOTION_LEFT:
        label.text = "Motion: left"
    elif motion == pyglet.window.key.MOTION_RIGHT:
        label.text = "Motion: right"
    print(motion)
    on_draw()


pyglet.app.run()
